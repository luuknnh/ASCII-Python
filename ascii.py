import ascii_magic

""" This code will create ascii image from the chosen image in the image directory. Place the wanted image in the directory and run the file. """

draw_image = ascii_magic.from_image_file("./images/dart.jpg", colums=200, char="#")


if __name__ == "__main__":
    ascii_magic.to_terminal(draw_image)