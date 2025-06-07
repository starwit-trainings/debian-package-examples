#!/usr/bin/env python

import os
import subprocess
import shutil
from pathlib import Path

def build_executable():
    """Build an executable using PyInstaller"""
    print("Building executable with PyInstaller...")
    
    # Create spec file if it doesn't exist
    if not os.path.exists("heartbeat_service.spec"):
        subprocess.run([
            "python", "-m", "PyInstaller",
            "--name=heartbeat_service",
            "--onefile",
            "--clean",
            "src/heartbeat_service/service.py"
        ], check=True)
    else:
        # Build using existing spec file
        subprocess.run([
            "python", "-m", "PyInstaller",
            "heartbeat_service.spec"
        ], check=True)
    
    print("Executable built successfully!")
    print(f"Executable location: {os.path.abspath('dist/heartbeat_service')}")

if __name__ == "__main__":
    build_executable()