from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .config import APP_TITLE, FRONTEND_DIR, FRONTEND_INDEX
from .db import init_db
from .routers import action_items, notes

# Initialize database schema on startup so routes can rely on it.
init_db()

# Main FastAPI application instance with a clear, centralized title.
app = FastAPI(title=APP_TITLE)


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    """
    Serve the main frontend HTML page.

    This keeps the backend responsible for returning the static index while
    the frontend assets are served from the static mount below.
    """
    return FRONTEND_INDEX.read_text(encoding="utf-8")


app.include_router(notes.router)
app.include_router(action_items.router)

# Serve static frontend assets from the centralized frontend directory.
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")