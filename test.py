from pydub import AudioSegment

# Explicitly set paths to ffmpeg and ffprobe
AudioSegment.ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
AudioSegment.ffprobe = r"C:\ffmpeg\bin\ffprobe.exe"

# Test playback functionality
try:
    from pydub.playback import play
    silent_audio = AudioSegment.silent(duration=1000)  # 1 second of silence
    play(silent_audio)
    print("Audio playback test successful.")
except Exception as e:
    print(f"Audio playback test failed: {e}")
