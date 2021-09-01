# negative_converter.py
#   Program converts a picture to negative.
from graphics import *
from grayscale_converter import open_image


def convert_to_negative(image):
    """Converts all pixels to negative"""
    for row in range(image.getWidth()):
        for column in range(image.getHeight()):
            r, g, b = image.getPixel(row, column)
            negativity = int(round(255 - r + 255 - g + 255 - b))
            image.setPixel(row, column, color_rgb(negativity, negativity, negativity))
        # update the image # to see progress row by row
        update(60)


def main():
    print("This program converts an image to grayscale.")

    in_file = input("Enter the name of the pic to convert: ")
    image = open_image(in_file)

    print("Click the image to start conversion...")
    print("Converting...", end="")
    convert_to_negative(image)

    print("Done")

    out_file = input("Enter filename for the converted image: ")
    image.save(out_file)


if __name__ == '__main__':
    main()
