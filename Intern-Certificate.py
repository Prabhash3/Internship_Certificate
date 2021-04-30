from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

#pip install pillow
#pip install pandas
#pip install os

df = pd.read_csv('IntenDetails.csv') #Read from .csv file
font = ImageFont.truetype('fonts/MLSJN.ttf',70) #Font style and size

for index,j in df.iterrows():
    img = Image.open('Internship-Certificate.jpg') #Open the .jpg file
    draw = ImageDraw.Draw(img)

    name = j['Name'].split()
    j=370
    for x in name:
        draw.text(xy=(95,j),text='{}'.format(x),fill=(0,0,0),font=font) #for name of length <=10
        j+=80

    tag = ' '.join([str(s) for s in name])
    img.save('Generated-Certificates/{}.jpg'.format(tag))