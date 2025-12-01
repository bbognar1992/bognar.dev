from pathlib import Path
import sys

# Add parent directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent))

from app import handler

# Export the handler for Vercel
__all__ = ["handler"]

