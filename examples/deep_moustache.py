from PIL import Image, ImageDraw
import face_recognition
# Image Landmark Source https://github.com/schromotion/face_recognition/blob/master/face_recognition/api.py
# Face landmarks definition https://cdn-images-1.medium.com/max/1600/1*AbEg31EgkbXSQehuNJBlWg.png

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image, 'RGBA')

    # Change color
    # Make width 75% of distance between lip and nose.
    # Move line up 50% of the width in pixel diraction
topLip = face_landmarks_list[0]['top_lip']
print(topLip)
print(topLip[0])
print(topLip[0][0])

topLipList = [list(elm) for elm in topLip]

for point in topLipList:
    point[1] = point[1]+50

topLip1 = [tuple(elm) for elm in topLipList]

#print(topLip)
d.line(topLip1, fill=(150, 0, 0, 64), width=8)

pil_image.show()
