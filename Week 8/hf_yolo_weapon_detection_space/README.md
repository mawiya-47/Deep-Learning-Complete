---
title: YOLO Weapon Detection
emoji: 🛡️
colorFrom: blue
colorTo: red
sdk: gradio
sdk_version: 6.16.0
app_file: app.py
pinned: false
---

# YOLO Weapon Detection App

This Hugging Face Space uses a custom YOLO model trained with Ultralytics and a Roboflow dataset.

## Files Required

Upload these files to your Hugging Face Space:

1. `app.py`
2. `requirements.txt`
3. `best.pt`

## How to Get `best.pt`

After YOLO training in Colab, download your trained model from:

```text
runs/detect/weapon_detection_yolov8_roboflow/weights/best.pt
```

or:

```text
runs/detect/train/weights/best.pt
```

## Features

- Upload image
- Capture image from webcam
- Adjust confidence threshold
- Display bounding boxes
- Show detection summary

## Safety Note

This application is for educational and public-safety research only.  
AI detection systems can produce false positives and false negatives.  
Human verification is required before taking any real-world action.