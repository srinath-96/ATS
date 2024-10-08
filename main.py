import os
import sys

print("Current working directory:", os.getcwd())
print("Python version:", sys.version)
print("Python path:", sys.path)

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

print("Updated Python path:", sys.path)

import streamlit as st
from ui.app import run_app

if __name__ == "__main__":
    run_app()