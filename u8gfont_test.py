#!/usr/bin/env python3

from PIL import Image, ImageDraw

import font_6x10_repacked as font
# import font_8x13B_repacked as font
# import font_helvb24r_repacked as font
# import font_repacked as font

from u8g.font import U8GFont


fgi = U8GFont(font.data)
print(fgi)

img = Image.new('L', (1800, 200), 'white')
draw = ImageDraw.Draw(img)


def draw_pixel(x: int, y: int):
    draw.point((x, y))


def draw_font(x, y, rng: range):
    str = ''
    for i in rng:
        str += chr(i)
    r = fgi.draw_string(x, y, str, draw_pixel)
    draw.rectangle(((r[0], r[1]), (r[2], r[3])))
    return r

# (_, _, _, y1) = draw_font(10, 10, range(33, 64))
# (_, _, _, y1) = draw_font(10, y1, range(65, 96))
# (_, _, _, y1) = draw_font(10, y1, range(97, fgi.enc_end))
(_, _, _, y1) = draw_font(10, 10, range(fgi.enc_start, fgi.enc_end + 1))

# r = fgi.draw_string(10, 10, '"A', draw_pixel)
# draw.rectangle(((r[0], r[1]), (r[2], r[3])))

img.show()