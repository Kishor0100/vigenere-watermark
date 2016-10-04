from PIL import Image

def _process_image(img, key, encrypt_mode=True):
    px = img.load()
    list_text = ["1" if px[x,y] else "0" for x in range(img.width) for y in range(img.height)]    
    list_text_processed = [int("".join(list_text[i:i+8]), 2) for i in range(0, len(list_text), 8)]
    list_text_processed = encrypt(list_text_processed, key) if encrypt_mode else decrypt(list_text_processed, key)
    list_text_processed = "".join([bin(x).lstrip("0b").zfill(8) for x in list_text_processed])    
    
    processed = Image.new("1", img.size)
    px_processed = processed.load()    
    for x in range(img.width):
        for y in range(img.height):                        
            px_processed[x,y] = 255 if list_text_processed[x*img.width+y] == "1" else 0            
    return processed    

def encrypt_image(img, key):
    return _process_image(img, key, True)

def decrypt_image(img, key):
    return _process_image(img, key, False)    

def encrypt(plain_text, key):
    encrypt_text = []
    length_key = len(key)
    for i, x in enumerate(plain_text):
        encrypt_text.append((x + ord(key[i%length_key])) % 256)
    return encrypt_text

def decrypt(encrypt_text, key):
    decrypt_text = []
    length_key = len(key)
    for i, x in enumerate(encrypt_text):
        decrypt_text.append((x - ord(key[i%length_key])) % 256)
    return decrypt_text
