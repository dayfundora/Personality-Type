from flask import Flask, render_template, request, url_for, redirect
from logic.Model import Model,train_models
from logic.Predict import Predictor
from logic.Scraper_Face import  FBScraper, ExecFace
from bson import json_util
import json
import yaml
import pickle

UPLOAD_FOLDER = 'static/img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)


@app.route("/", methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        global textpredict
        textpredict = request.form['text']
        return predict_text()
    return render_template('index.html')

def predict_text():
    if textpredict is not None:
        p = Predictor()
        global prediction
        prediction = p.predict([textpredict])
        return redirect(url_for('result'))
    else:
        return str("-----------No Text to Predict------------")


if __name__ == '__main__':
    app.run(debug=True)
