import base64
import io
import os
import math
import re
from PIL import Image
from flask import current_app

def base64_to_file(args):
    file_image = f"/img/imgphotouser{args['identification']}.png"
    image_stream = io.BytesIO(base64.b64decode(args["image"]))
    image = Image.open(image_stream)
    file_format = image.format
    if file_format in ("JPEG", "PNG"):
        image.save(f"{current_app.config['ROOT_FOLDER']}{file_image}", file_format)
        args["image"] = file_image
    else:
        return {'error': 'This file is not image'}, 400

def pagination(page = None, cuantity_total = 0, url = ''):
    pagination = int(os.getenv("PAGINATION"))
    if page and page.isdigit() and int(page) > 0 :
        page = int(page)
        page_initial = pagination * (page-1)
        page_cuantity = math.ceil(cuantity_total / pagination)
        next_page = page + 1 if page < page_cuantity and page > 0 else None
        previus_page = page - 1 if page > 1 and page <= page_cuantity else None
    else:
        page_initial = 0
        next_page = (None if cuantity_total < pagination else 2)
        previus_page = None

    next_page = {'next' :f"{url}?page={next_page}"} if next_page else {}
    previus_page = {'previus' :f"{url}?page={previus_page}"} if previus_page else {}

    return page_initial, pagination, next_page, previus_page

def format_url_image(data, url):
    for i in data:
        i['image'] = f"{url[0:-1]}{i['image']}" if i['image'] else None
    return data

def validatestr(value):
    regex = re.compile('^[a-zA-Z0-9 ]*$')
    
    if value and bool(regex.match(value)):
        return value
    else:
        raise ValueError("string is empty")