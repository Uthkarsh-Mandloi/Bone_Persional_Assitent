#This File contain speech intake function just like our Ears its only task is to intake the voice convert to text and return to requested files
import speech_recognition as sr

#Function for taking voice and returning text
def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        
        try:
            text = r.recognize_google(audio)
            return text.lower()
        except sr.UnknownValueError:
            return "Could not understand audio"
        except sr.RequestError as e:
            return f"API error: {str(e)}"

# Test the function
# while __name__ == "__main__":
#     print("Speak now:")
#     result = voice_to_text()
#     print(f"You said: {result}")
