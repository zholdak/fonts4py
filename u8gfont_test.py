#!/usr/bin/env python3

from PIL import Image, ImageDraw

import pyfonts.font_profont10_5x6_full as font_small

from u8g.font import U8GFont


fgi_small = U8GFont(font_small.data)
# print(fgi)

img = Image.new('L', (1800, 800), 'white')
draw = ImageDraw.Draw(img)


def draw_pixel(x: int, y: int):
    draw.point((x, y))


def draw_font(x, y, name, font):
    fgi = U8GFont(font.data)
    str = ''
    for i in range(fgi.enc_start, fgi.enc_end + 1):
        str += chr(i)
    r = fgi_small.draw_string(x, y, name, draw_pixel)
    r = fgi.draw_string(x, r[3], str, draw_pixel)
    draw.rectangle(((r[0], r[1]), (r[2], r[3])))
    return r

# (_, _, _, y1) = draw_font(10, 10, range(33, 64))
# (_, _, _, y1) = draw_font(10, y1, range(65, 96))
# (_, _, _, y1) = draw_font(10, y1, range(97, fgi.enc_end))

import pyfonts
import pkgutil
y1 = 10
for importer, modname, ispkg in pkgutil.iter_modules(pyfonts.__path__):
    if not ispkg:
        font_module = importer.find_module(modname).load_module(modname)
        (_, _, _, y1) = draw_font(10, y1 + 5, modname, font_module)



# (_, _, _, y1) = draw_font(10, 10, font_5x_baby_full)
# (_, _, _, y1) = draw_font(10, y1 + 5, font_5x_micro_full)
# (_, _, _, y1) = draw_font(10, y1 + 5, font_4x6_full)
# (_, _, _, y1) = draw_font(10, y1 + 5, font_5x8_full)
# (_, _, _, y1) = draw_font(10, y1 + 5, font_fixed_v0_7x7_full)
# (_, _, _, y1) = draw_font(10, y1 + 5, font_profont10_5x6_full)

# r = fgi.draw_string(10, 10, '"A', draw_pixel)
# draw.rectangle(((r[0], r[1]), (r[2], r[3])))

img.show()