#
# U8 Glyph
#

from u8g.error import U8GInvalidFont, U8GNoGlyph


class U8GGlyph:

    # offset
    # = format 0 =
    # 0  BBX width     unsigned
    # 1  BBX height    unsigned
    # 2  data size     unsigned    (BBX width + 7)/8 * BBX height
    # 3  DWIDTH        signed
    # 4  BBX xoffset   signed
    # 5  BBX yoffset   signed
    # = format 1 =
    # 0  BBX xoffset   signed --> upper 4 Bit
    # 0  BBX yoffset   signed --> lower 4 Bit
    # 1  BBX width     unsigned --> upper 4 Bit
    # 1  BBX height    unsigned --> lower 4 Bit
    # 2  data size     unsigned -(BBX width + 7)/8 * BBX height --> lower 4 Bit
    # 2  DWIDTH        signed --> upper  4 Bit
    # = format 44 =
    # 0  BBX width     unsigned
    # 1  BBX height    unsigned
    # 2  data size     unsigned    (BBX width + 7)/8 * BBX height
    # 4  DWIDTH        signed
    # 5  BBX xoffset   signed
    # 6  BBX yoffset   signed
    # byte 0 == 255 indicates empty glyph

    @staticmethod
    def isvalid(font, pos):
        return pos and font.font_data[pos] != 255

    @staticmethod
    def header_size(font):
        if font.format == 0:
            return 6
        elif font.format == 44:
            return 7
        elif font.format == 1:
            return 3

    @staticmethod
    def width(font, enc_pos):
        if enc_pos:
            if font.format == 0:
                return font.font_data[enc_pos + 0]
            elif font.format == 44:
                return font.font_data[enc_pos + 0]
            elif font.format == 1:
                return font.font_data[enc_pos + 1] >> 4
        else:
            return 0

    @staticmethod
    def height(font, enc_pos):
        if font.format == 0:
            return font.font_data[enc_pos + 1]
        elif font.format == 44:
            return font.font_data[enc_pos + 1]
        elif font.format == 1:
            return font.font_data[enc_pos + 1] & 0x0f

    @staticmethod
    def data_size(font, enc_pos):
        if font.format == 0:
            return font.font_data[enc_pos + 2]
        elif font.format == 44:
            return (font.font_data[enc_pos + 2] << 8) | font.font_data[enc_pos + 3]
        elif font.format == 1:
            return font.font_data[enc_pos + 2] & 0x0f

    @staticmethod
    def deltax(font, enc_pos):
        if font.format == 0:
            deltax = font.font_data[enc_pos + 3]
            return deltax - 256 if deltax > 127 else deltax
        elif font.format == 44:
            deltax = font.font_data[enc_pos + 4]
            return deltax - 256 if deltax > 127 else deltax
        elif font.format == 1:
            deltax = (font.font_data[enc_pos + 2] & 0xf0) >> 4
            return -(deltax & 0x07) if deltax & 0x08 else deltax

    @staticmethod
    def xoffset(font, enc_pos):
        if font.format == 0:
            xoffset = font.font_data[enc_pos + 4]
            return xoffset - 256 if xoffset > 127 else xoffset
        elif font.format == 44:
            xoffset = font.font_data[enc_pos + 5]
            return xoffset - 256 if xoffset > 127 else xoffset
        elif font.format == 1:
            return font.font_data[enc_pos + 0] >> 4

    @staticmethod
    def yoffset(font, enc_pos):
        if font.format == 0:
            yoffset = font.font_data[enc_pos + 5]
            return yoffset - 256 if yoffset > 127 else yoffset
        elif font.format == 44:
            yoffset = font.font_data[enc_pos + 6]
            return yoffset - 256 if yoffset > 127 else yoffset
        elif font.format == 1:
            yoffset = font.font_data[enc_pos + 0] & 0x0f
            return yoffset - 2

    @staticmethod
    def size(font, pos):
        return 1 if font.font_data[pos] == 255 else U8GGlyph.header_size(font) + U8GGlyph.data_size(font, pos)

    @staticmethod
    def glyph_pos(font, req_enc: int):
        """
        Iterate font array and try to find required character symbol header start

        :return: Index of start position of required character in the font array
        """

        start = font.enc_start
        end = font.enc_end

        # a little speed optimization when find character in the array
        if req_enc >= 97 and font.start_sm_a:  # 97 = 'a' (small letter 'a')
            start = 97
            pos = font.start_sm_a
        elif req_enc >= 65 and font.start_cap_A:  # 65 = 'A' (capital letter 'A')
            start = 65
            pos = font.start_cap_A
        else:
            pos = font.Header.size

        # iterate array and try to find required character symbol header start
        cur_enc = start
        while cur_enc <= end and pos < font.len:
            if cur_enc == req_enc:
                return pos
            pos += U8GGlyph.size(font, pos)
            cur_enc += 1

        return None
        # raise U8GNoGlyph("No character {} ({}) defined in this font!".format(req_enc, chr(req_enc)))
