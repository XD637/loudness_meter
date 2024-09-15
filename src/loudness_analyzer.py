import pyloudnorm as pyln
import numpy as np
import librosa

def analyze_loudness(file_path):
    try:
        # Load audio file with librosa
        audio_data, sample_rate = librosa.load(file_path, sr=None, mono=True)

        if len(audio_data) == 0:
            print("Error: Audio file is empty.")
            return None, None

        # Calculate LUFS using pyln
        meter = pyln.Meter(sample_rate)  # Create a meter
        loudness_lufs = meter.integrated_loudness(audio_data)

        # Define loudness targets (in LUFS) for different platforms
        target_lufs = {
            'Spotify - Loud Mode': -11,
            'Spotify - Normal Mode (Preferred)': -14,
            'Spotify - Quiet Mode': -19,
            'Apple Music': -16,
            'YouTube Music': -14,
            'Amazon Music': -14
        }

        # Calculate penalties based on these targets
        penalties = {}
        for platform, target in target_lufs.items():
            if loudness_lufs > target:
                penalty = target - loudness_lufs  # Negative value for reduction
            else:
                penalty = 0  # No penalty for quieter tracks

            penalties[platform] = penalty

        return loudness_lufs, penalties
    except Exception as e:
        print(f"Error analyzing file: {e}")
        return None, None
