from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException

from .. import db
from ..services.extract import extract_action_items, extract_action_items_llm


router = APIRouter(prefix="/action-items", tags=["action-items"])


@router.post("/extract")
def extract(payload: Dict[str, Any]) -> Dict[str, Any]:
    text = str(payload.get("text", "")).strip()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    if payload.get("save_note"):
        note_id = db.insert_note(text)

    items = extract_action_items(text)
    ids = db.insert_action_items(items, note_id=note_id)
    return {"note_id": note_id, "items": [{"id": i, "text": t} for i, t in zip(ids, items)]}


@router.post("/extract_llm")
def extract_llm(payload: Dict[str, Any]) -> Dict[str, Any]:
    """
    Extract action items using the LLM-based extractor.

    This endpoint accepts the same request body as the heuristic /extract
    endpoint, but routes the text through extract_action_items_llm instead.
    The response shape is kept identical for contract consistency.
    """
    text = str(payload.get("text", "")).strip()
    if not text:
        # Keep error behaviour in line with the existing /extract endpoint.
        raise HTTPException(status_code=400, detail="text is required")

    note_id: Optional[int] = None
    if payload.get("save_note"):
        note_id = db.insert_note(text)

    # Use the LLM-powered extractor; it already has internal error handling and
    # guarantees a list return type.
    items = extract_action_items_llm(text)
    ids = db.insert_action_items(items, note_id=note_id)
    return {"note_id": note_id, "items": [{"id": i, "text": t} for i, t in zip(ids, items)]}


@router.get("")
def list_all(note_id: Optional[int] = None) -> List[Dict[str, Any]]:
    rows = db.list_action_items(note_id=note_id)
    return [
        {
            "id": r["id"],
            "note_id": r["note_id"],
            "text": r["text"],
            "done": bool(r["done"]),
            "created_at": r["created_at"],
        }
        for r in rows
    ]


@router.post("/{action_item_id}/done")
def mark_done(action_item_id: int, payload: Dict[str, Any]) -> Dict[str, Any]:
    done = bool(payload.get("done", True))
    db.mark_action_item_done(action_item_id, done)
    return {"id": action_item_id, "done": done}


