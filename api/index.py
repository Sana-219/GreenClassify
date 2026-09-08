"""Vercel serverless function entry point"""
import sys
import os

# Add flask directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'flask'))

from app import app

# Export for Vercel
handler = app
