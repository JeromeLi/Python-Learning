import logging
import os
import logging
from PIL import Image

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

os.chdir('/Users/jerome/Git/learn_python/Automatic the boring stuff with python/Chapter_17/Images')
catIm_ori = Image.open('zophie.png')
catIm = Image.new('RGBA', (catIm_ori.size), 'black')
faceIm = Image.open('zophie_cropped.png')
catIm_width, catIm_height = catIm.size
faceIm_width, faceIm_height = faceIm.size
catCopy = catIm.copy()

for left in range(0, catIm_width, faceIm_width+10):
    for top in range(0, catIm_height, faceIm_height+10):
        print(left, top)
        catCopy.paste(faceIm, (left, top))

catCopy.save('zophie_face_titled.png')

logging.debug('End of program')

