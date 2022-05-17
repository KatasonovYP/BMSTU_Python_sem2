from PIL import Image

from src.constants import RADIX


def decodeImage(image):
    message = ''
    return_code = 0

    height, width = image.size  # define width and height
    pixels = image.load()  # load pixels values
    length = image.getpixel((0, 0))[0]  # we encoded length to first component
    for i in range(1, length + 1):
        code = ''

        for offset in range(3):
            y = (i * 3 + offset) // width
            x = (i * 3 + offset) % width
            pixel = pixels[y, x]

            for color in range(len(pixel)):
                code += str(pixel[color] % RADIX)

        # we don't use last color of pixel
        code = reversed(code[:-1])

        # change string
        message = message + chr(int(code, 2))

    return {
        'message': message,
        'code': return_code
    }