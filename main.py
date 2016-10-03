import random
import string
from PIL import Image

import watermark
import util

sample_image = "sample/lenna.png"
watermark_image = "sample/watermark.bmp"
watermark_insert = "out/watermark_insert.png"
watermark_extract = "out/watermark_extract.bmp"

def test_watermark():
    len_key = 10
    key = "".join([random.choice(string.ascii_letters) for _ in range(len_key)])
    watermark.insert(sample_image, watermark_image, key, watermark_insert)
    watermark.extract(watermark_insert, key, watermark_extract)
    print("Original:", sample_image)
    print("Watermark:", watermark_image)
    print("Saved as:", watermark_insert)
    print("Extracted:", watermark_extract)

def test_psnr():
    img_b = Image.open(sample_image)
    img_a = Image.open(watermark_insert)
    print("PSNR:", util.psnr(img_a, img_b), "dB")

def main():
    test_watermark()
    test_psnr()

if __name__ == '__main__':
    main()