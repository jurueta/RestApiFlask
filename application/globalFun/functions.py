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

def pagination(page=None, cuantity_total=0):
    pagination = int(os.getenv("PAGINATION"))
    if page and page.isdigit() and int(page) > 0 :
        page = int(page)
        
        page_initial = pagination * (page-1)

        page_cuantity = cuantity_total / pagination
        
        next_page = page + 1 if page < page_cuantity and page > 0 else None

        previus_page = page - 1 if page > 1 and page < page_cuantity else None
        
        return page_initial, pagination, next_page, previus_page
    else:
        return 0, pagination, (None if cuantity_total < pagination else 2), None