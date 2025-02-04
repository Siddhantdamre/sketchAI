import whisper
import torch
from textblob import TextBlob
from diffusers import StableDiffusionPipeline
import sounddevice as sd
import numpy as np
import warnings
from scipy.io.wavfile import write  # For saving audio data as a .wav file
warnings.simplefilter('ignore', FutureWarning)


# Function to capture and transcribe speech using Whisper
def capture_and_transcribe_speech():
    model = whisper.load_model("base")  # Use a larger model for better accuracy

    print("Please describe the person...")

    # Record audio using sounddevice
    duration = 15  # seconds
    samplerate = 16000  # Whisper's required sampling rate
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    print("Recording completed")

    # Save the audio data to a .wav file
    audio_file = "temp_audio.wav"
    write(audio_file, samplerate, audio_data)  # Save audio as .wav

    # Transcribe the audio using Whisper
    print("Transcribing audio...")
    result = model.transcribe(audio_file)
    description_text = result["text"]
    print(f"Captured Description: {description_text}")
    return description_text

# Function to correct spelling errors in the transcribed text
def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()  # Automatically corrects spelling
    return str(corrected_text)

# Function to generate the face sketch based on the description
def generate_face_sketch(description_text):
    try:
        # Load the Stable Diffusion model
        pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipe.to("cuda" if torch.cuda.is_available() else "cpu")

        # Generate the image from the description
        image = pipe(description_text).images[0]

        # Display and save the image
        image.show()
        image_path = "generated_face_sketch.png"
        image.save(image_path)
        return image_path
    except Exception as e:
        print(f"An error occurred during sketch generation: {e}")
        return None

# Main workflow
def main():
    description_text = capture_and_transcribe_speech()  # Step 1: Capture speech and transcribe it
    description_text = correct_spelling(description_text)  # Step 2: Correct spelling
    image_path = generate_face_sketch(description_text)  # Step 3: Generate the face sketch
    if image_path:
        print(f"Sketch generated and saved at: {image_path}")
    else:
        print("Failed to generate the sketch.")

if __name__ == "__main__":
    main()
