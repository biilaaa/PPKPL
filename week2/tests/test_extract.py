import os
import pytest

from ..app.services.extract import extract_action_items
from ..app.services.extract import extract_action_items_llm
from ..app.services import extract as extract_module


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)
    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items

def _fake_chat_factory(response_content: str):
    """
    Create a fake `chat` function that always returns the given JSON
    string in the `message.content` field, simulating an Ollama response.
    """

    def _fake_chat(*args, **kwargs):
        return {"message": {"content": response_content}}

    return _fake_chat


def test_extract_action_items_llm_bullet_list(monkeypatch: pytest.MonkeyPatch):
    """LLM extractor should handle bullet list style input and return tasks as a list of strings."""
    note_text = "- Prepare the report\n- Email the client"
    # Simulate the LLM returning two clear tasks as a JSON array of strings.
    monkeypatch.setattr(
        extract_module,
        "chat",
        _fake_chat_factory('["Prepare the report", "Email the client"]'),
    )

    result = extract_action_items_llm(note_text)
    # The return type must always be a list.
    assert isinstance(result, list)
    # Avoid strict equality; just verify key phrases appear somewhere in the output.
    joined = " ".join(result)
    assert "Prepare the report" in joined
    assert "Email the client" in joined


def test_extract_action_items_llm_keyword_prefixed(monkeypatch: pytest.MonkeyPatch):
    """LLM extractor should work with keyword-prefixed lines like 'TODO:' or 'Action:'."""
    note_text = "TODO: write unit tests\nAction: update the documentation"
    monkeypatch.setattr(
        extract_module,
        "chat",
        _fake_chat_factory('["write unit tests", "update the documentation"]'),
    )

    result = extract_action_items_llm(note_text)
    assert isinstance(result, list)
    joined = " ".join(result)
    assert "write unit tests" in joined
    assert "update the documentation" in joined


def test_extract_action_items_llm_empty_input(monkeypatch: pytest.MonkeyPatch):
    """Empty input should still return a list, typically empty, from the LLM extractor."""
    note_text = ""
    monkeypatch.setattr(
        extract_module,
        "chat",
        _fake_chat_factory("[]"),
    )

    result = extract_action_items_llm(note_text)
    assert isinstance(result, list)
    # We expect no tasks for empty input, but we keep the assertion loose.
    assert len(result) == 0


def test_extract_action_items_llm_non_action_text(monkeypatch: pytest.MonkeyPatch):
    """Clearly non-action narrative text should reasonably result in no tasks from the LLM extractor."""
    note_text = "It was a sunny day and everyone felt relaxed."
    monkeypatch.setattr(
        extract_module,
        "chat",
        _fake_chat_factory("[]"),
    )

    result = extract_action_items_llm(note_text)
    assert isinstance(result, list)
    # Avoid strict expectations about exact content; just ensure there are no tasks.
    assert len(result) == 0