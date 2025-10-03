from flask import Flask, request
import cv2
import cvlib as cv
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Drone Cloud Server is Running!"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    faces, confidences = cv.detect_face(img)
    return {"faces_detected": len(faces)}

if __name__ == '__main__':
    app.run()
