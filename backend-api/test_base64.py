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


with open('./base64_test_image.txt', 'r') as file:
    # Read the entire contents of the file into a string
    file_contents = file.read()



decoded = base64.b64decode(file_contents.split(',')[1])


print (file_contents)

image = Image.open(io.BytesIO(decoded))


event = process_image.process_image_array(decoded)
print(event)