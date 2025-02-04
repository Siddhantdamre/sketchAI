import speech_recognition as sr

def capture_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Please describe the person or scene...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source)  # Listen to the microphone

    # Debugging: Check if audio_data is empty
    print(f"Captured audio: {audio_data}")
    
    try:
        print("Recognizing with Sphinx...")
        text = recognizer.recognize_sphinx(audio_data)  # Offline speech recognition
        print(f"Transcription: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the speech. Please try again.")
        return None
    except sr.RequestError as e:
        print(f"Sorry, there was an error with the speech recognition service: {e}")
        return None
