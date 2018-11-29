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
    # byte 0 == 255 indicates empty glyph

    # def __init__(self, font, req_enc: int):
    #
    #     self.font = font
    #     self.req_enc = req_enc
    #
    #     try:
    #         self.header_pos = U8GGlyph.glyph_start(self.font, self.req_enc)
    #         if self.header_pos >= len(self.font.font_data):
    #             raise U8GInvalidFont("Invalid position: it greater than total bytes if current font!")
    #
    #         if self.font.font_data[self.header_pos] == 255:
    #             self.data_pos = None
    #         else:
    #             self.data_pos = self.header_pos + U8GGlyph.header_size(self.font)
    #
    #         if self.data_pos:
    #             if self.header_pos + U8GGlyph.header_size(self.font) >= len(self.font.font_data):
    #                 raise U8GInvalidFont(
    #                     "Invalid position: pointer to data's first byte is greater than total bytes in current font!")
    #
    #             self.width = self.font.font_data[self.header_pos + U8GGlyph.Header.width_offset]
    #             self.height = self.font.font_data[self.header_pos + U8GGlyph.Header.height_offset]
    #
    #             self.data_size = self.font.font_data[self.header_pos + U8GGlyph.Header.size_offset]
    #             if self.data_size > len(self.font.font_data):
    #                 raise U8GInvalidFont("Invalid position: len of current glyph data out of total font's data array")
    #
    #             self.deltax = self.font.font_data[self.header_pos + 3]
    #             self.xoffset = self.font.font_data[self.header_pos + 4]
    #             self.xoffset = self.xoffset - 256 if self.xoffset > 127 else self.xoffset
    #             self.yoffset = self.font.font_data[self.header_pos + 5]
    #             self.yoffset = self.yoffset - 256 if self.yoffset > 127 else self.yoffset
    #
    #     except U8GNoGlyph:
    #         self.header_pos = None
    #         self.data_pos = None

    # def __str__(self):
    #     return "pos={}, width={}, height={}, data_size={}, deltax={}, xoffset={}, yoffset={}" \
    #         .format(self.header_pos, self.width, self.height, self.data_size, self.deltax, self.xoffset, self.yoffset)
    #
    # def __len__(self):
    #     return self.data_size

    @staticmethod
    def isvalid(font, pos):
        return pos and font.font_data[pos] != 255

    @staticmethod
    def header_size(font):
        if font.format == 0:
            return 6
        elif font.format == 1:
            return 3

    @staticmethod
    def width(font, enc_pos):
        if font.format == 0:
            return font.font_data[enc_pos + 0]
        elif font.format == 1:
            return (font.font_data[enc_pos + 1] & 0xf0) >> 4

    @staticmethod
    def height(font, enc_pos):
        if font.format == 0:
            return font.font_data[enc_pos + 1]
        elif font.format == 1:
            return font.font_data[enc_pos + 1] & 0x0f

    @staticmethod
    def data_size(font, enc_pos):
        if font.format == 0:
            return font.font_data[enc_pos + 2]
        elif font.format == 1:
            return font.font_data[enc_pos + 2] & 0x0f

    @staticmethod
    def deltax(font, enc_pos):
        if font.format == 0:
            deltax = font.font_data[enc_pos + 3]
            return deltax - 256 if deltax > 127 else deltax
        elif font.format == 1:
            deltax = (font.font_data[enc_pos + 2] & 0xf0) >> 4
            return -(deltax & 0x07) if deltax & 0x08 else deltax

    @staticmethod
    def xoffset(font, enc_pos):
        if font.format == 0:
            xoffset = font.font_data[enc_pos + 4]
            return xoffset - 256 if xoffset > 127 else xoffset
        elif font.format == 1:
            xoffset = (font.font_data[enc_pos + 0] & 0xf0) >> 4
            return -(xoffset & 0x07) if xoffset & 0x08 else xoffset

    @staticmethod
    def yoffset(font, enc_pos):
        if font.format == 0:
            yoffset = font.font_data[enc_pos + 5]
            return yoffset - 256 if yoffset > 127 else yoffset
        elif font.format == 1:
            yoffset = font.font_data[enc_pos + 0] & 0x0f
            return -(yoffset & 0x07) if yoffset & 0x08 else yoffset

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
