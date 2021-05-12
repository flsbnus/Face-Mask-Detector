#얼굴 랜드마크 추출

import face_recognition
from PIL import Image, ImageDraw

face_image_path='data/without_mask/100.jpg'
mask_image_path = 'data/mask.png'

face_image_np=face_recognition.load_image_file(face_image_path)
face_locations=face_recognition.face_locations(face_image_np)
face_landmarks=face_recognition.face_landmarks(face_image_np,face_locations)

face_landmarks_image=Image.fromarray(face_image_np)
draw=ImageDraw.Draw(face_landmarks_image)

#chin 1번 15번 7번 9번


print(face_landmarks)

for face_landmark in face_landmarks:
    print(face_landmark)
    for feature_name,points in face_landmark.items():
        print(feature_name,points)
        for point in points:
            draw.point(point)

chin_l_tx=face_landmark['chin'][1][0]
chin_l_ty=face_landmark['chin'][1][1]
chin_r_tx=face_landmark['chin'][15][0]
chin_r_ty=face_landmark['chin'][15][1]
chin_l_bx=face_landmark['chin'][7][0]
chin_l_by=face_landmark['chin'][7][1]
chin_r_bx=face_landmark['chin'][9][0]
chin_r_by=face_landmark['chin'][9][1]
chin_m_bx=face_landmark['chin'][8][0]
chin_m_by=face_landmark['chin'][8][1]
nose_t_ty=face_landmark['nose_bridge'][1][1]

#for face_location in face_locations:
mask_image = Image.open(mask_image_path)
mask_width = chin_r_tx-chin_l_tx
mask_height = chin_m_by-nose_t_ty
mask_image = mask_image.resize((mask_width, int(mask_height)))

face_landmarks_image.paste(mask_image, (chin_l_tx, nose_t_ty), mask_image)


face_landmarks_image.show()

