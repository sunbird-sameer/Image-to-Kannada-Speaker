# pip install gTTS
# pip install easyocr

from gtts import gTTS
import os
import easyocr

language = 'kn'

reader = easyocr.Reader([language])

image = input("Enter The Image Name: ")

output = reader.readtext(image, detail=0)
print(output)


def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele

    return str1

s = output
print(listToString(s))
output = listToString(s)


myobj = gTTS(text=output, lang=language, slow=False)

myobj.save(image + ".mp3")
os.system(image + ".mp3")
