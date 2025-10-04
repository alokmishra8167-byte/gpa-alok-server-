from flask import Flask, request
import cvlib as cv
import numpy as np
import cv2
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Drone Cloud Server is Running!"

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return {"error": "No image uploaded"}, 400

    file = request.files['image']
    img_array = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    if img is None:
        return {"error": "Invalid image format"}, 400

    faces, _ = cv.detect_face(img)
    return {"faces_detected": len(faces)}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
