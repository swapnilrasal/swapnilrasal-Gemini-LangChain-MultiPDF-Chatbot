#!/usr/bin/env python3
"""
Gemini-LangChain MultiPDF Chatbot - Python Setup and Run Script
Cross-platform Python script that automatically sets up the environment and runs the Streamlit app
"""

import os
import sys
import subprocess
import platform
import venv
from pathlib import Path

def run_command(command, shell=False):
    """Run a command and return success status."""
    try:
        result = subprocess.run(command, shell=shell, check=True, capture_output=True, text=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def create_virtual_environment():
    """Create virtual environment if it doesn't exist."""
    venv_path = Path("venv")
    if venv_path.exists():
        print("✅ Virtual environment already exists")
        return True
    
    print("📦 Creating virtual environment...")
    try:
        venv.create("venv", with_pip=True)
        print("✅ Virtual environment created")
        return True
    except Exception as e:
        print(f"❌ Failed to create virtual environment: {e}")
        return False

def get_python_executable():
    """Get the correct Python executable path for the virtual environment."""
    system = platform.system()
    if system == "Windows":
        return Path("venv/Scripts/python.exe")
    else:
        return Path("venv/bin/python")

def get_pip_executable():
    """Get the correct pip executable path for the virtual environment."""
    system = platform.system()
    if system == "Windows":
        return Path("venv/Scripts/pip.exe")
    else:
        return Path("venv/bin/pip")

def install_packages():
    """Install required packages."""
    pip_exe = get_pip_executable()
    
    print("⬆️ Upgrading pip...")
    success, _ = run_command([str(pip_exe), "install", "--upgrade", "pip"])
    if not success:
        print("⚠️ Failed to upgrade pip, continuing...")
    
    print("📚 Installing requirements...")
    
    # Try requirements.txt first
    if Path("requirements.txt").exists():
        print("📋 Installing from requirements.txt...")
        success, output = run_command([str(pip_exe), "install", "-r", "requirements.txt"])
        if not success:
            print("⚠️ Some packages from requirements.txt failed. Installing core dependencies...")
        else:
            print("✅ Requirements installed successfully")
            return True
    
    # Install core dependencies
    core_packages = [
        "streamlit",
        "langchain",
        "langchain-google-genai",
        "langchain-community",
        "langchain-text-splitters",
        "pypdf",
        "python-dotenv",
        "chromadb"
    ]
    
    print("📋 Installing core dependencies...")
    success, output = run_command([str(pip_exe), "install"] + core_packages)
    if success:
        print("✅ Core dependencies installed successfully")
        
        # Install optional performance enhancement
        print("🚀 Installing optional performance enhancement...")
        run_command([str(pip_exe), "install", "watchdog"])
        
        return True
    else:
        print(f"❌ Failed to install dependencies: {output}")
        return False

def check_env_file():
    """Check if .env file exists and is properly configured."""
    env_file = Path(".env")
    
    if not env_file.exists():
        print("⚠️ .env file not found. Creating template...")
        with open(".env", "w") as f:
            f.write("GOOGLE_API_KEY=your_actual_google_api_key_here\n")
        print("📝 Please edit .env file and add your Google API key from: https://makersuite.google.com/app/apikey")
        print("   Then run this script again.")
        return False
    
    # Check if API key is properly set
    with open(".env", "r") as f:
        content = f.read()
    
    if "your_actual_google_api_key_here" in content:
        print("⚠️ Please update your Google API key in the .env file")
        print("   Get your API key from: https://makersuite.google.com/app/apikey")
        print("   Then run this script again.")
        return False
    
    return True

def run_streamlit_app():
    """Run the Streamlit application."""
    system = platform.system()
    if system == "Windows":
        streamlit_exe = Path("venv/Scripts/streamlit.exe")
    else:
        streamlit_exe = Path("venv/bin/streamlit")
    
    print("")
    print("🎉 Setup complete! Starting the Streamlit app...")
    print("📱 The app will open in your browser at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the application")
    print("")
    
    try:
        subprocess.run([str(streamlit_exe), "run", "app.py"], check=True)
    except KeyboardInterrupt:
        print("\n🛑 Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to run Streamlit app: {e}")

def main():
    """Main function to set up and run the application."""
    print("🚀 Setting up Gemini-LangChain MultiPDF Chatbot...")
    print("==================================================")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} found")
    
    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)
    
    # Install packages
    if not install_packages():
        sys.exit(1)
    
    # Check environment configuration
    if not check_env_file():
        sys.exit(1)
    
    print("✅ Environment configuration complete")
    
    # Run the application
    run_streamlit_app()

if __name__ == "__main__":
    main()
