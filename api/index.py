"""Vercel serverless function entry point"""
import sys
import os

# Add flask directory to path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
flask_dir = os.path.join(project_root, 'flask')
sys.path.insert(0, flask_dir)
if project_root in sys.path:
	sys.path.remove(project_root)
if '' in sys.path:
	sys.path.remove('')

from app import app

# Export for Vercel
handler = app
