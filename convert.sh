#!/bin/bash

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont11.py pyfonts/pyfull/font_profont11_6x7_full.py --charset @full_encoding.txt

otf2bdf -p 21 ttf/Lato-Bold.ttf > ttf/Lato-Bold-21.bdf
./ttf/bdf2u8g -b 32 -e 254 -f 0 ttf/Lato-Bold-21.bdf u8g_font_lato_bold_21 pyfonts/u8g/u8g_font_lato_bold_21.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_21.py pyfonts/pyfull/font_lato_bold_21_full.py --charset @full_encoding.txt

otf2bdf -p 33 ttf/Lato-Bold.ttf > ttf/Lato-Bold-33.bdf
./ttf/bdf2u8g -b 32 -e 254 -f 0 ttf/Lato-Bold-33.bdf u8g_font_lato_bold_33 pyfonts/u8g/u8g_font_lato_bold_33.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_33.py pyfonts/pyfull/font_lato_bold_33_full.py --charset @full_encoding.txt

otf2bdf -p 58 ttf/Lato-Bold.ttf > ttf/Lato-Bold-58.bdf
./ttf/bdf2u8g -b 32 -e 254 -f 44 ttf/Lato-Bold-58.bdf u8g_font_lato_bold_58 pyfonts/u8g/u8g_font_lato_bold_58.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_58.py pyfonts/pyfull/font_lato_bold_58_full.py --charset @full_encoding.txt

######

python3 u8gfont_repack.py pyfonts/pyfull/font_profont11_6x7_full.py pyfonts/font_profont11_6x7_numbers.py --charset 1234567890.-

python3 u8gfont_repack.py pyfonts/pyfull/font_lato_bold_21_full.py pyfonts/font_lato_bold_21_degC.py --charset °C
python3 u8gfont_repack.py pyfonts/pyfull/font_lato_bold_33_full.py pyfonts/font_lato_bold_33_numbers.py --charset 1234567890.
python3 u8gfont_repack.py pyfonts/pyfull/font_lato_bold_58_full.py pyfonts/font_lato_bold_58_numbers.py --charset 1234567890-

######

# https://github.com/olikraus/u8glib/wiki/fontsize

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_baby.py pyfonts/pyfull/font_5x_baby_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_micro.py pyfonts/pyfull/font_5x_micro_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_4x6.py pyfonts/fpyfull/ont_4x6_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_5x8.py pyfonts/pyfull/font_5x8_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_fixed_v0.py pyfonts/pyfull/font_fixed_v0_7x7_full.py --charset @full_encoding.txt

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont10.py pyfonts/pyfull/font_profont10_5x6_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont11.py pyfonts/pyfull/font_profont11_6x7_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont12.py pyfonts/pyfull/font_profont12_6x8_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont15.py pyfonts/pyfull/font_profont15_7x9_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont17.py pyfonts/pyfull/font_profont17_9x11_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont22.py pyfonts/pyfull/font_profont22_12x14_full.py --charset @full_encoding.txt
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont29.py pyfonts/pyfull/font_profont29_16x19_full.py --charset @full_encoding.txt

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_33.py pyfonts/pyfull/font_lato_bold_33_full.py --charset @full_encoding.txt

######

