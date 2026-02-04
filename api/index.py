import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from crop import app

# Vercel auto-detects FastAPI from 'app' variable