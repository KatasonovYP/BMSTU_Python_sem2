import PIL.Image

from src.constants import RADIX


def decodeImage(image: PIL.Image):
    '''
    function for decode message from image (pillow)
    '''
    message = ''
    return_code = 0

    _, width = image.size
    pixels = image.load()
    length = image.getpixel((0, 0))[0]
    for i in range(1, length + 1):
        code = ''

        for offset in range(3):
            # * 3 для перемещения сразу по трем пикселям
            y = (i * 3 + offset) // width
            # + offset для тех 3 пикселей внутри
            x = (i * 3 + offset) % width
            pixel = pixels[y, x]

            for color in range(len(pixel)):
                # достаем младшие биты цвета каждого пикселя
                bit = str(pixel[color] % RADIX)
                # обновление двоичного кода символа
                code += bit

        # избавимся от 9 бита и перевернем строку
        code = code[:-1][::-1]

        # переведем в 10 систему счисления
        code = int(code, 2)

        # обновим строку
        message += chr(code)

    return {
        'message': message,
        'code': return_code
    }
