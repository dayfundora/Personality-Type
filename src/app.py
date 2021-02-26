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
    #global model
    #model = Model()
    #train_models()
    #train_models('tfidf')
    
    if request.method == 'POST':
        global textpredict
        textpredict = request.form['text']
        return predecir_texto()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
