import math

from PIL import Image
from PIL import ImageDraw


def draw_angle(draw: ImageDraw, angle: float):
    fi = (-angle) * math.pi / 180
    len = 200
    pos_x, pos_y = 100, 500

    draw.line((pos_x, pos_y, pos_x + len, pos_y), "white")
    draw.line((pos_x, pos_y, pos_x + math.cos(fi)*len, pos_y + math.sin(fi)*len), "white")


def main():
    image = Image.new("RGB", (900, 800), "black")

    draw = ImageDraw.Draw(image)
    draw_angle(draw, 90)

    image.show()


if __name__ == "__main__":
    main()
