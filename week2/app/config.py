from __future__ import annotations

"""
Central application configuration.

This module centralizes common paths and constants so they can be reused
across the API, database layer, and other services without duplication.
"""

from pathlib import Path

# Base directory of the week2 project.
BASE_DIR: Path = Path(__file__).resolve().parents[1]

# Data directory and SQLite database path.
DATA_DIR: Path = BASE_DIR / "data"
DB_PATH: Path = DATA_DIR / "app.db"

# Frontend directory and main index file.
FRONTEND_DIR: Path = BASE_DIR / "frontend"
FRONTEND_INDEX: Path = FRONTEND_DIR / "index.html"

# General application metadata.
APP_TITLE: str = "Action Item Extractor"

