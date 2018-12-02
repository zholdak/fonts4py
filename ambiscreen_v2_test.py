from PIL import Image, ImageDraw

from canvas.canvas import Canvas
from u8g.font import U8GFont
from u8g.glyph import U8GGlyph


class Drawing(Canvas):

    EPD_WIDTH = 200
    EPD_HEIGHT = 200

    def __init__(self):
        super().__init__(self.EPD_WIDTH, self.EPD_HEIGHT, rotate=Canvas.ROTATE_0)
        self.img = Image.new('L', (self.EPD_WIDTH, self.EPD_HEIGHT), 'white')
        self.draw = ImageDraw.Draw(self.img)

    def draw_absolute_pixel(self, x, y):
        self.draw.point((x, y))

    def update(self):
        self.img.show()

    def draw_battery(self, x: int, y: int, pc: int = 0, width: int = 10, height: int = 30):
        """
        Draw battery indicator

        :param x: Horizontal position
        :param y: Vertical position of left-top corner of battery indicator
        :param width: Width of the battery indicator. 10 by default
        :param height: Height of the battery indicator. 30 by default
        :param pc: Percent of battery. 0 by default
        :return: None
        """
        pc = 100 if pc > 100 else 0 if pc < 0 else pc
        piptik_height = 3
        piptik_padding = 3
        inner_margin = 2
        full = height - piptik_height - inner_margin * 2
        filled = full * pc // 100
        self.draw_filled_rect(x + piptik_padding, y, x + width - piptik_padding, y + piptik_height)
        self.draw_rect(x, y + piptik_height, x + width, y + height, width=1)
        self.draw_filled_rect(x + inner_margin, y + piptik_height + inner_margin + (full - filled),
                              x + width - inner_margin, y + height - inner_margin)

    def draw_temperature(self, x: int = None, y: int= 0, temp: float = 24.5):
        """
        Draw Temperature indicator

        :param x: Horizontal position. Is not specified -- indicator will be centered in the whole screen
        :param y: Vertical position
        :param temp: Temperature (float) value, 24.5, for example.
        :return: Tuple of left-top and right-bottom (x0, y0, x1, y1) coordinated of temperature indicator
        """

        import pyfonts.font_lato_bold_21_degC as font_b21degC_data
        import pyfonts.font_lato_bold_33_numbers as font_b33n_data
        import pyfonts.font_lato_bold_58_numbers as font_b58n_data

        text0 = str(int(temp))
        text1 = ".{:d}".format(int(temp * 10 % 10))
        textc = '°C'
        font0 = U8GFont(font_b58n_data.data)
        font1 = U8GFont(font_b33n_data.data)
        font2 = U8GFont(font_b21degC_data.data)
        text0w, text0h = font0.string_exact_width_height(text0, hspacing=2)
        text1w, text1h = font1.string_exact_width_height(text1, hspacing=2)
        textcw = font2.string_exact_width(textc, hspacing=2)
        w = text0w + text1w + U8GGlyph.glyph_xoffset(font1, ord('.')) + 2
        x0 = (self.width / 2) - (w / 2) if x is None else x
        x1 = x0 + w
        y1 = y + text0h
        self.draw_string_exact(x0, y, text0, font0, hspacing=2)
        self.draw_string_exact(x1 - text1w, y1 - text1h, text1, font1, hspacing=2)
        self.draw_string_exact(x1 - textcw, y, textc, font2, hspacing=2)

        del font0
        del font1
        del font2
        del font_b21degC_data
        del font_b33n_data
        del font_b58n_data

        return x0, y, x1, y1

    def draw_humidity(self, x: int = 0, y: int = 0, humid: int = 54):
        """
        Draw humidity indicator

        :param x: Horizontal position
        :param y: Vertical position
        :param humid: Humidity value
        :return: Tuple of left-top and right-bottom (x0, y0, x1, y1) coordinated of humidity indicator
        """

        from gfx import pc_rh_xbm as xbm
        import pyfonts.font_lato_bold_40_numbers as font_b40n_data

        font = U8GFont(font_b40n_data.data)
        text = str(int(humid))
        (_, _, _, _), (dx0, _, dx1, _) = self.draw_string_exact(x, y, text, font, hspacing=-1)
        last_text_char = ord(text[len(text)-1:len(text)])  # get last char from humidity string
        xoff = U8GGlyph.glyph_xoffset(font, last_text_char) + 2  # proper interval from humidity value
        _, _, x1, y1 = self.draw_xbm(x + (dx1 - dx0) + xoff + 3, y, xbm)

        del font
        del font_b40n_data
        del xbm

        return x, y, x1, y1

    def draw_pressure(self, x: int = 0, y: int = 0, press: int = 754, align=Canvas.ALIGN_RIGHT):
        """
        Draw pressure indicator

        :param x: Horizontal position
        :param y: Vertical position
        :param press: Pressure value (in mmHg)
        :param align: Align Canvas.ALIGN_LEFT of Canvas.ALIGN_RIGHT
        :return: Tuple of left-top and right-bottom (x0, y0, x1, y1) coordinated of pressure indicator
        """

        from gfx import mmhg_xbm as xbm
        import pyfonts.font_lato_bold_40_numbers as font_b40n_data

        text = str(press)
        font = U8GFont(font_b40n_data.data)
        (text_width, text_height) = font.string_exact_width_height(text, hspacing=-1)
        last_text_char = ord(text[len(text)-1:len(text)])  # get last char from humidity string
        xoff = U8GGlyph.glyph_xoffset(font, last_text_char) + 2  # proper interval from humidity value
        x0 = x if align == Canvas.ALIGN_LEFT else self.width - x - text_width - xbm.width - xoff
        x1 = x0 + text_width + xbm.width + xoff if align == Canvas.ALIGN_LEFT else self.width - x
        y0 = y
        y1 = y0 + max(text_height, xbm.height)
        self.draw_xbm(x1 - xbm.width, y, xbm)
        self.draw_string_exact(x0, y0, text, font, hspacing=-1)

        del font
        del font_b40n_data
        del xbm

        return x0, y0, x1, y1

    def draw_grid(self, x0: int, y0: int, x1: int, y1: int, step: int, hcount: int, min_text: str, max_text: str):
        """
        Draws graph grid

        :param x0: Left-top horizontal position of the graph boundary
        :param y0: Left-top vertical position of the graph boundary
        :param x1: Right-bottom horizontal position of the graph boundary
        :param y1: Right-bottom vertical position of the graph boundary
        :param step: Step (in pixels) to draw horizonval grid
        :param font: Font to draw minimum and maximum values on left-vertical axis
        :param min_text: Text with minimum value, to be written on right vertical axis
        :param max_text: Text with maximum value, to be written on right vertical axis
        :return: Tuple of left-top and right-bottom (x0, y0, x1, y1) coordinated of available graph boundary
        """

        import pyfonts.font_profont11_6x7_numbers as font_b9n_data

        font = U8GFont(font_b9n_data.data)
        max_text_w = font.string_width(max_text, hspacing=1)
        self.draw_string(x0, y0, max_text, font, hspacing=1)
        min_text_w, min_text_h = font.string_width_height(min_text, hspacing=1)
        self.draw_string(x0, y1 - min_text_h, min_text, font, hspacing=1)
        x = x0 + max(max_text_w, min_text_w) + 2
        self.draw_line(x, y0, x, y1, width=2)
        self.draw_line(x, y1 - 1 - 1, x1, y1 - 1 - 1, width=2)

        grid_rows_count = (y1 - y0 - 1) // step
        # for i in range(1, grid_rows_count + 1):
        #     y = y1 - 1 - i * step
        #     self.draw_line(x, y, x1, y)
        self.draw_line(x - 1, y0, x + 2, y0)
        self.draw_line(x - 1, y1 - 4, x + 2, y1 - 4)
        hstep = (x1 - x) / hcount
        for i in range(hcount):
            hx = x + 5 + (i * hstep)
            self.draw_line(hx, y1 - 3, hx, y1)

        del font
        del font_b9n_data

        return x + 5, y0, x1, y1 - 4

    def draw_graph(self, x0: int, y0: int, x1: int, y1: int, graph_data):
        """
        Draws graph

        :param x0: Left-top horizontal position of the graph boundary
        :param y0: Left-top vertical position of the graph boundary
        :param x1: Right-bottom horizontal position of the graph boundary
        :param y1: Right-bottom vertical position of the graph boundary
        :param graph_data: Array of graph data
        :return: None
        """
        hcount = len(graph_data)
        min_value = min(graph_data)
        max_value = max(graph_data)
        value_delta = max_value - min_value
        y1 -= 2
        graph_width = x1 - x0
        graph_height = y1 - y0
        hstep = graph_width / hcount

        for i in range(hcount):
            cur_delta = max_value - graph_data[i]
            offset = graph_height // 2 if value_delta == 0 else (cur_delta * graph_height) / value_delta
            x = x0 + (hstep * i)
            y = y1 - graph_height + offset
            if i == 0:  # this is first point, don't draw it, just save first point
                lx0 = x
                ly0 = y
            else:
                lx1 = x1 if i == hcount - 1 else x
                ly1 = y
                c.draw_line(lx0, ly0, lx1, ly1, 3)
                lx0 = lx1  # end point of current line became first point on next iterate
                ly0 = ly1

    def draw_status(self, text: str):
        from pyfonts import u8g_font_helvB08_full
        font = U8GFont(u8g_font_helvB08_full.data)
        text_width, text_height = font.string_exact_width_height(text, hspacing=0)
        self.draw_string_exact(self.width / 2 - text_width / 2, self.height - text_height - 2, text, font, hspacing=0)
        del font
        del u8g_font_helvB08_full

