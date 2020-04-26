# To draw overlays on Faces from supplied image
from PIL import Image, ImageDraw
import face_recognition

# Note:kriks.jpg file must exist in current direcotry for this to work
# Can be any image with a single person on any background
# Image quality must be good, or some more lines of code is required to make it
# look as expected
image = face_recognition.load_image_file("kriks.jpg")

face_landmarks_list = face_recognition.face_landmarks(image)

pil_image = Image.fromarray(image)

d = ImageDraw.Draw(pil_image, 'RGBA')

for face_landmarks in face_landmarks_list:
    d.line(face_landmarks["left_eyebrow"], fill=(128, 0, 128, 100), width=6)
    d.line(face_landmarks["right_eyebrow"], fill=(128, 0, 128, 100), width=6)

    # Draw over the lips
    d.line(face_landmarks["top_lip"], fill=(128, 0, 128, 100), width=4)
    d.line(face_landmarks["bottom_lip"], fill=(128, 0, 128, 100), width=4)

pil_image.show()
