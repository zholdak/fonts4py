#!/bin/bash

# https://github.com/olikraus/u8glib/wiki/fontsize

python3 u8gfont_repack.py pyfonts/u8g/u8g_font_profont11.py pyfonts/pyfull/font_profont11_6x7_full.py --charset @full_encoding.txt

./ttf/bdf2u8g -b 32 -e 254 -f 0 u8g_tools/bdf/helvB08.bdf u8g_font_helvB08 pyfonts/u8g/u8g_font_helvB08.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_helvB08.py pyfonts/pyfull/font_helvB08_full.py --charset @full_encoding.txt

otf2bdf -p 21 ttf/Lato-Bold.ttf > ttf/Lato-Bold-21.bdf
./ttf/bdf2u8g -b 32 -e 254 -f 0 ttf/Lato-Bold-21.bdf u8g_font_lato_bold_21 pyfonts/u8g/u8g_font_lato_bold_21.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_21.py pyfonts/pyfull/font_lato_bold_21_full.py --charset @full_encoding.txt

otf2bdf -p 33 ttf/Lato-Bold.ttf > ttf/Lato-Bold-33.bdf
./ttf/bdf2u8g -b 32 -e 254 -f 0 ttf/Lato-Bold-33.bdf u8g_font_lato_bold_33 pyfonts/u8g/u8g_font_lato_bold_33.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_33.py pyfonts/pyfull/font_lato_bold_33_full.py --charset @full_encoding.txt

otf2bdf -p 40 ttf/Lato-Bold.ttf > ttf/Lato-Bold-40.bdf
./ttf/bdf2u8g -b 32 -e 254 -f 44 ttf/Lato-Bold-40.bdf u8g_font_lato_bold_40 pyfonts/u8g/u8g_font_lato_bold_40.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_40.py pyfonts/pyfull/font_lato_bold_40_full.py --charset @full_encoding.txt

otf2bdf -p 58 ttf/Lato-Bold.ttf > ttf/Lato-Bold-58.bdf
./ttf/bdf2u8g -b 32 -e 254 -f 44 ttf/Lato-Bold-58.bdf u8g_font_lato_bold_58 pyfonts/u8g/u8g_font_lato_bold_58.py
python3 u8gfont_repack.py pyfonts/u8g/u8g_font_lato_bold_58.py pyfonts/pyfull/font_lato_bold_58_full.py --charset @full_encoding.txt

######

python3 u8gfont_repack.py pyfonts/pyfull/font_profont11_6x7_full.py pyfonts/font_profont11_6x7_numbers.py --charset 1234567890.-
python3 u8gfont_repack.py pyfonts/pyfull/font_helvB08_full.py pyfonts/font_helvB08_full.py --charset @full_encoding.txt

python3 u8gfont_repack.py pyfonts/pyfull/font_lato_bold_21_full.py pyfonts/font_lato_bold_21_degC.py --charset °C
python3 u8gfont_repack.py pyfonts/pyfull/font_lato_bold_33_full.py pyfonts/font_lato_bold_33_numbers.py --charset 1234567890.
python3 u8gfont_repack.py pyfonts/pyfull/font_lato_bold_40_full.py pyfonts/font_lato_bold_40_numbers.py --charset 1234567890.
python3 u8gfont_repack.py pyfonts/pyfull/font_lato_bold_58_full.py pyfonts/font_lato_bold_58_numbers.py --charset 1234567890-


###### XBM IMAGES

python3 xbm_repack.py gfx/mmhg.xbm gfx/mmhg_xbm.py
python3 xbm_repack.py gfx/pc_rh.xbm gfx/pc_rh_xbm.py
