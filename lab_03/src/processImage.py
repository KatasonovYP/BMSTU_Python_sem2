from PIL import Image


MAX_LENGTH = 256
RADIX = 2


def encodeImage(image, message="I love Python!"):
    '''
    :param filename: name (path to) encoding image
    :param length: len of message (num of
    :param string: message
    :return:
    '''
    return_code = 0
    height, width = image.size  # define width and height
    pixels = image.load()  # load pixels values

    # message length must be less then size of image
    if len(message) > MAX_LENGTH:
        return_code = 1
    else:
        for i in range(1, len(message) + 1):

            letter_code = ord(message[i - 1])

            for offset in range(3):
                x = (i * 3 + offset) % width
                y = (i * 3 + offset) // width
                pixel = pixels[y, x]
                new_pixel = [0, 0, 0]

                for color in range(len(pixel)):
                    bit = letter_code % RADIX
                    letter_code //= RADIX
                    new_pixel[color] = pixel[color] // 2 * 2 + bit

                # we don't change last color of third pixel
                if offset == 2:
                    new_pixel[2] = pixel[2]

                # change pixel
                image.putpixel((y, x), tuple(new_pixel))

        # end of message
        image.putpixel((0, 0), (len(message), 0, 0))

    return {
        'image': image,
        'code': return_code
    }


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
        code = code[:-1][::-1]

        # change string
        message = message + chr(int(code, 2))

    return {
        'message': message,
        'code': return_code
    }


if __name__ == '__main__':
    image = Image.open('src/assets/2.bmp')
    print(encodeImage(image))
    print(decodeImage(image))
