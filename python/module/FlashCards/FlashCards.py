from PIL import ImageFont, ImageDraw, Image
import os
import cv2
import module.DB.DB_conn as c
conn=c.DBConn.conn


def MakeEngImage(width, height, english, fileName):
    
    img = Image.new("RGBA", (width, height), "black")

    fontpath = ".\module\FlashCards\CookieRun_Bold.ttf"
    font = ImageFont.truetype(fontpath, 60)

    draw = ImageDraw.Draw(img)

    engX, engY = draw.textsize(english, font = font)
    orgEngX = int(width/2 - engX/2) 
    orgEngY = int(height/2 - engY/2)
    draw.text((orgEngX, orgEngY), english, font = font, fill="white")

    img.save(fileName, "PNG")


def MakeWordImage(width, height, english, korean, fileName):

    img = Image.new("RGBA", (width, height), "black")

    fontpath = ".\module\FlashCards\CookieRun_Bold.ttf"
    font = ImageFont.truetype(fontpath, 60)

    draw = ImageDraw.Draw(img)

    engX, engY = draw.textsize(english, font = font)
    
    orgEngX = int(width/2 - engX/2)
    orgEngY = int(height/3 - engY/2)
    
    draw.text((orgEngX, orgEngY), english, font = font, fill = "white")

    korXsize, korYsize = draw.textsize(korean, font = font)
    
    orgKorX = int(width/2 - korXsize/2)
    orgKorY = int(height*(2/3) - korYsize/2)

    draw.text((orgKorX, orgKorY), korean, font = font, fill = "white")

    img.save(fileName, "PNG")
    

def flashcard(word,definition):
    MakeWordImage(400, 300, word, definition, '.\module\FlashCards\images\{}.png'.format(word+"definition"))
    MakeEngImage(400, 300, word, '.\module\FlashCards\images\{}.png'.format(word+""))






