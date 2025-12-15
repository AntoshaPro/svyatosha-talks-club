#!/usr/bin/env python3
"""
Script to run the SvyaTosha: Quantum Empire Builder application
"""

import os
import subprocess
import sys

def main():
    print("🚀 Starting SvyaTosha: Quantum Empire Builder...")
    print("Make sure you have set your GOOGLE_API_KEY in the .env file")
    print("")
    
    # Check if streamlit is installed
    try:
        import streamlit
    except ImportError:
        print("📦 Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    print("✨ Launching the Quantum Empire Builder dashboard...")
    print("🌐 Application will be available at: http://localhost:8501")
    print("💡 Tip: Use Ctrl+C to stop the application")
    print("")
    
    # Run the streamlit app
    subprocess.run([
        "streamlit", "run", 
        "src/main.py",
        "--server.address", "0.0.0.0",
        "--server.port", "8501"
    ])

if __name__ == "__main__":
    main()