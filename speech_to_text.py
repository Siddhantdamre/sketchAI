import speech_recognition as sr

def capture_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please describe the person or scene...")
        audio_data = recognizer.listen(source)
        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio_data)
            print(f"Transcription: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")

    return ""
