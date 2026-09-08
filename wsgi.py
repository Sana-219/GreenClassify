"""WSGI entry point for Vercel deployment"""
import os
import sys

# Add flask directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flask'))

from app import app

if __name__ == "__main__":
    app.run()
