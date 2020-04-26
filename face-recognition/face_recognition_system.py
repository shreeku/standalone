# To compare multiple images and figure out if it matches with any of the
# given person images list
import face_recognition

image1 = face_recognition.load_image_file("person_1.jpg")
image2 = face_recognition.load_image_file("person_2.jpg")
image3 = face_recognition.load_image_file("person_3.jpg")

person_1 = face_recognition.face_encodings(image1)[0]
person_2 = face_recognition.face_encodings(image2)[0]
person_3 = face_recognition.face_encodings(image3)[0]

known_face_encodings = [
    person_1,
    person_2,
    person_3
]

unknown_image = face_recognition.load_image_file("unknown_8.jpg")

unknown_face_encodings = face_recognition.face_encodings(unknown_image)

for unknown_face_encoding in unknown_face_encodings:
    results = face_recognition.compare_faces(known_face_encodings,
                                             unknown_face_encoding)
    name = "Unknown"
    if results[0]:
        name = "Person 1"
    elif results[1]:
        name = "Person 2"
    elif results[2]:
        name = "Person 3"

    print("Found {} in the photo!".format(name))
