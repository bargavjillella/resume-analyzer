import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def download_spacy_model():
    """Download spaCy English model"""
    try:
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    except subprocess.CalledProcessError:
        print("Failed to download spaCy model. Please run manually: python -m spacy download en_core_web_sm")

def run_streamlit():
    """Run the Streamlit application"""
    subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])

if __name__ == "__main__":
    print("Setting up AI Resume Analyzer...")
    
    # Install requirements
    print("Installing requirements...")
    install_requirements()
    
    # Download spaCy model
    print("Downloading spaCy model...")
    download_spacy_model()
    
    # Run application
    print("Starting application...")
    run_streamlit()