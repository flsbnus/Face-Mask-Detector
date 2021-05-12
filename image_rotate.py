#이미지 회전

from PIL import Image

mask_image_path = 'data/mask.png'
mask_image=Image.open(mask_image_path)

mask_image_rotate=mask_image.rotate(100,expand=True)
mask_image_rotate.show()