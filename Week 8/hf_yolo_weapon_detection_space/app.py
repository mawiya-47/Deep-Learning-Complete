import gradio as gr
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

# -------------------------------
# Load YOLO Model
# -------------------------------
# Put your trained model file "best.pt" in the same Hugging Face Space folder.
MODEL_PATH = "best.pt"

if not os.path.exists(MODEL_PATH):
    model = None
else:
    model = YOLO(MODEL_PATH)


def detect_image(image, confidence):
    """
    This function accepts an uploaded image or webcam-captured image,
    runs YOLO detection, and returns the image with bounding boxes.
    """
    if model is None:
        return None, "Model file best.pt not found. Please upload best.pt to your Hugging Face Space."

    if image is None:
        return None, "Please upload or capture an image first."

    # Convert PIL image to RGB
    image = image.convert("RGB")

    # Run YOLO prediction
    results = model.predict(
        source=image,
        conf=confidence,
        save=False
    )

    # Draw boxes on image
    annotated_image = results[0].plot()

    # Ultralytics returns numpy image. Convert it to PIL image.
    annotated_image = Image.fromarray(annotated_image)

    # Prepare detection summary
    names = model.names
    detected = []

    if results[0].boxes is not None:
        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            detected.append(f"{names[cls_id]}: {conf:.2f}")

    if len(detected) == 0:
        summary = "No object detected."
    else:
        summary = "Detected objects:\n" + "\n".join(detected)

    return annotated_image, summary


# -------------------------------
# Gradio Interface
# -------------------------------
with gr.Blocks(title="YOLO Weapon Detection") as demo:
    gr.Markdown(
        """
        # AI-Based Weapon Detection using YOLO

        Upload an image or capture an image from webcam, then run YOLO detection.

        **Important:** This app is for educational and public-safety research only.  
        The model may produce false positives or false negatives. Human verification is required.
        """
    )

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(
                label="Upload Image or Capture from Webcam",
                sources=["upload", "webcam"],
                type="pil"
            )

            confidence = gr.Slider(
                minimum=0.05,
                maximum=0.95,
                value=0.40,
                step=0.05,
                label="Confidence Threshold"
            )

            detect_button = gr.Button("Run YOLO Detection")

        with gr.Column():
            output_image = gr.Image(label="YOLO Detection Output")
            output_text = gr.Textbox(label="Detection Summary", lines=8)

    detect_button.click(
        fn=detect_image,
        inputs=[input_image, confidence],
        outputs=[output_image, output_text]
    )

if __name__ == "__main__":
    demo.launch()