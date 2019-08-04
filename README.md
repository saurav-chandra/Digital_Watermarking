# Digital_Watermarking

This code implements spatial domain digital watermarking using the Python Imaging Library(PIL) module.

Takes an image as input named as "input.jpg", and produce output as "output.bmp".
(Make sure to keep input.jpg file in the same folder as the code, it should be more than atleast 1000x1000 pixels)
This new image is encrypted image containing the string entered by the user.

## Working

1. Computes the dimension of the input image.
2. Takes the input as string and convert each word into ascii value substracted by 255 (because 255 is the maximum value a pixel can hold).
3. Creates new row and column to work on.
4. Combines the R+G value and store in R, similarly combines R+B value and store in B of that pixel.
5. Changes the pixel RGB value of the row and column selected by repacing with R+G as R, 255-ascii value as G and R+B as B.
6. Repeat process 3-5 for the length of string, replacing that no. of pixels from the image.
7. For decrypting, reverse the process by converting ascii to real value and so on.

~~~~~~~~~~~~~~~~~~~~~~~~~~
Saurav Chandra
NIT Allahabad (MNNIT)
