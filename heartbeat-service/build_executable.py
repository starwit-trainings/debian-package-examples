#!/usr/bin/env python

import os
import subprocess
import shutil
from pathlib import Path

def build_executable():
    """Build an executable using PyInstaller"""
    print("Building executable with PyInstaller...")
    
    # Remove existing spec file to ensure we use the latest options
    if os.path.exists("heartbeat_service.spec"):
        os.remove("heartbeat_service.spec")
        
    # Build with options to properly bundle Python interpreter
    subprocess.run([
        "python", "-m", "PyInstaller",
        "--name=heartbeat_service",
        "--onefile",
        "--clean",
        "--add-binary=/usr/lib/python3.13/lib-dynload/*:lib-dynload",
        "--hidden-import=_decimal",
        "src/heartbeat_service/service.py"
    ], check=True)
    
    print("Executable built successfully!")
    print(f"Executable location: {os.path.abspath('dist/heartbeat_service')}")

if __name__ == "__main__":
    build_executable()