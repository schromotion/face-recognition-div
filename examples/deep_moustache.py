from PIL import Image, ImageDraw
import face_recognition
import math
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
noseTip = face_landmarks_list[0]['nose_tip']

#Convert from Tuple to List so we can alter
topLipList = [list(elm) for elm in topLip]
noseTipList = [list(elm) for elm in noseTip]
#print(topLipList)

#Make Line the width of the lip
#Points from https://github.com/ageitgey/face_recognition/blob/85a643dae52fb99b116a1bc2fe8b274b0c95ac32/face_recognition/api.py & https://cdn-images-1.medium.com/max/1600/1*AbEg31EgkbXSQehuNJBlWg.png
topLipWidth = list()
topLipWidth.append(topLipList[0])
topLipWidth.append(topLipList[6])
print(topLipWidth)
print(topLipWidth[0][0])
print(topLipWidth[1][0])

#Make Line between nose tip and middle of lip
noseLipDist = list()
noseLipDist.append(noseTipList[2])
noseLipDist.append(topLipList[3])

#Make Line the Height of the lip
topLipHeight = list()
topLipHeight.append(topLipList[3])
topLipHeight.append(topLipList[10])
#print(topLipHeight)

lipWidthVal = math.sqrt((((topLipWidth[1][0])-(topLipWidth[0][0]))**(2))+(((topLipWidth[1][1])-(topLipWidth[0][1]))**(2)))
noseLipDistVal = math.sqrt((((noseLipDist[1][0])-(noseLipDist[0][0]))**(2)+(((noseLipDist[1][1])-(noseLipDist[0][1]))**(2))))
lipSlope = ((topLipWidth[1][1])-(topLipWidth[0][1]))/((topLipWidth[1][0])-(topLipWidth[0][0]))
recipLipSlope = (-1)*(1/lipSlope)

stacheWidth = topLipWidth
stacheWidth = stacheWidth * int(round(noseLipDistVal * recipLipSlope))

topLipWidth1 = [tuple(elm) for elm in topLipWidth]
topLipHeight1 = [tuple(elm) for elm in topLipHeight]
topLip1 = [tuple(elm) for elm in topLipList]
stacheWidth1 = [tuple(elm) for elm in stacheWidth]

#print(topLip)
#d.line(topLipWidth1, fill=(150,150,150,150), width=3)
#d.line(topLipHeight1, fill=(150,150,150,150), width=3)
d.line(stacheWidth1, fill=(255,255,255,255), width=8)

pil_image.show()
