from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/train4/weights/best.pt")  # <-- replace with your .pt path

# Run prediction on an image
results = model.predict(source="/Users/christiansalz/Desktop/SPoHF-Yolov8/test-manual/images/22.jpg", imgsz=640, conf=0.25, device="cpu")

# Show results
results[0].show()  # opens image with detections
