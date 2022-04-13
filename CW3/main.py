from random import randint

from PIL import Image

image = Image.open("monkey.jpg")


def fixed_thresholding():
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            sr = (r + g + b) // 3

            if sr > 127:
                image.putpixel((x, y), (255, 255, 255))
            else:
                image.putpixel((x, y), (0, 0, 0))

    image.show()


def random_thresholding():
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            sr = (r + g + b) // 3

            if sr > randint(0, 255):
                image.putpixel((x, y), (255, 255, 255))
            else:
                image.putpixel((x, y), (0, 0, 0))

    image.show()


def patterning():
    m2x2 = [
        [0, 2],
        [3, 1]
    ]

    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            sr = (r + g + b) // 3

            if sr * 5 // 256 > m2x2[y % 2][x % 2]:
                image.putpixel((x, y), (255, 255, 255))
            else:
                image.putpixel((x, y), (0, 0, 0))

    image.show()


def error_diffusion():
    for x in range(image.width):
        for y in range(image.height):
            r, g, b = image.getpixel((x, y))
            sr = (r + g + b) // 3
            new_pixel = tuple([i + i * 7 // 48 for i in image.getpixel((x+1, y))])
            image.putpixel(image.getpixel((x+1, y)), new_pixel)



def main():
    # fixed_thresholding()
    # random_thresholding()
    patterning()
    # error_diffusion()


if __name__ == "__main__":
    main()
