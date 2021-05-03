#얼굴 랜드마크 추출

import face_recognition
from PIL import Image, ImageDraw

face_image_path='data/without_mask/110.jpg'

face_image_np=face_recognition.load_image_file(face_image_path)
face_locations=face_recognition.face_locations(face_image_np)
face_landmarks=face_recognition.face_landmarks(face_image_np,face_locations)

face_landmarks_image=Image.fromarray(face_image_np)
draw=ImageDraw.Draw(face_landmarks_image)

print(face_landmarks)

for face_landmark in face_landmarks:
    print(face_landmark)
    for feature_name,points in face_landmark.items():
        print(feature_name,points)
        for point in points:
            draw.point(point)

lb=face_landmark['chin'][2]
rb=face_landmark['chin'][15]


face_landmarks_image.show()

