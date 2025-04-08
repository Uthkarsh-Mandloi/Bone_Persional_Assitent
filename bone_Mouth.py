#this Part contain The voice of Bone

#This comented fart is for basic speech function with fixed voice in it
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    # Configure voice properties
    engine.setProperty('rate', 190)  # Speed: 180 words/minute
    engine.setProperty('volume', 1.0)  # Volume: 0.0 to 1.0
    
    # Get available voices (uncomment to list)
    # voices = engine.getProperty('voices')
    # print("Available voices:", [v.id for v in voices])
    
    # Select voice (modify index as needed)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Typically [0]=male, [1]=female
    
    engine.say(text)
    engine.runAndWait()

# # Test the function
# if __name__ == "__main__":
#     speak("Hello Uthkarsh! I am Bone, your AI assistant.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This part contain google clour api for customme voices after free credits it may cost real money per character

# from google.cloud import texttospeech_v1beta1 as tts
# import os

# #this part contain modules for directly speak out
# from io import BytesIO
# from pydub import AudioSegment
# from pydub.playback import play

# from pydub import AudioSegment

# # Explicitly set paths to ffmpeg and ffprobe
# AudioSegment.ffmpeg = r"C:\FFmpeg\bin\ffmpeg.exe"
# AudioSegment.ffprobe = r"C:\FFmpeg\bin\ffprobe.exe"

# # Set up Google Cloud credentials
# credential_path = r"D:\New_AI\bone-resources-69dd4f762b89.json"
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credential_path

# # Function to synthesize and play speech
# def speak(text, voice_type="standard"):
#     client = tts.TextToSpeechClient()

#     # Configure voice type
#     voice_configs = {
#         "standard": tts.VoiceSelectionParams(
#             language_code="en-US",
#             name="en-US-Standard-B"
#         ),
#         "wavenet": tts.VoiceSelectionParams(
#             language_code="en-US",
#             name="en-US-Wavenet-D"
#         )
#     }
#     voice = voice_configs.get(voice_type, voice_configs["standard"])

#     # Configure audio output
#     audio_config = tts.AudioConfig(
#         audio_encoding=tts.AudioEncoding.MP3  # MP3 format for playback
#     )

#     # Synthesize speech
#     synthesis_input = tts.SynthesisInput(text=text)
#     response = client.synthesize_speech(
#         input=synthesis_input,
#         voice=voice,
#         audio_config=audio_config
#     )

#     # Play the audio directly without saving
#     audio_data = BytesIO(response.audio_content)
#     audio_segment = AudioSegment.from_file(audio_data, format="mp3")
#     play(audio_segment)

# # Example usage
# if __name__ == "__main__":
#     text = "Hello Uthkarsh! This is Bone speaking directly without saving the audio."
#     speak(text, voice_type="standard")  # Change to "wavenet" if needed


