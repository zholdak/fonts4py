from PIL import Image, ImageDraw

from canvas import Canvas
from bmp import BitmapHeader, BitmapHeaderInfo
import sys
import math

# ./font_to_py.py DejaVuSans.ttf 7 sans_numbers_dot_minus_7.py -xi -c 1234567890.-
# ./font_to_py.py DejaVuSans.ttf 8 sans_8.py -xi -c 1234567890.°-C%RHmg
# ./font_to_py.py DejaVuSans.ttf 9 sans_9.py -xi -c 1234567890.°-C%RHmg
# ./font_to_py.py DejaVuSans.ttf 13 sans_13.py -xi -c 1234567890.°-C%RHmg
# ./font_to_py.py DejaVuSans.ttf 14 sans_14.py -xi -c 1234567890.°-C%RHmg
#
# ./font_to_py.py Lato-Bold.ttf 58 lato_bold_numbers_minus_58.py -xi -c 1234567890-
# ./font_to_py.py Lato-Bold.ttf 40 lato_bold_numbers_dot_40.py -xi -c 1234567890.
# ./font_to_py.py Lato-Bold.ttf 33 lato_bold_numbers_dot_33.py -xi -c 1234567890.
# ./font_to_py.py Lato-Bold.ttf 21 lato_bold_deg_cels_21.py -xi -c °C


import fonts.lato_bold_deg_cels_21
import fonts.lato_bold_numbers_dot_40
import fonts.lato_bold_numbers_dot_33
import fonts.lato_bold_numbers_minus_58

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

    def draw_battery(self, x, y, pc=0, width=10, height=30):
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

    def draw_temperature(self, x=None, y=0, temp=24.5):
        """
        Draw Temperature indicator

        :param x: Horizontal position. Is not specified -- indicator will be centered in the whole screen
        :param y: Vertical position
        :param temp: Temperature (float) value, 24.5, for example.
        :return: Tuple of left-top and right-bottom (x0, y0, x1, y1) coordinated of temperature indicator
        """
        text0 = str(int(temp))
        text1 = ".{:d}".format(int(temp * 10 % 10))
        textc = '°C'
        font0 = fonts.lato_bold_numbers_minus_58
        font1 = fonts.lato_bold_numbers_dot_33
        font2 = fonts.lato_bold_deg_cels_21
        if x is None:
            w = self.string_width(text0, font0) - 4
            w += self.string_width(text1, font1) - 4
        x = self.width / 2 - w / 2
        x0 = x
        x1 = self.width / 2 + w / 2
        x += self.draw_string(x, y, text0, font0, condensed=2)
        x += self.draw_string(x, y + font0.height() - font1.height(), text1, font1, condensed=2)
        w = self.string_width(textc, font2)
        self.draw_string(x - w - 2, y, textc, font2)
        return x0, y, x1, y + font0.height()

    def draw_humidity(self, x=0, y=0, humid=54):
        """
        Draw humidity indicator

        :param x: Horizontal position
        :param y: Vertical position
        :param humid: Humidity value
        :return: Tuple of left-top and right-bottom (x0, y0, x1, y1) coordinated of humidity indicator
        """
        f = fonts.lato_bold_numbers_dot_40
        w = self.draw_string(x, y, str(int(humid)), f, condensed=1)
        _, _, x1, y1 = self.draw_xbm(x + w + 3, y, 'pc_rh.xbm')
        return x, y, x1, y1

    def draw_pressure(self, x=0, y=0, press=754, align=Canvas.ALIGN_RIGHT):
        """
        Draw pressure indicator

        :param x: Horizontal position
        :param y: Vertical position
        :param press: Pressure value (in mmHg)
        :param align: Align Canvas.ALIGN_LEFT of Canvas.ALIGN_RIGHT
        :return: Tuple of left-top and right-bottom (x0, y0, x1, y1) coordinated of pressure indicator
        """
        t = str(press)
        f = fonts.lato_bold_numbers_dot_40
        tw = self.string_width(t, f) - (1 * len(t))  # will be printed condensed
        xbm = self.get_xbm_dimension('mmhg.xbm')
        bw = next(xbm)  # bmp width
        _ = next(xbm)  # ignore height
        x0 = x + tw if align == Canvas.ALIGN_LEFT else self.width - x - bw
        self.draw_xbm(x0, y, 'mmhg.xbm')  # width is 17
        x0 = x if align == Canvas.ALIGN_LEFT else x0 - tw
        self.draw_string(x0, y, str(int(t)), f, condensed=1)
        if align == Canvas.ALIGN_LEFT:
            return x, y, x + tw + bw, y + f.height()
        else:
            return self.width - x - tw - bw, y, self.width - x - 1, y + f.height()

    def draw_grid(self, x0, y0, x1, y1, step, hcount, min_text, max_text):
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
        font = fonts.sans_numbers_dot_minus_7
        text_len = max(self.draw_string(x0, y0, max_text, font, condensed=1), 0)
        text_len = max(self.draw_string(x0, y1 - font.height(), min_text, font, condensed=1), text_len)
        x = x0 + text_len + 2
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
        return x + 5, y0, x1, y1 - 4

    def draw_graph(self, x0, y0, x1, y1, graph_data):
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


