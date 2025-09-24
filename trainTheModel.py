from ultralytics import YOLO
import torch
import os
torch.set_num_threads(os.cpu_count())

# Check if MPS is available
# device = 'mps' if torch.backends.mps.is_available() else 'cpu'
# print(f"Training auf Gerät: {device}")

# Define model and dataset paths
model_path = "yolo12n.pt"  # Path to your model configuration
data_path = 'data.yaml'  # Path to your dataset YAML file

# Load the YOLO model
model = YOLO(model_path)

# Train the model
results = model.train(data=data_path, epochs=100, imgsz=320)  # Train the model

#pip install ultralytics
#pip install torch torchvision torchaudio