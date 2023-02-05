import numpy as np
from PIL import Image

import color_image
import grayscale_image
import ref_matrix

np.set_printoptions(precision=1, linewidth=100, threshold=81)

M = 3
x_0 = 0.4
r = 3.8
encrypting = False
image_name = "peppers.jpg"

matrix = ref_matrix.get_matrix(x_0, r, M)

image = Image.open('images/' + image_name)

number_of_blocks = int((image.height - (image.height % (M ** 2))) / (M ** 2))

if image.mode == "RGB":
    if encrypting:
        color_image.show_encrypt(image_name, matrix, M, number_of_blocks)
    else:
        color_image.show_decrypt(image_name, matrix, M)
else:
    if encrypting:
        grayscale_image.show_encrypt(image_name, matrix, M, number_of_blocks)
    else:
        grayscale_image.show_decrypt(image_name, matrix, M)
