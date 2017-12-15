import face_recognition
import cv2
from simplecrypt import encrypt, decrypt
import os
from os.path import exists
from os import unlink
import sys
import random
import datetime
from termcolor import colored, cprint

now = datetime.datetime.now()
dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

camera_port = 0
ramp_frames = 30
camera = cv2.VideoCapture(camera_port)
def get_image():
    retval, im = camera.read()
    return im
for i in range(ramp_frames):
    temp = get_image()
cprint('Scanning for face...', 'blue')
camera_capture = get_image()
file = "images/face.jpg"
cv2.imwrite(file, camera_capture)
del(camera)

password_image = face_recognition.load_image_file("password.jpg")
face_image = face_recognition.load_image_file("images/face.jpg")

password_face_encoding = face_recognition.face_encodings(password_image)[0]
encodings = face_recognition.face_encodings(face_image)

if len(encodings) > 0:
	face_face_encoding = encodings[0]
else:
    cprint("Wasn't able to find a face. Please restart and try again.", 'red')
    os.remove('images/face.jpg')
    quit()

known_faces = [
    password_face_encoding
]

results = face_recognition.compare_faces(known_faces, face_face_encoding)

if(results[0]):
    cprint('Correct face detected.', 'green')
    requestpass = input('What password do you need? ')
    with open('accounts.txt', 'rb') as input:
        ciphertext = input.read()
        plaintext = decrypt('P24KYeMzkXNRr3gV', ciphertext)
        plaintext2 = (plaintext.decode('utf8'))
        if requestpass in (plaintext2):
            accountname = "passwords/" + requestpass + ".txt"
            with open(accountname, 'rb') as input:
                ciphertext2 = input.read()
                plaintext3 = decrypt('P24KYeMzkXNRr3gV', ciphertext2)
                plaintext4 = (plaintext3.decode('utf8'))
                print ("Here you go: " + plaintext4)
                os.remove('images/face.jpg')

        else:
        	cprint('Invalid Account Name. Please restart the program and try again', 'red')

else:
    cprint('Incorrect face detected. Please restart the program and try again', 'red')
    newname = 'images/' + dateandtime + '.jpg'
    os.rename('images/face.jpg', newname)
