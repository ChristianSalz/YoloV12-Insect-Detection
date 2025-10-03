from ultralytics import YOLO
import torch
import os

# Check if MPS is available
# device = 'mps' if torch.backends.mps.is_available() else 'cpu'
# print(f"Training auf Gerät: {device}")

# Define model and dataset paths
model_path = "yolo12m.pt"  # Path to your model configuration
data_path = 'data.yaml'  # Path to your dataset YAML file

# Load the YOLO model
model = YOLO(model_path)

# Train the model
# workers= to the amount of CPU cores of your machine, you can aso experiment with the batch=X parameter
results = model.train(data=data_path, epochs=125, imgsz=640, workers=8)  # Train the model
