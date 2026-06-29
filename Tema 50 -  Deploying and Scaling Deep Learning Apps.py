from flask import Flask, request, jsonify, render_template_string
import numpy as np
from PIL import Image

# pornire aplicatie flask
app = Flask(__name__)

# model dummy pentru simulare
class DummyModel:

    def predict(self, x):
        return np.array([[0.85,0.15]])

model = DummyModel()

# clase animale
classes = ["mainecoon_cat", "other_cat"]

# pagina HTML integrata
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>AI Detectie Pisica Maine Coon</title>
</head>

<body style="font-family:Arial; text-align:center; padding-top:40px;">

<h2>AI Detectie Pisica Maine Coon</h2>

<form action="/predict" method="post" enctype="multipart/form-data">

<input type="file" name="file" required>

<br><br>

<button type="submit">Detecteaza Pisica</button>

</form>

</body>
</html>
"""

# pagina principala
@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

# endpoint predictie
@app.route("/predict", methods=["POST"])
def predict():

    if "file" not in request.files:
        return "Nu ai incarcat imagine"

    file = request.files["file"]

    image = Image.open(file)

    image = image.resize((224,224))

    image_array = np.array(image)/255.0
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)

    index = np.argmax(prediction)

    result = classes[index]

    return f"<h2>Rezultat detectie: {result}</h2><br><a href='/'>Inapoi</a>"

# rulare server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
