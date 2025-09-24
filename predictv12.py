from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train/weights/best.pt")  # <-- replace with your .pt path

# Run prediction on an image
results = model.predict(source="testPics/6.jpg", imgsz=640, conf=0.25, device="cpu")

# Show results
results[0].show()   # opens image with detections
