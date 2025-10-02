# gpa-alok-server-
from flask import Flask, request
import face_recognition

app = Flask(__name__)

@app.route('/')
def home():
    return "Drone Cloud Server is Running!"

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image)
    return {"faces_detected": len(face_locations)}

if __name__ == '__main__':
    app.run()
