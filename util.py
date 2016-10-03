import math
from PIL import Image

def psnr(img_a, img_b):
    if img_a.size != img_b.size:
        return None

    return 20 * math.log(256 / math.sqrt(mse(img_a, img_b)), 10)

def mse(img_a, img_b):
    img_int_a = img_int(img_a)
    img_int_b = img_int(img_b)
    tmp = sum((sum(a)-sum(b))**2 for a, b in zip(img_int_a, img_int_b))
    return tmp / img_a.width / img_a.height

def img_int(img):
    px = img.load()
    for x in range(img.width):
        for y in range(img.height):
            yield px[x,y]
