#
# --charset 0123456789-.°C
#

import argparse
import os
import sys

from u8g.font import U8GFont
from u8g.glyph import U8GGlyph
from utils.bytewriter import ByteAsBytearrayWriter


def char_info(char_enc: int):
    return "0x{0:02x} ({0:d}) '{1}'".format(char_enc, chr(char_enc))


def repack_and_write(stream, font_data, charset):

    font = U8GFont(font_data)

    #
    # header
    #
    include_encodings = None
    if charset:  # if we should to include only specified characters
        include_encodings = {ord(x) for x in str(charset)}  # deduplicate
        enc_start = min(include_encodings)  # in repacked font header -- starting character
        enc_end = min(max(include_encodings), font.enc_end)  # in repacked font header -- ending character
        start_cap_a_pos = 0  # in repacked font header -- position of capital letter 'A'
        start_sm_a_pos = 0  # in repacked font header -- position of small letter 'a'
    else:  # we include all characters in the given font
        start_cap_a_pos = font.start_cap_A  # keep value from original font
        start_sm_a_pos = font.start_sm_a  # keep value from original font
        enc_start = font.enc_start  # keep value from original font
        enc_end = font.enc_end  # keep value from original font

    #
    # characters data
    #
    skipped_chars = list()
    repacked_characters = bytearray()  # repacked characters data
    empty_tail = bytearray()  # keep "empty tail", that will not store if no valuable characters occurs after it
    cur_pos = U8GFont.Header.size  # skip font header and point to begin of characters data
    cur_enc = font.enc_start  # from which character we should start to iterate
    last_valuable_enc = None  # store last valuable character in the font (non-empty)
    # iterate thought characters, available in the font
    while cur_enc <= enc_end:  # and cur_pos < len(font_data):
        if cur_enc >= enc_start:  # if current encoding already at start
            if cur_enc == ord('A') and not start_cap_a_pos:  # not already set
                start_cap_a_pos = U8GFont.Header.size + len(repacked_characters) + len(empty_tail)  # save position
            if cur_enc == ord('a') and not start_sm_a_pos:  # not already set
                start_sm_a_pos = U8GFont.Header.size + len(repacked_characters) + len(empty_tail)  # save position
        byte = font_data[cur_pos]  # get byte from font data array
        if byte == 255:  # if this is "empty" (skipped) character
            skipped_chars.append(cur_enc)
            cur_pos += 1  # increment array position
            if last_valuable_enc:  # if at least one valuable character encountered
                empty_tail.extend(b'\xff')  # save "empty" character to "tail"
        else:
            ch_size = U8GGlyph.header_size(font) + U8GGlyph.data_size(font, cur_pos)
            if not include_encodings or cur_enc in include_encodings:
                if len(empty_tail):
                    repacked_characters.extend(empty_tail)
                    empty_tail.clear()
                repacked_characters.extend(font_data[cur_pos:cur_pos + ch_size])
                last_valuable_enc = cur_enc
            else:
                skipped_chars.append(cur_enc)
                if last_valuable_enc:
                    empty_tail.extend(b'\xff')
            cur_pos += ch_size
        cur_enc += 1
    if start_sm_a_pos <= last_valuable_enc :  # if small 'a' position above our last valuable character
        start_sm_a_pos = 0  # "reset" this position

    repacked_font_header = font_data[:U8GFont.Header.size]
    repacked_font_header[U8GFont.Header.start_cap_A_offset] = (start_cap_a_pos >> 8) & 0xff
    repacked_font_header[U8GFont.Header.start_cap_A_offset + 1] = start_cap_a_pos & 0xff
    repacked_font_header[U8GFont.Header.start_sm_a_offset] = (start_sm_a_pos >> 8) & 0xff
    repacked_font_header[U8GFont.Header.start_sm_a_offset + 1] = start_sm_a_pos & 0xff
    repacked_font_header[U8GFont.Header.enc_start_offset] = enc_start
    repacked_font_header[U8GFont.Header.enc_end_offset] = last_valuable_enc  # enc_end

    font2_data = bytearray()
    font2_data.extend(repacked_font_header)
    font2_data.extend(repacked_characters)
    font2 = U8GFont(font2_data)
    print(font)
    print("Skipped chars: {}".format(''.join(chr(x) for x in skipped_chars)))
    print(font2)

    stream.write("# {}\n".format(repr(font2)))
    stream.write('all_chars = """{}"""\n'.format(font2.get_all_chars()))
    # bw_font = ByteAsIntArrayWriter(stream, 'data')
    bw_font = ByteAsBytearrayWriter(stream, 'data')
    bw_font.out_data(repacked_font_header)
    bw_font.out_data(repacked_characters)
    bw_font.eot()

    if args.charset is None:
        pass


def quit(msg):
    print(msg)
    sys.exit(1)


DESC = """u8gfont_repack.py
Utility to repack .
Sample usage:
u8gfont_repack.py <infile.py> <outfile.py>
"""

if __name__ == "__main__":

    parser = argparse.ArgumentParser(__file__, description=DESC, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', type=str, help='Input file path')
    parser.add_argument('outfile', type=str, help='Path and name of output file')
    parser.add_argument('-c', '--charset',
                        type=str,
                        help='Character set. e.g. 1234567890 or @filename.ext to load from file',
                        default='')
    args = parser.parse_args()

    req_charset = None
    if args.charset:
        if args.charset[0] == '@':
            charset_filename = args.charset[1:]
            print("Loading charset from file '{}'".format(charset_filename))
            if not os.path.isfile(charset_filename):
                quit("Can't load charset from file '{}'".format(charset_filename))
            req_charset = open(charset_filename).read()
        else:
            req_charset = args.charset
        print("Requested charset: {}".format(req_charset))

    font_vars = {}
    with open(args.infile, 'r') as infile:
        exec(infile.read(), font_vars)

    try:
        with open(args.outfile, 'w', encoding='utf-8') as stream:
            repack_and_write(stream, bytearray(font_vars['data']), req_charset)
    except OSError:
        print("Can't open", args.infile, 'for writing')
