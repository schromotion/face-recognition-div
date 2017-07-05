from PIL import Image, ImageDraw
import face_recognition
# Image Landmark Source https://github.com/schromotion/face_recognition/blob/master/face_recognition/api.py
# Face landmarks definition https://cdn-images-1.medium.com/max/1600/1*AbEg31EgkbXSQehuNJBlWg.png

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    #Is this line necessary
    #for face_landmarks in face_landmarks_list:
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image, 'RGBA')

    # Change color
    # Make width 75% of distance between lip and nose.
    # Move line up 50% of the width in pixel diraction
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)

    pil_image.show()
