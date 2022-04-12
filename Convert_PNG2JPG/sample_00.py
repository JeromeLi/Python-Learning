# import cv2
# import logging
# import os,glob,re
import os
from PIL import Image

# logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# logging.debug('Start of program')

def convert_image(source_path, dest_path):
    pngim = Image.open(source_path)
    jpgim = pngim.convert('RGB')
    jpgim.save(dest_path, format="JPEG", quality=50)
    print(f'Would convert {source_path} -> {dest_path}')

pwd = os.getcwd()
source_dir = os.path.join(pwd, '')
dest_dir = os.path.join(pwd, 'jpg')
for dirpath, dirnames, filenames in os.walk(source_dir):
    for filename in filenames:
        if filename.endswith('.png'):
            source_path = os.path.join(dirpath, filename)
            dest_path = os.path.join(dest_dir, os.path.relpath(dirpath, source_dir), filename.replace('.png', '.jpg'))
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            convert_image(source_path, dest_path)

# logging.debug('End of program')