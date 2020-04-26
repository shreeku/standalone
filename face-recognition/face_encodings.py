# To encode the image
import face_recognition

image = face_recognition.load_image_file("kriks.jpg")

face_encodings = face_recognition.face_encodings(image)

if len(face_encodings) == 0:
    print("No faces were found.")
else:
    first_face_encoding = face_encodings[0]
    print(first_face_encoding)
