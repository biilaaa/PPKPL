from __future__ import annotations

"""
Pydantic request and response schemas used by the API.

These models define the public HTTP contract for the backend and help keep
the routers small, explicit, and well-typed.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    """Payload for creating a new note."""

    content: str = Field(..., description="Raw note content from which to extract action items.")


class NoteResponse(BaseModel):
    """Representation of a stored note."""

    id: int
    content: str
    created_at: str


class ActionItemsExtractRequest(BaseModel):
    """Payload for extracting action items from free-form text."""

    text: str = Field(..., description="Source text containing potential action items.")
    save_note: bool = Field(
        False,
        description="If true, the original text is saved as a note before extraction.",
    )


class ExtractedActionItem(BaseModel):
    """A single extracted action item returned from the extract endpoint."""

    id: int
    text: str


class ActionItemsExtractResponse(BaseModel):
    """Response returned by the /action-items/extract endpoint."""

    note_id: Optional[int]
    items: List[ExtractedActionItem]


class ActionItemListItem(BaseModel):
    """Representation of an action item stored in the database."""

    id: int
    note_id: Optional[int]
    text: str
    done: bool
    created_at: str


class ActionItemDoneUpdate(BaseModel):
    """Payload to mark an action item as done/undone."""

    done: bool = Field(
        True,
        description="Whether the action item should be marked as completed.",
    )


class ActionItemDoneResponse(BaseModel):
    """Response model confirming the done state of an action item."""

    id: int
    done: bool