c = Drawing()
c.draw_battery(c.width - 12, 2, 100)
_, _, _, y = c.draw_temperature(y=5, temp=24.7)
c.draw_humidity(x=0, y=y + 10, humid=54)
_, _, _, y = c.draw_pressure(x=0, y=y + 10, press=754, align=Canvas.ALIGN_RIGHT)

press_data = [759.46, 759.46, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92,
              754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 751.84, 751.84,
              751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84,
              751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84,
              751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84,
              751.84, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38,
              754.38, 754.38, 754.38, 754.38, 754.38, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92,
              756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 759.46, 759.46, 759.46,
              759.46, 759.46, 759.46, 759.46]

# press_data = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 2, 2,
#               2, 2, 2, 3, 3, 4, 5, 6, 5, 4, 4, 4, 3, 3]
graph_data = [int(i) for i in press_data[:48]]

x0, y0, x1, y1 = c.draw_grid(x0=2, y0=y + 10, x1=197, y1=y + 6 + 50, step=10, hcount=len(graph_data),
                             min_text=str(min(graph_data)), max_text=str(max(graph_data)))
c.draw_graph(x0, y0, x1, y1, graph_data)
c.draw_status("2018/01/16 21:28:33")
c.update()


# from PIL import Image, ImageDraw
#
# import pyfonts.font_lato_bold_58_full as font_b58f_data
# font_b58f = U8GFont(font_b58f_data.data)
#
# img = Image.new('L', (200, 200), 'white')
# draw = ImageDraw.Draw(img)
#
#
# def draw_pixel(x: int, y: int):
#     draw.point((x, y))
#
#
# (x0, y0, x1, y1), (dx0, dy0, dx1, dy1) = font_b58f.draw_string(10, 10, '27.3', draw_pixel)
# draw.rectangle(((x0, y0), (x1, y1)))
# draw.rectangle(((dx0, dy0), (dx1, dy1)))
#
# img.show()

#
#
# # import pyfonts.font_lato_bold_36_full as lb36
# # pf = U8GFont(lb36.data)
#
# import pyfonts.font_lato_bold_58_numbers as lb58
# pf = U8GFont(lb58.data)
#
# pf.draw_string(10, 10, "25", draw_pixel)
#
#