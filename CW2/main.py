from PIL import Image, ImageDraw

image = Image.new("RGB", (900, 800), "white")
draw = ImageDraw.Draw(image)


def set_pixel(x, y):
    draw.point((x, y), "black")


def dda():
    def draw_line(x1, y1, x2, y2):
        x = x1
        y = y1 + 0.5
        slope = (y2 - y1) / (x2 - x1)

        while x <= x2:
            set_pixel(x, int(y))
            y += slope
            x += 1

    def main():
        draw_line(10, 10, 100, 100)

        image.show()

    main()


def bresenham():
    def draw_line(x1, y1, x2, y2):
        x = float(x1)
        y = float(y1)
        dx = x2 - x1
        dy = y2 - y1

        def f(xx, yy):
            return dy * xx - dx * yy - (x1 * dy - y1 * dx)

        set_pixel(x, y)
        count = dx

        while count > 0:
            count -= 1
            if f(x + 1, y + 0.5) > 0:
                y += 1
            x += 1
            set_pixel(x, y)

    def main():
        draw_line(10, 80, 90, 11)

        image.show()

    main()


if __name__ == "__main__":
    bresenham()
