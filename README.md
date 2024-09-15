"""
# Loudness Meter Application

## Table of Contents
- Project Description
- Features
- Technologies Used
- Requirements
- Installation
- How to Use
- Loudness Targets
- LUFS Explained
- Known Issues
- Contributing
- License

## Project Description

The **Loudness Meter** application is a desktop utility designed for audio professionals and enthusiasts to analyze the loudness levels of their audio files. It computes the LUFS (Loudness Units Full Scale) of an audio track using the **ITU-R BS.1770-4** standard. The app also provides real-time analysis and displays penalty adjustments required for various popular streaming platforms like Spotify, YouTube, and Apple Music.

## Features
- **LUFS Calculation**: Calculates the integrated loudness of an audio track in LUFS.
- **Platform Penalties**: Displays required dB adjustment penalties for popular streaming platforms based on their target loudness standards.
- **Multi-format Support**: Supports audio formats such as WAV, MP3, and FLAC.
- **Drag and Drop Interface**: Easily drag and drop audio files for quick analysis.
- **Export Results**: Export the loudness analysis and penalties into a text file for future reference.
- **Real-Time UI Updates**: Live updates within the application as the analysis runs.

## Technologies Used
- Python 3.10+
- PyQt5 for building the user interface.
- librosa for audio file handling and loading.
- pyloudnorm for calculating loudness (LUFS).
- NumPy for efficient numerical computations.
- SciPy for signal processing.
- FFmpeg for backend audio decoding (required for MP3 support).

## Requirements
- Python 3.10 or higher
- The following Python libraries (install via `pip`):
  - PyQt5
  - pyloudnorm
  - librosa
  - numpy
  - scipy
  - ffmpeg-python

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/loudness-meter.git
cd loudness-meter
2. Set Up a Virtual Environment
bash
Copy code
python -m venv loudness_meter_env
source loudness_meter_env/bin/activate  # On Windows: loudness_meter_env\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Install FFmpeg
Follow this guide to install FFmpeg.

5. Run the Application
bash
Copy code
python src/main.py
How to Use
Upload an Audio File: Upload an audio file by clicking the Upload Audio button or dragging and dropping your file into the designated area.

Analyze Audio: The app will analyze the loudness of the track and display the LUFS value and penalties for different streaming platforms.

View Penalties: Penalties (dB adjustments) for platforms like Spotify, YouTube, Apple Music, and Amazon Music will be shown in the results panel.

Export Results: Click on the Export Results button to save the analysis as a text file.

Loudness Targets
Here are the default loudness targets:

Platform	Target LUFS
Spotify (Loud Mode)	-11 LUFS
Spotify (Normal Mode)	-14 LUFS
Spotify (Quiet Mode)	-19 LUFS
Apple Music	-16 LUFS
YouTube Music	-14 LUFS
Amazon Music	-14 LUFS
LUFS Explained
LUFS (Loudness Units Full Scale) is a standard loudness unit used in audio normalization to ensure consistent loudness across tracks. The meter calculates:

Integrated LUFS: Overall loudness of the track.
Penalties: Adjustments in dB required to meet a platform's target LUFS.
Known Issues
Some audio formats may not be supported by default.
Large audio files may affect performance.
Contributing
Fork the repository.
Create a new branch: git checkout -b feature/YourFeature.
Commit your changes: git commit -m 'Add feature'.
Push to the branch: git push origin feature/YourFeature.
Open a pull request.
License