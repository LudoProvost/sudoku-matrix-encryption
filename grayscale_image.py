import numpy as np
from PIL import Image


def show_encrypt(image_name, matrix, M, number_of_blocks):

    image = Image.open('images/' + image_name).convert('L').resize((number_of_blocks * (M ** 2), number_of_blocks * (M ** 2)))

    image_data = np.asarray(image)

    encrypted_img = Image.fromarray(encrypt(image_data, matrix, M)).convert('L')

    encrypted_img.save('encrypted/' + image_name.split(".")[0] + '_grayscale.png')

    encrypted_img.show()


def show_decrypt(image_name, matrix, M):
    image = Image.open('encrypted/' + image_name.split(".")[0] + '_grayscale.png')

    image_data = np.asarray(image)

    decrypted_img = Image.fromarray(decrypt(image_data, matrix, M)).convert('L')

    decrypted_img.save('decrypted/' + image_name.split(".")[0] + '_grayscale.png')

    decrypted_img.show()


def encrypt(image_data, rescaled_ref_matrix, M):
    # divide image into refmatrix-scale matrices

    block_size = M ** 2
    number_of_blocks = int(image_data.shape[0] / (M ** 2))
    img_block = np.empty((number_of_blocks, number_of_blocks, block_size, block_size))

    blocks = np.array(np.split(image_data, number_of_blocks, axis=1))

    for block_col in range(len(blocks)):
        temp = np.array(np.split(np.concatenate(blocks[block_col]), number_of_blocks, axis=0))  # 126x9

        for block_row in range(number_of_blocks):
            img_block[block_row][block_col] = temp[block_row].reshape((block_size, block_size))

    # encrypt pixels

    encrypted_img = np.empty(image_data.shape)
    img_block_encrypted = np.empty(img_block.shape)

    for row in range(number_of_blocks):
        for col in range(number_of_blocks):
            X = img_block[row][col]
            Y = rescaled_ref_matrix
            img_block_encrypted[row][col] = (X + Y) % 255

    for row in range(img_block.shape[0]):
        for col in range(img_block.shape[1]):
            for row_block in range(img_block.shape[2]):
                for col_block in range(img_block.shape[3]):
                    encrypted_img[(row * block_size) + row_block][(col * block_size) + col_block] = \
                    img_block_encrypted[row][col][row_block][col_block]

    return encrypted_img


def decrypt(image_data, rescaled_ref_matrix, M):
    # divide image into refmatrix-scale matrices

    block_size = M ** 2
    number_of_blocks = int(image_data.shape[0] / (M ** 2))
    img_block = np.empty((number_of_blocks, number_of_blocks, block_size, block_size))

    blocks = np.array(np.split(image_data, number_of_blocks, axis=1))

    for block_col in range(len(blocks)):
        temp = np.array(np.split(np.concatenate(blocks[block_col]), number_of_blocks, axis=0))  # 126x9

        for block_row in range(number_of_blocks):
            img_block[block_row][block_col] = temp[block_row].reshape((block_size, block_size))

    # encrypt pixels

    decrypted_img = np.empty(image_data.shape)
    img_block_decrypted = np.empty(img_block.shape)

    for row in range(number_of_blocks):
        for col in range(number_of_blocks):
            X = img_block[row][col]
            Y = rescaled_ref_matrix
            img_block_decrypted[row][col] = X - Y

    for row in range(img_block.shape[0]):
        for col in range(img_block.shape[1]):
            for row_block in range(img_block.shape[2]):
                for col_block in range(img_block.shape[3]):
                    px = img_block_decrypted[row][col][row_block][col_block]
                    if px < 0:
                        px += 255
                    decrypted_img[(row * block_size) + row_block][(col * block_size) + col_block] = px

    return decrypted_img