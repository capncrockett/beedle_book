# grayscale_converter.py
#   Program converts a picture to grayscale.
from graphics import *


def open_image(pic_file):
    """Load image file into graphic window"""
    image = Image(Point(0, 0), pic_file)
    width = image.getWidth()
    height = image.getHeight()
    image.move(width // 2, height // 2)
    win = GraphWin(pic_file, width, height)
    image.draw(win)
    win.getMouse()
    return image


def convert_to_grayscale(image):
    """Converts all pixels to grayscale"""
    for row in range(image.getWidth()):
        for column in range(image.getHeight()):
            r, g, b = image.getPixel(row, column)
            gray_izer = int(round(0.299 * r + 0.578 * g + 0.114 * b))
            image.setPixel(row, column, color_rgb(gray_izer, gray_izer, gray_izer))
        # update the image # to see progress row by row
        update(60)


def main():
    print("This program converts an image to grayscale.")

    in_file = input("Enter the name of the pic to convert: ")
    image = open_image(in_file)

    print("Click the image to start conversion...")
    print("Converting...", end="")
    convert_to_grayscale(image)

    print("Done")

    out_file = input("Enter filename for the converted image: ")
    image.save(out_file)


if __name__ == '__main__':
    main()
