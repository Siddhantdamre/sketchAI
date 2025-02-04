from diffusers import StableDiffusionPipeline
import torch

def generate_face_sketch(description_text):
    try:
        # Load the Stable Diffusion model from Hugging Face
        pipeline = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipeline.to("cuda" if torch.cuda.is_available() else "cpu")

        # Generate the sketch based on the descriptive text
        image = pipeline(description_text).images[0]

        # Display the generated image
        image.show()

        # Save the image and return the path
        image_path = "generated_face_sketch.png"
        image.save(image_path)
        return image_path
    except Exception as e:
        print(f"An error occurred during sketch generation: {e}")
        return None
