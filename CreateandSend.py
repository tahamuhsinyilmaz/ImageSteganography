from stegano import lsb
import dropbox
import base64
import pandas as pd

dbx = dropbox.Dropbox("H7ykPa2RREAAAAAAAAABCm501mchU3ywlKYArQ1k6eAmPvRN7nTmJKrW7eerCzLM")
image = "test.PNG"



def uploadImage():
    with open(image, "rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        print(str)
    dbx.files_upload(str, "/image.txt")


def downloadImage():
    j = "image.txt"
    metadata, f = dbx.files_download('/' + j)
    out = open(j, 'wb')
    out.write(f.content)
    out.close()

def hideMessage(message):
    secret= lsb.hide(image, message)
    secret.save(image)

def readMessage():
    clear_message = lsb.reveal(image)
    print("Görüntü içerisinde saklı olan mesaj: " +clear_message)

def textToImage():
    data = open("image.txt", "r").read()
    decoded = base64.b64decode(data)
    fh = open("imageToSave.png", "wb")
    fh.write(decoded)
    fh.close()


with open('test.txt', 'r',encoding='utf-8') as file:
    data = file.read()
    hideMessage(data)
readMessage()