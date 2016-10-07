import random
import string
from PIL import Image

import watermark
import util

def main():
    while(1):
        pilihan = int(menu())
        if pilihan == 0:
            print("Terimakasih sudah menggunakan aplikasi kami :)")
            break
        elif pilihan == 1:
            key = input("Masukan kata kunci: ")
            cover_image = input("Masukan path ke cover image (contoh: input/cover.bmp): ")
            watermark_image = input("Masukan path ke watermark image (contoh: input/watermark.bmp): ")
            watermark_embedded = input("Masukan nama file keluaran (contoh: out/out.bmp): ")
            watermark.insert(cover_image, watermark_image, key, watermark_embedded)
            print("")
        elif pilihan == 2:
            key = input("Masukan kata kunci: ")
            watermark_embedded = input("Masukan path ke gambar stegano (contoh: input/stegano.bmp): ")
            watermark_image = input("Masukan nama file keluaran (contoh: out/watermark.bmp): ")
            watermark.extract(watermark_embedded, key, watermark_image)
            print("")
        elif pilihan == 3:
            file_a = input("Masukan path ke file gambar 1 (contoh: input/stegano.bmp): ")
            file_b = input("Masukan path ke file gambar 2 (contoh: input/cover.bmp): ")
            img_b = Image.open(file_b)
            img_a = Image.open(file_a)
            print("PSNR:", util.psnr(img_a, img_b), "dB")
            print("")
        else:
            print("Command salah")
            print("")

if __name__ == '__main__':
    main()
