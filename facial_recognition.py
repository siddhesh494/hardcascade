from PIL import Image
import face_recognition
image = face_recognition.load_image_file("image/obama1.jpeg")
 
face_location = face_recognition.face_locations(image)
print("I found {} face(s) in the photograph.".format(len(face_location)))

for face_location in face_location:

	#print the location of each face in the image
	top, right, bottom, left = face_location
	print("A face is location at pixel location Top: {}, left: {}, Bottom: {}, right{}".format(top, right, bottom, left))
	#you can access the actual face itself like this:
	face_image = image[top:bottom, left:right]
	pil_image = Image.fromarray(face_image)

	pil_image.show()
