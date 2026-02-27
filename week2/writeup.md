# Week 2 Write-up

Tip: To preview this markdown file

- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: Zahra Nabila  
SUNet ID: your_sunet_id  
Citations: Ollama documentation (https://ollama.com/blog/structured-outputs), FastAPI documentation

This assignment took me about 7 hours to do.

## YOUR RESPONSES

For each exercise, please include what prompts you used to generate the answer, in addition to the location of the generated response. Make sure to clearly add comments in your code documenting which parts are generated.

### Exercise 1: Scaffold a New Feature

Prompt:

## Prompt Used (Initial Implementation)

Analyze the existing extract_action_items() function.

Create a new function called extract_action_items_llm(text: str) -> list[str].

Requirements:

- Use the ollama Python package.
- Use model "mistral:7b".
- Send a prompt instructing the model to extract actionable tasks.
- Return ONLY a JSON array of strings.
- Parse the JSON safely.
- Add proper error handling (return empty list on failure).
- Do not modify the existing heuristic function.
- Add docstrings and comments explaining the implementation.

## Prompt Used (Refactor Model Selection)

Refactor extract_action_items_llm() to use the model "llama3.1:8b" instead of "mistral:7b".

Do not modify any other logic.
Preserve structured JSON handling and error handling.
Only change the model name.

TODO

- Added new function `extract_action_items_llm(text: str) -> list[str]` in `week2/app/services/extract.py`.
- Integrated Ollama using the `chat()` function.
- Updated model selection to `llama3.1:8b` after verifying available models.
- Implemented structured JSON output parsing using `json.loads()`.
- Added defensive error handling to return an empty list on failure.
- Preserved the original heuristic-based `extract_action_items()` function without modification.
- Added docstrings and inline comments explaining the LLM integration.

Generated Code Snippets:

week2/app/services/extract.py

- Added function `extract_action_items_llm(text: str) -> list[str]`

TODO: List all modified code files with the relevant line numbers.

- Approximate location: lines 90–150

### Exercise 2: Add Unit Tests

Prompt:
Add unit tests for extract_action_items_llm() in this file.

Requirements:

- Test bullet list input.
- Test keyword-prefixed lines like "TODO:".
- Test empty input.
- Test non-action text.
- Assert that the return type is always a list.
- Do NOT modify existing heuristic extractor tests.
- Add clear comments explaining each test case.
- Avoid overly strict equality assertions since LLM output may vary slightly.

TODO:

- Added unit tests for `extract_action_items_llm()` in `week2/tests/test_extract.py`.
- Covered bullet list input.
- Covered keyword-prefixed input (e.g., "TODO:").
- Covered empty input case.
- Covered non-action text case.
- Ensured return type is always a list.
- Avoided strict equality assertions to account for minor LLM variation.

Generated Code Snippets:
week2/tests/test_extract.py  
Added new test cases for `extract_action_items_llm()`

TODO: List all modified code files with the relevant line numbers.
Approximate location: line 5-6 and 23-97

### Exercise 3: Refactor Existing Code for Clarity

Prompt:
Refactor the backend code for clarity and maintainability.

Focus on:

- Defining clear Pydantic request and response schemas.
- Improving API contract definitions.
- Cleaning up database interactions if needed.
- Centralizing configuration where possible.
- Improving error handling with proper HTTP exceptions.
- Adding meaningful comments where necessary.

Do not break existing functionality.
Do not remove heuristic or LLM extraction functions.
Keep the architecture clean and modular.

TODO

- Refactored backend structure for improved readability and maintainability.
- Improved API contract definitions using clearer request/response models.
- Enhanced error handling with proper HTTP exceptions.
- Added additional comments and documentation for clarity.
- Ensured no regression in heuristic or LLM extraction functionality.
- Preserved existing endpoints and frontend behavior.

Generated/Modified Code Snippets:
week2/app/main.py

- Refactored API endpoint definitions
- Improved request/response handling
- Approximate location: relevant endpoint sections

week2/app/routers/... (if modified)

- Improved route clarity and typing

week2/app/database/... (if modified)

- Cleaned up database interaction logic

TODO: List all modified code files with the relevant line numbers. (We anticipate there may be multiple scattered changes here – just produce as comprehensive of a list as you can.)
week2/app/db.py

- Minor structural refactoring for clarity
- Small updates to database session handling
- Scattered minor changes throughout file

week2/app/main.py

- Improved API structure and error handling
- Minor refactoring for readability
- Scattered minor changes throughout file

week2/app/services/extract.py

- Minor cleanup and typing improvements
- No major functional changes

week2/tests/test_extract.py

- Adjusted test structure to align with refactored backend
- Minor updates for clarity

### Exercise 4: Use Agentic Mode to Automate a Small Task

Prompt:
Prompt Used (LLM Endpoint)
Add a new POST endpoint called "/extract_llm".
Requirements:

- Accept the same request body schema as the existing extract endpoint.
- Call extract_action_items_llm().
- Return the extracted items in the same response format.
- Add proper error handling.
- Do not modify the existing heuristic endpoint.
- Keep API contracts consistent.

Prompt Used (List Notes Endpoint)
Add a new GET endpoint called "/notes".
Requirements:

- Retrieve all saved notes from the database.
- Return them in JSON format.
- Use existing database session dependency.
- Add proper response typing.
- Include basic error handling.

Prompt Used (Frontend Update)
Update the frontend to:

1. Add a button labeled "Extract LLM" that calls POST /action-items/extract_llm.
2. Add a button labeled "List Notes" that calls GET /notes.
3. Display results dynamically without reloading the page.
4. Keep existing Extract button unchanged.
5. Keep UI simple and clean.

TODO

- Added new endpoint `POST /action-items/extract_llm`.
- Added new endpoint `GET /notes`.
- Integrated LLM extraction flow into the backend API layer.
- Updated frontend to include "Extract LLM" and "List Notes" buttons.
- Implemented dynamic result rendering using JavaScript fetch.
- Preserved existing heuristic extraction behavior and API contracts.
- Ensured compatibility with existing database and router structure.

Generated Code Snippets:
week2/app/main.py

- Updated application configuration and router integration.

week2/app/routers/action_items.py

- Added new endpoint for LLM-based extraction.

week2/app/routers/notes.py

- Added endpoint to retrieve all saved notes.

week2/app/services/extract.py

- Maintained integration of LLM extraction logic.

week2/frontend/index.html

- Added new UI buttons and JavaScript logic to call new endpoints.

week2/app/db.py

- Minor structural updates aligned with refactored backend.

week2/tests/test_extract.py

- Ensured compatibility with refactored backend structure.

### Exercise 5: Generate a README from the Codebase

Prompt:
Prompt Used (Initial Generation)
Analyze the entire week2 codebase and generate a comprehensive README.md file.
The README must include:

- Project overview
- Tech stack used
- Setup instructions (conda, poetry, uvicorn)
- API endpoints with descriptions
- Explanation of heuristic vs LLM extraction
- How to run tests
- Short explanation of agentic integration (frontend → backend → LLM)
- Folder structure overview

Keep it clean, structured, and professional.
Use markdown formatting.

Prompt Used (Refinement)
Refine and improve the existing README.md.
Keep all technical details the same.
Improve clarity, structure, and professionalism.
Make it more concise and academically polished.
Do not remove any required sections.

TODO

- Generated README.md using AI codebase introspection.
- Refined README for improved clarity and structure.
- Ensured all required assignment sections were included.
- Preserved technical accuracy while improving professionalism.

Generated Code Snippets:
README.md

- Fully generated and refined using Cursor AI.

## SUBMISSION INSTRUCTIONS

1. Hit a `Command (⌘) + F` (or `Ctrl + F`) to find any remaining `TODO`s in this file. If no results are found, congratulations – you've completed all required fields.
2. Make sure you have all changes pushed to your remote repository for grading.
3. Submit via Gradescope.
