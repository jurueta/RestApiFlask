import base64
import io
import os
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

def pagination(page=None):
    pagination = os.getenv("PAGINATION")
    if page:
        page_initial = int(pagination) * (int(page)-1)
        print(f"pagination {page}")
        return {'page_initial': page_initial, 'page_final': pagination}
    else:
        return {'page_initial': 0, 'page_final': pagination}