from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

#pip install pillow
#pip install pandas
#pip install os

df = pd.read_csv('IntenDetails.csv') #Read from .csv file
fontName = ImageFont.truetype('fonts/MLSJN.ttf',70) #Font style and size
fontDomain = ImageFont.truetype('fonts/Lato-Black.ttf',45)
fontDuration = ImageFont.truetype('font/arial.ttf',26)
fontIssueDate1 = ImageFont.truetype('fonts/Lato-Black.ttf',28)
fontIssueDate2 = ImageFont.truetype('fonts/Lato-Black.ttf',45)

for index,j in df.iterrows():
    img = Image.open('Internship-Certificate.jpg') #Open the .jpg file
    draw = ImageDraw.Draw(img)

    #Issue Date
    id = j['IssueDate(dd-mmm-yyyy)'].split('-')
    line1 = id[1]+" "+id[2]
    if len(id[0])==1:
        line2 = "0"+id[0]
    else:
        line2 = id[0]
    draw.text(xy=(97,90),text='{}'.format(line1),fill=(0,0,0),font=fontIssueDate1)
    draw.text(xy=(131,140),text='{}'.format(line2),fill=(0,0,0),font=fontIssueDate2)

    #Name
    name = j['Name'].split()
    jaxis=370
    for x in name:
        draw.text(xy=(95,jaxis),text='{}'.format(x),fill=(0,0,0),font=fontName)
        jaxis+=80

    tag = ' '.join([str(s) for s in name])

    #Domain
    draw.text(xy=(640,410),text='{}'.format(j['Domain']),fill=(0,0,0),font=fontDomain)

    #Duration with start and end dates
    dd = j['StartDate'] + " to " + j['EndDate']  #double date
    draw.text(xy=(784,557),text='{}'.format(dd),fill=(0,0,0),font=fontDuration)


    img.save('Generated-Certificates/{}.jpg'.format(tag))
