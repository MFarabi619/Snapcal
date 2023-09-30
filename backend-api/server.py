from flask import request
from flask import Flask
import base64
import os
import sys
from importlib import import_module
from PIL import Image
import io

path = os.path.abspath("../")
sys.path.append(path)
# todo: change to snake case for package names
from image_processing import process_image


app = Flask(__name__)

@app.route("/process-image", methods=['POST'])
def process_image_handler():
    body = request.json
    encoded = body['encoded_image']
    decoded = base64.b64decode(encoded.split(',')[1])
    
    # image = Image.open(io.BytesIO(decoded))


    event = process_image.process_image_array(decoded)

    return event
