from __future__ import annotations

import os
import re
from typing import List
import json
from typing import Any
from ollama import chat
from dotenv import load_dotenv

load_dotenv()

BULLET_PREFIX_PATTERN = re.compile(r"^\s*([-*•]|\d+\.)\s+")
KEYWORD_PREFIXES = (
    "todo:",
    "action:",
    "next:",
)

def _is_action_line(line: str) -> bool:
    stripped = line.strip().lower()
    if not stripped:
        return False
    if BULLET_PREFIX_PATTERN.match(stripped):
        return True
    if any(stripped.startswith(prefix) for prefix in KEYWORD_PREFIXES):
        return True
    if "[ ]" in stripped or "[todo]" in stripped:
        return True
    return False


def extract_action_items(text: str) -> List[str]:
    lines = text.splitlines()
    extracted: List[str] = []
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue
        if _is_action_line(line):
            cleaned = BULLET_PREFIX_PATTERN.sub("", line)
            cleaned = cleaned.strip()
            # Trim common checkbox markers
            cleaned = cleaned.removeprefix("[ ]").strip()
            cleaned = cleaned.removeprefix("[todo]").strip()
            extracted.append(cleaned)
    # Fallback: if nothing matched, heuristically split into sentences and pick imperative-like ones
    if not extracted:
        sentences = re.split(r"(?<=[.!?])\s+", text.strip())
        for sentence in sentences:
            s = sentence.strip()
            if not s:
                continue
            if _looks_imperative(s):
                extracted.append(s)
    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: List[str] = []
    for item in extracted:
        lowered = item.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        unique.append(item)
    return unique


def _looks_imperative(sentence: str) -> bool:
    words = re.findall(r"[A-Za-z']+", sentence)
    if not words:
        return False
    first = words[0]
    # Crude heuristic: treat these as imperative starters
    imperative_starters = {
        "add",
        "create",
        "implement",
        "fix",
        "update",
        "write",
        "check",
        "verify",
        "refactor",
        "document",
        "design",
        "investigate",
    }
    return first.lower() in imperative_starters

def extract_action_items_llm(text: str) -> list[str]:
    """
    Extract actionable tasks from free-form text using an LLM.

    This function calls the Ollama `llama3.1:8b` model and instructs it to return
    only a JSON array of strings, where each string is a concise actionable task.
    The JSON is parsed safely and any error (LLM failure, bad JSON, wrong shape)
    results in an empty list being returned.
    """
    # Build a clear instruction so the model responds with *only* a JSON array.
    system_prompt = (
        "You extract actionable tasks from meeting notes or free-form text.\n"
        "Return ONLY a JSON array of strings, nothing else.\n"
        "Each string must be a concise, actionable task.\n"
        "Example output: [\"Follow up with the client\", \"Prepare the report\"]"
    )

    try:
        # Call the Ollama chat API with the llama3.1:8b model.
        response = chat(
            model="llama3.1:8b",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
        )

        # Extract the raw text content returned by the model.
        content = response.get("message", {}).get("content", "")
        if not isinstance(content, str) or not content.strip():
            return []

        content = content.strip()

        # Some models may wrap JSON in ```json ... ``` fences; strip those if present.
        if content.startswith("```"):
            # Remove the opening fence (with optional 'json') and the closing fence.
            content = re.sub(r"^```(?:json)?\s*", "", content)
            content = re.sub(r"\s*```$", "", content).strip()

        # Safely parse the JSON; if it fails or isn't the expected shape, return [].
        try:
            parsed = json.loads(content)
        except json.JSONDecodeError:
            return []

        # We expect a JSON array of strings; anything else is treated as failure.
        if not isinstance(parsed, list):
            return []

        tasks: list[str] = []
        for item in parsed:
            if isinstance(item, str):
                cleaned = item.strip()
                if cleaned:
                    tasks.append(cleaned)

        return tasks
    except Exception:
        # Any unexpected error (network issues, API errors, etc.) results in a safe fallback.
        return []
