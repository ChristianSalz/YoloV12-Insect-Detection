from diffusers import DiffusionPipeline, EulerDiscreteScheduler
import torch
import os

# Set device
device = "mps" if torch.backends.mps.is_available() else "cpu"

# Load model
pipe = DiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    use_safetensors=True
).to(device)

pipe.scheduler = EulerDiscreteScheduler.from_config(pipe.scheduler.config)

prompt = "decayed apple"

# Folder to save images
output_folder = "generatedPictures"
os.makedirs(output_folder, exist_ok=True)  # create folder if it doesn't exist

# Generate 50 images
for i in range(1, 2):
    image = pipe(prompt).images[0]
    filename = os.path.join(output_folder, f"batchI{i}.png")  # use relative path
    image.save(filename)
    print(f"Saved {filename}")