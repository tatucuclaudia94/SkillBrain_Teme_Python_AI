from ultralytics import YOLO
import cv2
from flask import Flask


# incarcare model YOLO

model = YOLO("yolov8n.pt")


# creare aplicatie flask

app = Flask(__name__)


# ruta principala

@app.route("/")

def detectie():

    img = cv2.imread("test.jpg")

    rezultate = model(img)

    rezultate[0].show()

    return "Detectie obiecte YOLO finalizata"


# rulare aplicatie

if __name__ == "__main__":

    app.run(debug=True)