c = Drawing()

# _, _, _, y = c.draw_temperature(y=10, temp=28.5)
# c.draw_humidity(x=0, y=y + 10, humid=54)
# _, _, _, y = c.draw_pressure(x=0, y=y + 10, press=754, align=Canvas.ALIGN_RIGHT)
# c.draw_battery(c.width - 12, 2, 100)
#
# press_data = [759.46, 759.46, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92,
#               754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 751.84, 751.84,
#               751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84,
#               751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84,
#               751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84, 751.84,
#               751.84, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38, 754.38,
#               754.38, 754.38, 754.38, 754.38, 754.38, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92,
#               756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 756.92, 759.46, 759.46, 759.46,
#               759.46, 759.46, 759.46, 759.46]

# press_data = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4, 4, 3, 3, 3, 2, 2, 1, 1, 2, 2,
#               2, 2, 2, 3, 3, 4, 5, 6, 5, 4, 4, 4, 3, 3]
# graph_data = [int(i) for i in press_data[:48]]
#
# x0, y0, x1, y1 = c.draw_grid(x0=2, y0=y + 10, x1=197, y1=y + 6 + 50, step=10, hcount=len(graph_data),
#                              min_text=str(min(graph_data)), max_text=str(max(graph_data)))
# c.draw_graph(x0, y0, x1, y1, graph_data)

#c.draw_rect(x0, y0, x1, y1)

# c.draw_rect(10, 10, 190, 190)
# c.draw_filled_rect(10, 190, 190, 200)
# c.draw_circle(100, 100, 81, width=2)
# c.draw_circle(100, 100, 85)
# c.draw_filled_circle(100, 100, 20)
# c.draw_circle_arc(100, 100, 70, 0, 120)
#c.draw_char(0, 0, '8', fonts.lato_bold_numbers_50)
# c.draw_string(100 - (c.string_width('42', fonts.lato_bold_numbers_50) - 4) / 2, 120, '42', fonts.lato_bold_numbers_50)

#c.draw_rect(x0, y0, x1, y1)


import fonts.sans_12
import fonts.roboto_bold_15

y = 2

c.draw_string(10, y, '.123456789', fonts.roboto_bold_15, condensed=-1)
y += fonts.lato_bold_deg_cels_21.height() + 2

c.draw_string(10, y, 'QWEMLJGCVZAL', fonts.roboto_bold_15, condensed=-1)
y += fonts.lato_bold_deg_cels_21.height() + 2

c.draw_string(10, y, 'qwemljgcvzal', fonts.roboto_bold_15, condensed=-1)
y += fonts.lato_bold_deg_cels_21.height() + 2

#
# c.draw_string(10, y, '°C', fonts.lato_bold_deg_cels_21, condensed=1)
# y += fonts.lato_bold_deg_cels_21.height() + 2
#
# c.draw_string(10, y, '.42567890', fonts.lato_bold_numbers_dot_33, condensed=2)
# y += fonts.lato_bold_numbers_dot_33.height() + 2
#
# c.draw_string(10, y, '.42567890', fonts.lato_bold_numbers_dot_40, condensed=2)
# y += fonts.lato_bold_numbers_dot_40.height() + 2
#
# c.draw_string(10, y, '-42', fonts.lato_bold_numbers_minus_58, condensed=2)
# y += fonts.lato_bold_numbers_minus_58.height() + 2
#
# c.draw_xbm(160, 160, 'pc_rh.xbm')
# c.draw_xbm(183, 160, 'mmhg.xbm')


#c.load_xbm(0, 0, "ambi.xbm")

c.update()
