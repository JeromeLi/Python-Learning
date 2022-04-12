from turtle import width
from PIL import Image
import os
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
os.chdir('/Users/jerome/Git/learn_python/Automatic the boring stuff with python/Chapter_17/Images')
catIm = Image.open('zophie.png')
# catIm.size
# width, height = catIm.size
# catIm.filename
# catIm.format
# catIm.format_description
# catIm.save('zophie.jpg')
# im = Image.new('RGBA', (300, 400), 'white')
# im.save('white.png')
# im = Image.new('RGBA', (300, 400), 'purple')
# im.save('purple.png')
# im = Image.new('RGBA', (300, 400))
# im.save('transparent.png')
croppedIm = catIm.crop((335, 235, 565, 365))
croppedIm.save('zophie_cropped_01.png')
logging.debug('End of program')
