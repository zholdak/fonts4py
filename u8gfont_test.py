#!/usr/bin/env python3

from PIL import Image, ImageDraw

# import pyfonts.font_5x_baby_full as font
# import pyfonts.font_5x_micro_full as font
# import pyfonts.font_4x6_full as font
# import pyfonts.font_5x8_full as font
# import pyfonts.font_fixed_v0_7x7_full as font
# import pyfonts.font_profont10_5x6_full as font
import pyfonts.font_profont29_16x19_full as font

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