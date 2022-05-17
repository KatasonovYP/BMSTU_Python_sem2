import PIL.Image

from src.constants import MAX_LENGTH, RADIX


def encodeImage(image: PIL.Image, message: str = "I love Python!") -> dict:
    '''
    function for encode message in image (pillow)
    '''
    return_code = 0
    height, width = image.size
    pixels = image.load()

    if len(message) > MAX_LENGTH:
        return_code = 1
    else:
        # начинаем с единицы, так как в нулевой пиксель кодируется размер строки
        for i in range(1, len(message) + 1):

            # -1 так как сообщение нужно читать сначала
            letter_code = ord(message[i - 1])
            # Так как у нас 8 бит, то нужно 3 пикселя по 3 цвета для кодирования
            for offset in range(3):
                # * 3 для перемещения сразу по трем пикселям
                # + offset для тех 3 пикселей внутри
                x = (i * 3 + offset) % width
                y = (i * 3 + offset) // width
                pixel = pixels[y, x]
                new_pixel = [0, 0, 0]

                for color in range(len(pixel)):
                    # постепенный перевод слова в двоичную систему счисления
                    bit = letter_code % RADIX
                    letter_code //= RADIX
                    # обнуление младшего бита
                    new_pixel[color] = pixel[color] // 2 * 2
                    # Закодируем бит в младший бит цвета пикселя
                    new_pixel[color] += bit

                # change pixel
                image.putpixel((y, x), tuple(new_pixel))

        # end of message
        image.putpixel((0, 0), (len(message), 0, 0))

    return {
        'image': image,
        'code': return_code
    }
