# -*- coding: utf-8 -*-
from PIL import Image


class ImgToTxt(object):
    def conv(self, path):
        im = Image.open(path).resize((32, 32))
        im.save("tmp2-2.png")
        lena = im.convert("1")
        width, height = lena.size
        string = ""
        for x in range(0, width):
            for y in range(0, height):
                num = 1 - lena.getpixel((y, x)) / 255
                string += str(num)
            string += '\n'
        with open('test.txt', 'w') as f:
            f.write(string)
