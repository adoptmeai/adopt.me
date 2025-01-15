import torch
from diffusers import StableDiffusionPipeline
import os
import random

class DogGenerator:
    def __init__(self, model_path="CompVis/stable-diffusion-v1-4"):
        """Initializes the Stable Diffusion model for generating dog images."""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.pipeline = StableDiffusionPipeline.from_pretrained(model_path).to(self.device)

    def generate_dog_image(self, prompt, output_path="generated_dogs"):
        """
        Generates a dog image based on the provided prompt.

        Args:
            prompt (str): The text prompt describing the dog.
            output_path (str): Directory to save the generated image.

        Returns:
            str: Path to the generated image file.
        """
        os.makedirs(output_path, exist_ok=True)

        # Generate a unique filename
        image_name = f"dog_{random.randint(1000, 9999)}.png"
        image_path = os.path.join(output_path, image_name)

        print(f"Generating image with prompt: {prompt}")
        image = self.pipeline(prompt).images[0]

        image.save(image_path)
        print(f"Image saved to {image_path}")

        return image_path

if __name__ == "__main__":
    # Example usage
    generator = DogGenerator()
    prompt = "A friendly golden retriever sitting in a sunny park"
    generator.generate_dog_image(prompt)
