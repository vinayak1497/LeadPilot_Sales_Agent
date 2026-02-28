"""
Vercel serverless function entry point for FastAPI application.
This file serves as the bridge between Vercel's serverless infrastructure
and the FastAPI application.
"""

import sys
from pathlib import Path

# Add the parent directory to Python path so imports work correctly
root_path = Path(__file__).parent.parent
sys.path.insert(0, str(root_path))

# Import the FastAPI app from ui_client
from ui_client.main import app

# Vercel expects the app to be available as 'app' or 'handler'
# FastAPI is ASGI compatible, which Vercel's Python runtime supports
