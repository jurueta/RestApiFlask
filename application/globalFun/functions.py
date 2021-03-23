import base64
import io
from PIL import Image
from flask import current_app

def Base64ToFile(args):
    file_image = f"/img/imgphotouser{args['identification']}.png"
    image_stream = io.BytesIO(base64.b64decode(args["image"]))
    image = Image.open(image_stream)
    file_format = image.format
    if file_format in ("JPEG", "PNG"):
        image.save(f"{current_app.config['ROOT_FOLDER']}{file_image}", file_format)
        args["image"] = file_image
    else:
        return {'error': 'This file is not image'}, 400