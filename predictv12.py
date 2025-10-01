from PIL import Image
import cv2
from ultralytics import YOLO

# Path to image
image_path = '/Users/christiansalz/Desktop/SPoHF-Yolov8/test-manual/images/22.jpg'
image = Image.open(image_path)

# Load trained model (YOLO v12)
model = YOLO('runs/detect/train4/weights/best.pt')

# Run inference
results = model.predict(image, conf=0.40, iou=0.20)

# Customize annotation look (line thickness + font size)
annotated_image = results[0].plot(
    labels=True,        # show labels
    line_width=1,       # thinner boxes (default is ~2-3)
    font_size=12        # increase font size (default ~8)
)

# Convert BGR → RGB for PIL
annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
annotated_image_pil = Image.fromarray(annotated_image_rgb)

# Show or save result
annotated_image_pil.show()
# annotated_image_pil.save("annotated.jpg")

# Count insects
detected_insects = results[0].boxes
num_insects = len(detected_insects)
print(f"Number of insects detected: {num_insects}")
