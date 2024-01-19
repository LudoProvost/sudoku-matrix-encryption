# Encryption / decryption algorithm using the Sudoku matrix
Lossless image encryption and decryption algorithms. This project could not have been accomplished without the **amazing** paper by Yue Wu et al.[^1] cited in the reference section below.

## More about the algorithm
### Block diagram of the proposed image encryption schema[^1]
![blockdiagram](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/79c7c72a-fba3-4473-be87-c72311c42ace)

### Flow chart of the Sudoku reference matrix generator[^1]
![flowchart](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/60132132-e2ab-4b08-886e-dbdbb7ec9f20)

## Examples of encryption and decryption of images
| Original image | Encryption | Decryption |
|----------------|------------|------------|
|![cameraman](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/5031eb5c-dcc0-477f-9b46-79539480d8f1)|![cameraman_encrypt](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/fda01066-b95b-40aa-b169-0a5147911a46)|![cameraman_decrypt](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/bd4ab255-d72b-492e-997b-5969547be46f)|
|![peppers](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/c4a7eb73-3439-43c1-a40b-7b425dd5f33e)
|![peppers_encrypt](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/6dc8dd5a-2d7d-41a4-9243-0c9f0ad41012)
|![peppers_decrypt](https://github.com/LudoProvost/sudoku-matrix-encryption/assets/70982826/6f142444-95d7-45e3-ade5-ef07dfd63ac3)|

## How to use
1. In the same direct as main.py, create 3 folders and name them as follows: *images*, *decrypted*, and *encrypted*.
   - *images* : This is the folder where you put the images you want to encrypt or decrypt.
   - *decrypted* : This is the folder in which decrypted images will be saved to after running the decryption algorithm.
   - *encrypted* : This is the folder in which encrypted images will be saved to after running the encryption algorithm.
2. In main.py, change the image_name variable on line 14 to the file name of the image you want to decrypt/encrypt. This image should be in the *images* folder.
3. In main.py, change the encrypting variable on line 13 to *False* for decryption or to *True* for encryption
4. (OPTIONAL) the x_0 and r variables on lines 11 and 12 are used by the algorithm to determine the initial value of the logistic map, which means that an image can not be decrypted successfully if those variables are not the same values as the values used to encrypt the image.

For more information on the algorithm and its capabilities, please refer to the paper in the reference below.

## Reference
[^1]: [Image Encryption using the Sudoku Matrix by Yue Wu et al.](https://viplab.cis.um.edu.mo/publications/conference/Image%20Encryption%20using%20the%20Sudoku%20Matrix.pdf)
