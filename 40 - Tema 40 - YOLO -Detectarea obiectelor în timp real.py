from ultralytics import YOLO
import cv2
from flask import Flask, Response


# incarcare model YOLO

model = YOLO("yolov8n.pt")


# creare aplicatie flask

app = Flask(__name__)


# pornire camera (0 = webcam laptop)

camera = cv2.VideoCapture(0)


# functie detectie

def gen_frames():

    while True:

        success, frame = camera.read()

        if not success:
            break

        rezultate = model(frame)

        frame = rezultate[0].plot()

        # salvare imagine daca sunt obiecte detectate

        if len(rezultate[0].boxes) > 0:

            cv2.imwrite("detectie.jpg", frame)

        ret, buffer = cv2.imencode('.jpg', frame)

        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# ruta streaming

@app.route('/')

def video():

    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# rulare aplicatie

if __name__ == "__main__":

    app.run(debug=True)

