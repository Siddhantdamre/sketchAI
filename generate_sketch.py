import whisper
import speech_recognition as sr
from spellchecker import SpellChecker
from transformers import StableDiffusionPipeline
import torch

# Function to capture and transcribe speech
def capture_and_transcribe_speech():
    recognizer = sr.Recognizer()
    model = whisper.load_model("base")

    with sr.Microphone() as source:
        print("Please describe the person...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        with open("temp_audio.wav", "wb") as f:
            f.write(audio_data.get_wav_data())

    print("Recognizing speech...")
    result = model.transcribe("temp_audio.wav")
    description_text = result["text"]
    print(f"Captured Description: {description_text}")
    return description_text

# Function to correct spelling errors in the transcribed text
def correct_spelling(text):
    spell = SpellChecker()
    words = text.split()
    corrected_text = " ".join([spell.correction(word) for word in words])
    return corrected_text

# Function to generate the sketch based on the description
def generate_face_sketch(description_text):
    try:
        # Load the Stable Diffusion model
        pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

        # Generate the image from the description
        image = pipeline(description_text).images[0]

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
    description_text = capture_and_transcribe_speech()
    description_text = correct_spelling(description_text)
    image_path = generate_face_sketch(description_text)
    if image_path:
        print(f"Sketch generated and saved at: {image_path}")
    else:
        print("Failed to generate the sketch.")

if __name__ == "__main__":
    main()
