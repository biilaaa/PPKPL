## Week 2 – Action Item Extractor

### Project overview

This project is a compact full‑stack application that converts free‑form notes into a checklist of action items.
The backend is a FastAPI service backed by a SQLite database; the frontend is a minimal HTML page that interacts
with the API using `fetch`. The core functionality—action‑item extraction—is implemented in two complementary ways:

- **Heuristic extractor**: uses regular expressions and simple rules to detect bullets, TODO markers, and
  imperative sentences.
- **LLM‑based extractor**: calls a local Ollama model to extract action items as structured JSON.

Together, these components provide a concise example of “agentic” behavior: the frontend collects user notes, the
backend persists and routes requests, and an LLM is invoked behind the scenes to help interpret the text.


### Tech stack

- **Language**: Python 3.12+
- **Web framework**: FastAPI
- **ASGI server**: Uvicorn
- **Database**: SQLite (via `sqlite3` in the standard library)
- **ORM / DB access**: manual SQL with lightweight helper functions in `app/db.py`
- **LLM runtime**: [Ollama](https://ollama.com/) using the `ollama` Python package  
  - Model used: `llama3.1:8b` for LLM‑based extraction
- **Environment loading**: `python-dotenv` (`load_dotenv()` in `services/extract.py`)
- **Testing**: `pytest`
- **Frontend**: static HTML/JS (`frontend/index.html`) served by FastAPI’s `StaticFiles`


### Setup instructions

All commands below assume you are in the project root (the directory that contains the `week2/` folder).

#### 1. Create and activate a conda environment

```bash
conda create -n cs146s python=3.12 -y
conda activate cs146s
```

#### 2. Install dependencies (Poetry / pip)

If you are using Poetry (recommended by the assignment instructions):

```bash
# From the project root
poetry install
```

If this repository does not yet contain a `pyproject.toml`, install the core dependencies directly:

```bash
pip install fastapi uvicorn[standard] pydantic python-dotenv ollama pytest
```

#### 3. Ensure Ollama and the model are available

1. Install Ollama from `https://ollama.com/` and verify that the `ollama` CLI is on your `PATH`.
2. Pull the model used by the LLM extractor:

```bash
ollama pull llama3.1:8b
```

The backend calls `ollama.chat(model="llama3.1:8b", ...)` in `week2/app/services/extract.py`.

#### 4. Run the FastAPI application with Uvicorn

Using Poetry (recommended):

```bash
poetry run uvicorn week2.app.main:app --reload
```

Or with plain `uvicorn`:

```bash
uvicorn week2.app.main:app --reload
```

Then open the frontend in a browser:

- `http://127.0.0.1:8000/` – main HTML UI
- `http://127.0.0.1:8000/docs` – auto‑generated Swagger UI for the API


### Folder structure

At a high level, the `week2` folder is organized as follows:

```text
week2/
  app/
    __init__.py
    main.py          # FastAPI app entrypoint, static mounting, router registration
    config.py        # Centralized paths (data directory, DB path, frontend directory, app title)
    db.py            # SQLite helpers: init_db, insert/list notes, insert/list/mark action items
    schemas.py       # Pydantic models for request/response contracts (not yet wired everywhere)
    routers/
      __init__.py
      notes.py       # /notes endpoints for creating and listing notes
      action_items.py# /action-items endpoints for extraction and listing
    services/
      __init__.py
      extract.py     # Heuristic and LLM‑based extraction logic
  frontend/
    index.html       # Minimal HTML/JS UI calling the backend via fetch
  tests/
    __init__.py
    test_extract.py  # Unit tests for heuristic and LLM extraction
  assignment.md      # Original assignment description and TODOs
  writeup.md         # Space for your own notes and prompts
  data/
    app.db           # SQLite database file (created at runtime)
```


### API endpoints

All endpoints are served under the main FastAPI app defined in `week2/app/main.py`.  
The most relevant routes and their behavior are summarized below.

#### Notes routes (`/notes`)

- **GET `/notes`**
  - **Description**: List all saved notes.
  - **Query params**: none.
  - **Response** (`200 OK`): JSON array of note objects:
    - `id: int`
    - `content: str`
    - `created_at: str`
  - **Error handling**:
    - Returns `500 Internal Server Error` with `{"detail": "failed to retrieve notes"}` if the
      underlying DB query raises an unexpected exception.

- **POST `/notes`**
  - **Description**: Create a new note.
  - **Request body** (JSON):
    - `content: str` – raw note content (required).
  - **Response** (`200 OK`): created note as JSON:
    - `id: int`
    - `content: str`
    - `created_at: str`
  - **Error handling**:
    - If `content` is missing or empty, returns `400 Bad Request` with
      `{"detail": "content is required"}`.

- **GET `/notes/{note_id}`**
  - **Description**: Fetch a single note by ID.
  - **Path params**:
    - `note_id: int`
  - **Response** (`200 OK`): same shape as POST `/notes`.
  - **Error handling**:
    - If the note does not exist, returns `404 Not Found` with `{"detail": "note not found"}`.


#### Action‑items routes (`/action-items`)

All extraction endpoints share a common request contract:

- **Request body** (JSON):
  - `text: str` – source text with potential action items (required).
  - `save_note: bool` – when `true`, the original text is stored as a note before extraction.

The responses for extraction endpoints have the same shape:

- **Response JSON**:
  - `note_id: int | null` – ID of the stored note if `save_note` was `true`, else `null`.
  - `items: List[{ id: int, text: str }]` – persisted action items.

Individual routes:

- **POST `/action-items/extract`**
  - **Description**: Extract action items using the **heuristic** extractor
    (`extract_action_items` in `services/extract.py`).
  - **Behavior**:
    - Optionally saves the note.
    - Calls the heuristic extractor.
    - Persists each action item via `db.insert_action_items`.
  - **Error handling**:
    - If `text` is empty or missing, returns `400 Bad Request` with
      `{"detail": "text is required"}`.

- **POST `/action-items/extract_llm`**
  - **Description**: Extract action items using the **LLM‑based** extractor
    (`extract_action_items_llm` in `services/extract.py`), backed by Ollama.
  - **Behavior**:
    - Same request body and response format as `/action-items/extract`.
    - Delegates extraction to the LLM function, then persists results.
  - **Error handling**:
    - Same `400 Bad Request` behavior as `/action-items/extract` for missing/empty `text`.
    - Internal LLM and JSON parsing errors are handled inside
      `extract_action_items_llm`, which falls back to returning an empty list rather
      than raising.

- **GET `/action-items`**
  - **Description**: List action items.
  - **Query params**:
    - `note_id: int | null` – if provided, filters items to a specific note.
  - **Response** (`200 OK`): JSON array of action items:
    - `id: int`
    - `note_id: int | null`
    - `text: str`
    - `done: bool`
    - `created_at: str`

- **POST `/action-items/{action_item_id}/done`**
  - **Description**: Mark an action item as done/undone.
  - **Path params**:
    - `action_item_id: int`
  - **Request body** (JSON):
    - `done: bool` – defaults to `true` if omitted.
  - **Response** (`200 OK`):
    - `{"id": <action_item_id>, "done": <bool>}`


### Heuristic vs. LLM extraction

The core extraction logic lives in `week2/app/services/extract.py`, which defines two
complementary strategies.

#### Heuristic extractor – `extract_action_items(text: str) -> List[str]`

- Splits the text into lines.
- Detects action lines using:
  - Bullet prefixes (`-`, `*`, `•`, `1.`, etc.).
  - Keyword prefixes like `todo:`, `action:`, `next:`.
  - Checkbox markers `[ ]` or `[todo]`.
- Cleans each line to remove bullet markers and checkbox patterns.
- If nothing is found, falls back to a sentence‑level heuristic:
  - Splits into sentences and searches for those that start with imperative verbs such as
    “add”, “create”, “implement”, “fix”, etc.
- Deduplicates results while preserving order.
- This approach is **fast and deterministic**, with no external dependencies.

#### LLM extractor – `extract_action_items_llm(text: str) -> list[str]`

- Uses `ollama.chat` with the `llama3.1:8b` model.
- Sends a **system prompt** instructing the model to:
  - Read meeting notes or free‑form text.
  - Return **only a JSON array of strings**, each a concise actionable task.
  - Example: `["Follow up with the client", "Prepare the report"]`.
- The function then:
  - Strips code fences such as ```json ... ``` if present.
  - Parses the content as JSON.
  - Validates that the result is a list of non‑empty strings.
  - Returns an empty list on any error (network issues, invalid JSON, wrong type,
    etc.), using broad `try/except` and explicit `json.JSONDecodeError` handling.
- This approach is **more flexible and context‑aware**, and can infer action items that
  do not follow rigid textual patterns.

Both implementations are preserved so you can compare behavior side‑by‑side via the
two separate API endpoints (`/action-items/extract` vs `/action-items/extract_llm`).


### Frontend → backend → LLM “agentic” integration

The `frontend/index.html` file provides a lightweight UI that illustrates how the different
parts of the system interact:

- The user pastes notes into a `<textarea>` and chooses whether to “Save as note”.
- Three buttons are available:
  - **Extract** – calls `POST /action-items/extract` (heuristic extractor).
  - **Extract LLM** – calls `POST /action-items/extract_llm` (LLM extractor via Ollama).
  - **List Notes** – calls `GET /notes` to show all saved notes.
- JavaScript uses `fetch` to call these endpoints without reloading the page and renders:
  - Extracted action items as a list of checkboxes that post back to
    `/action-items/{id}/done` when toggled.
  - All notes as a simple list of `#id content` rows.

From an “agentic” perspective, the control flow is:

1. **Frontend**: collects user input and issues HTTP requests based on which button is pressed.
2. **Backend (FastAPI)**: validates input, optionally persists notes, decides whether to use the
   heuristic or LLM extractor, and saves the results to SQLite.
3. **LLM (via Ollama)**: for LLM extraction, receives a structured prompt, returns a JSON array
   of action items, which the backend parses and stores.
4. **Frontend**: renders the updated state (items / notes) dynamically in the browser.

This constitutes a simple yet realistic pattern for integrating LLMs into a web application
without exposing them directly to the client.


### Running tests

The test suite currently focuses on the extraction logic in `week2/tests/test_extract.py`,
covering both the heuristic and LLM‑based extractors.

To run the tests with Poetry:

```bash
cd path/to/project/root
poetry run pytest week2/tests
```

Or, using plain `pytest` in your active environment:

```bash
cd path/to/project/root
pytest week2/tests
```

The tests for `extract_action_items_llm` **do not** call a real LLM. They monkeypatch the global
`chat` function in `services/extract.py` to return controlled JSON strings, ensuring that unit
tests are deterministic, fast, and independent of the Ollama runtime.


### Notes and further improvements

- The `schemas.py` module defines Pydantic models that can be progressively wired into the
  routers as explicit `response_model` and request body types to strengthen the API contract.
- Error handling is intentionally simple and kept close to the endpoints so that students can
  experiment with more advanced patterns (custom exception handlers, logging, etc.).
- The current design keeps the architecture modular:
  - Routers focus on HTTP validation and shaping responses.
  - `db.py` isolates persistence concerns.
  - `services/extract.py` encapsulates all extraction logic.

