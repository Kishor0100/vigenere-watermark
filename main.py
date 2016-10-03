import random
import string
import watermark

def main():
    len_key = 10
    key = "".join([random.choice(string.ascii_letters) for _ in range(len_key)])
    watermark.insert("sample/lenna.png", "sample/watermark.bmp", key, "out/watermark_insert.png")
    watermark.extract("out/watermark_insert.png", key, "out/watermark_extract.bmp")

if __name__ == '__main__':
    main()