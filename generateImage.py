import torch
from diffusers import DiffusionPipeline

device = "mps" if torch.backends.mps.is_available() else "cpu"

pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    dtype=torch.float16,
    use_safetensors=True,
    variant="fp16"
).to(device)

prompt = "Apple on a table"
image = pipe(prompt=prompt).images[0]
#image = pipe(prompt, height=512, width=512).images[0]
image.save("apple3.png")