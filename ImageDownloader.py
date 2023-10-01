from PIL import Image, ImageFilter, ImageDraw, ImageFont
import requests
from io import BytesIO


category = input("Please enter the type of image you'd like to download:")

API_KEY = "39777761-2d75f5997c7d066799342fd4c"


req_params = {
    'key': API_KEY,
    'q': category,
    'lang': 'en',
    'image_type': 'photo',
    'category': 'animals',
    'per_page': 3
}

response = requests.get('https://pixabay.com/api/', params=req_params, stream=True)


if response.status_code == 200:
    data = response.json()
    img_url = data['hits'][0]['largeImageURL']
    print(img_url)
    img_resp = requests.get(img_url, stream=True).raw
    img = Image.open(img_resp)
    img.save('New image.jpg', 'jpeg')
    img.show()

else:
    print(f'Error - {response.status_code}')

