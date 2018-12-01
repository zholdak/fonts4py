#
# U8G Font
#

from u8g.glyph import U8GGlyph
from u8g.error import U8GInvalidFont


class U8GFont:

    supported_formats = [0, 1, 44]

    class Header:
        size = 17
        start_cap_A_offset = 6
        start_sm_a_offset = 8
        enc_start_offset = 10
        enc_end_offset = 11

    def __init__(self, font_data):

        self.font_data = font_data
        self.len = len(self.font_data)
        self.format = self.font_data[0]
        if self.format not in self.supported_formats:
            raise U8GInvalidFont("Support only formats: {}".format(self.supported_formats))

        self.width = self.font_data[1]
        self.height = self.font_data[2]
        self.x_offset = int(self.font_data[3])
        self.x_offset = self.x_offset - 256 if self.x_offset > 127 else self.x_offset
        self.y_offset = int(self.font_data[4])
        self.y_offset = self.y_offset - 256 if self.y_offset > 127 else self.y_offset
        self.cap_A_height = self.font_data[5]
        self.start_cap_A = \
            (self.font_data[U8GFont.Header.start_cap_A_offset] << 8) + \
            self.font_data[U8GFont.Header.start_cap_A_offset + 1]
        self.start_sm_a = \
            (self.font_data[U8GFont.Header.start_sm_a_offset] << 8) + \
            self.font_data[U8GFont.Header.start_sm_a_offset + 1]
        self.enc_start = self.font_data[U8GFont.Header.enc_start_offset]
        self.enc_end = self.font_data[U8GFont.Header.enc_end_offset]
        self.desc_g = self.font_data[12]
        self.desc_g = self.desc_g - 256 if self.desc_g > 127 else self.desc_g
        self.max_ascent = self.font_data[13]
        self.min_descent = self.font_data[14]
        self.min_descent = self.min_descent - 256 if self.min_descent > 127 else self.min_descent
        self.xascent = self.font_data[15]
        self.xdescent = self.font_data[16]
        self.xdescent = self.xdescent - 256 if self.xdescent > 127 else self.xdescent

    def __str__(self):
        return "U8GFont(len={}, format={}, width={}, height={}, x_offset={}, y_offset={}, cap_A_height={}, " \
               "start_cap_A={}, start_sm_a={}, enc_start={}, enc_end={}, desc_g={}, max_ascent={}, min_descent={}, " \
               "xascent={}, xdescent={}, all_chars='{}')".format(self.len, self.format, self.width, self.height,
                                                                 self.x_offset, self.y_offset, self.cap_A_height,
                                                                 self.start_cap_A, self.start_sm_a, self.enc_start,
                                                                 self.enc_end, self.desc_g, self.max_ascent,
                                                                 self.min_descent, self.xascent, self.xdescent,
                                                                 self.get_all_chars())

    def __repr__(self):
        return "len={}, width={}, height={}, x_offset={}, y_offset={}, cap_A_height={}, " \
               "start_cap_A={}, start_sm_a={}, enc_start={}, enc_end={}, desc_g={}, max_ascent={}, min_descent={}, " \
               "xascent={}, xdescent={}".format(self.len, self.width, self.height, self.x_offset,
                                                self.y_offset, self.cap_A_height, self.start_cap_A, self.start_sm_a,
                                                self.enc_start, self.enc_end, self.desc_g, self.max_ascent,
                                                self.min_descent, self.xascent, self.xdescent)

    def get_all_chars(self):
        all_chars = ''
        for cur_enc in range(self.enc_start, self.enc_end + 1):
            glyph_pos = U8GGlyph.glyph_pos(self, cur_enc)
            if glyph_pos and self.font_data[glyph_pos] != 255:
                all_chars += chr(cur_enc)
        return all_chars

    def draw_char(self, x: int, y: int, ch: str, draw_pixel_func):
        """
        Draws a specified char

        :param x: Horizontal position of left-top bottom of character
        :param y: Vertical position of left-top bottom of character
        :param ch: The character to draw
        :param draw_pixel_func: Function that realizes pixel drawing. Use 'None' to just calculate char boundary
        :return: Character boundary
        """
        bound_x0 = x
        bound_y0 = y
        glyph_pos = U8GGlyph.glyph_pos(self, ord(ch))
        if U8GGlyph.isvalid(self, glyph_pos):
            # boundary & baseline
            glyph_width = U8GGlyph.width(self, glyph_pos)
            glyph_height = U8GGlyph.height(self, glyph_pos)
            glyph_xoffset = U8GGlyph.xoffset(self, glyph_pos)
            glyph_yoffset = U8GGlyph.yoffset(self, glyph_pos)
            bound_x1 = x + glyph_width + glyph_xoffset
            base_y = bound_y0 + self.max_ascent
            bound_y1 = base_y - self.min_descent
            if draw_pixel_func:
                base_x = bound_x0 + glyph_xoffset
                # glyph
                glyph_y_pos = base_y - glyph_yoffset - glyph_height
                # let draw
                glyph_byte_pos = glyph_pos + U8GGlyph.header_size(self)
                bytes_per_row = (glyph_width + 7) // 8
                for row in range(glyph_height):
                    for col in range(bytes_per_row):
                        byte = self.font_data[glyph_byte_pos]
                        bits_per_byte = 8 if col < bytes_per_row - 1 or glyph_width % 8 == 0 else glyph_width % 8
                        for bit_no in range(bits_per_byte):
                            if (byte << bit_no) & 0x80:
                                bit_x_offset = (col * 8) + bit_no
                                draw_pixel_func(base_x + bit_x_offset, glyph_y_pos)
                        glyph_byte_pos += 1
                    glyph_y_pos += 1
            return bound_x0, bound_y0, bound_x1, bound_y1
        else:
            return None

    def draw_string(self, x0: int, y0: int, string: str, draw_pixel_func, hspacing: int = 1, vspacing: int = 1):
        """

        :param x0: Horizontal position of left-top bottom of string
        :param y0: Vertical position of left-top bottom of string
        :param string: The string to draw
        :param draw_pixel_func: Function that realizes pixel drawing. Use 'None' to just calculate string boundary
        :param hspacing: Additional horizontal spacing between characters in string. Use negative values to condense
        :param vspacing: Additional vertical spacing between characters in string. Use negative values to condense
        :return: String boundary
        """
        cur_x = x0
        min_ry1 = 0
        for ch in string:
            ret = self.draw_char(cur_x, y0, ch, draw_pixel_func)
            if ret:
                rx0, ry0, rx1, ry1 = ret
                cur_x += (rx1 - rx0) + hspacing
                min_ry1 = max(min_ry1, ry1)
        return x0, y0, cur_x, min_ry1 + vspacing

    def string_boundary(self, string: str, hspacing: int = 1, vspacing: int = 1):
        return self.draw_string(0, 0, string, None, hspacing=hspacing, vspacing=vspacing)

    def string_width(self, string: str, hspacing: int = 1):
        x0, _, x1, _ = self.string_boundary(string, hspacing=hspacing)
        return x1 - x0

    def string_height(self, string: str, vspacing: int = 1):
        _, y0, _, y1 = self.string_boundary(string, vspacing=vspacing)
        return y1 - y0

    def string_width_height(self, string: str, hspacing: int = 1, vspacing: int = 1):
        x0, y0, x1, y1 = self.string_boundary(string, hspacing=hspacing, vspacing=vspacing)
        return (x1 - x0), (y1 - y0)
