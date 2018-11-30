#!/bin/bash

# https://github.com/olikraus/u8glib/wiki/fontsize

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_baby.py pyfonts/font_5x_baby_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_micro.py pyfonts/font_5x_micro_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_4x6.py pyfonts/font_4x6_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_5x8.py pyfonts/font_5x8_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_fixed_v0.py pyfonts/font_fixed_v0_7x7_full.py --charset @full_encoding.txt

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont10.py pyfonts/font_profont10_5x6_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont11.py pyfonts/font_profont11_6x7_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont12.py pyfonts/font_profont12_6x8_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont15.py pyfonts/font_profont15_7x9_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont17.py pyfonts/font_profont17_9x11_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont22.py pyfonts/font_profont22_12x14_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont29.py pyfonts/font_profont29_16x19_full.py --charset @full_encoding.txt

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_33.py pyfonts/u8g_font_lato_bold_33_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_36.py pyfonts/u8g_font_lato_bold_36_full.py --charset @full_encoding.txt
