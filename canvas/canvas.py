#
# https://github.com/peterhinch/micropython-epaper/blob/master/epaper.py
# https://github.com/ayoy/micropython-waveshare-epd/tree/master/epd
#

import math
from u8g.glyph import U8GGlyph
from u8g.font import U8GFont


class Canvas:

    ALIGN_RIGHT = 0
    ALIGN_LEFT = 1

    ROTATE_0 = 0
    ROTATE_90 = 1
    ROTATE_180 = 2
    ROTATE_270 = 3

    BLACK = 0
    WHITE = 1

    color = BLACK
    bg_color = WHITE

    def __init__(self, width, height, rotate=ROTATE_0):
        self.width, self.__width = width, width
        self.height, self.__height = height, height
        self.rotate = rotate

    def set_rotate(self, rotate):
        if rotate == self.ROTATE_0:
            self.rotate = self.ROTATE_0
            self.width = self.__width
            self.height = self.__height
        elif rotate == self.ROTATE_90:
            self.rotate = self.ROTATE_90
            self.width = self.__height
            self.height = self.__width
        elif rotate == self.ROTATE_180:
            self.rotate = self.ROTATE_180
            self.width = self.__width
            self.height = self.__height
        elif rotate == self.ROTATE_270:
            self.rotate = self.ROTATE_270
            self.width = self.__height
            self.height = self.__width

    def set_color(self, color):
        self.color = color

    def draw_pixel(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return
        if self.rotate == self.ROTATE_0:
            self.draw_absolute_pixel(x, y)
        elif self.rotate == self.ROTATE_90:
            point_temp = x
            x = self.__width - y
            y = point_temp
            self.draw_absolute_pixel(x, y)
        elif self.rotate == self.ROTATE_180:
            x = self.__width - x
            y = self.__height - y
            self.draw_absolute_pixel(x, y)
        elif self.rotate == self.ROTATE_270:
            point_temp = x
            x = y
            y = self.__height - point_temp
            self.draw_absolute_pixel(x, y)

    def clear(self):
        for col in range(self.width):
            for row in range(self.height):
                self.draw_pixel(col, row)

    def draw_absolute_pixel(self, x, y):
        raise NotImplementedError()

    def update(self):
        raise NotImplementedError()

    def _line(self, x0, y0, x1, y1):
        dx = x1 - x0
        dy = y1 - y0
        dx_sym = 1 if dx > 0 else -1
        dy_sym = 1 if dy > 0 else -1

        dx = dx_sym * dx
        dy = dy_sym * dy
        dx_x2 = dx * 2
        dy_x2 = dy * 2
        if dx >= dy:
            di = dy_x2 - dx
            while x0 != x1:
                self.draw_pixel(x0, y0)
                x0 += dx_sym
                if di < 0:
                    di += dy_x2
                else:
                    di += dy_x2 - dx_x2
                    y0 += dy_sym
            self.draw_pixel(x0, y0)
        else:
            di = dx_x2 - dy
            while y0 != y1:
                self.draw_pixel(x0, y0)
                y0 += dy_sym
                if di < 0:
                    di += dx_x2
                else:
                    di += dx_x2 - dy_x2
                    x0 += dx_sym
            self.draw_pixel(x0, y0)

    def draw_line(self, x0, y0, x1, y1, width=1):
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        if abs(x1 - x0) > abs(y1 - y0):  # < 45 degrees
            for w in range(-width // 2 + 1, width // 2 + 1):
                self._line(x0, y0 + w, x1, y1 + w)
        else:
            for w in range(-width // 2 + 1, width // 2 + 1):
                self._line(x0 + w, y0, x1 + w, y1)

    def _rect(self, x0, y0, x1, y1):
        self.draw_line(x0, y0, x1, y0)
        self.draw_line(x1, y0, x1, y1)
        self.draw_line(x0, y1, x1, y1)
        self.draw_line(x0, y0, x0, y1)

    def draw_rect(self, x0, y0, x1, y1, width=1):
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        x0, x1 = (x0, x1) if x1 > x0 else (x1, x0)  # x0, y0 is top left, x1, y1 is bottom right
        y0, y1 = (y0, y1) if y1 > y0 else (y1, y0)
        for w in range(width):
            self._rect(x0 + w, y0 + w, x1 - w, y1 - w)

    def draw_filled_rect(self, x0, y0, x1, y1):  # Draw filled rectangle
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        x0, x1 = (x0, x1) if x1 > x0 else (x1, x0)
        y0, y1 = (y0, y1) if y1 > y0 else (y1, y0)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                self.draw_pixel(x, y)

    def _circle(self, x0, y0, radius):
        x = - radius
        y = 0
        err = 2 - 2 * radius
        while x <= 0:
            self.draw_pixel(x0 - x, y0 + y)
            self.draw_pixel(x0 + x, y0 + y)
            self.draw_pixel(x0 + x, y0 - y)
            self.draw_pixel(x0 - x, y0 - y)
            e2 = err
            if e2 <= y:
                y += 1
                err += y * 2 + 1
                if -x == y and e2 <= x:
                    e2 = 0
            if e2 > x:
                x += 1
                err += x * 2 + 1

    def draw_circle(self, x0, y0, radius, width=1):
        x0, y0, radius = int(x0), int(y0), int(radius)
        for radius in range(radius, radius - width, -1):
            self._circle(x0, y0, radius)

        # """Python implementation of the original Bresenham algorithm for complete circles"""

        # def _px(x, y):
        #     self.draw_pixel(x + x0, y + y0)
        # switch = 3 - (2 * radius)
        # x = 0
        # y = radius
        # while x <= y:  # first quarter/octant starts clockwise at 12 o'clock
        #     _px(x, -y)  # first quarter first octant
        #     _px(y, -x)  # first quarter 2nd octant
        #     _px(y, x)  # second quarter 3rd octant
        #     _px(x, y)  # second quarter 4.octant
        #     _px(-x, y)  # third quarter 5.octant
        #     _px(-y, x)  # third quarter 6.octant
        #     _px(-y, -x)  # third quarter 6.octant
        #     _px(-x, -y)  # fourth quarter 8.octant
        #     if switch < 0:
        #         switch = switch + (4 * x) + 6
        #     else:
        #         switch = switch + (4 * (x - y)) + 10
        #         y = y - 1
        #     x = x + 1

    def draw_filled_circle(self, x0, y0, radius):
        x0, y0, radius = int(x0), int(y0), int(radius)
        x = -radius
        y = 0
        err = 2 - 2 * radius
        while x <= 0:
            self.draw_line(x0 - x, y0 - y, x0 - x, y0 + y)
            self.draw_line(x0 + x, y0 - y, x0 + x, y0 + y)
            e2 = err
            if e2 <= y:
                y += 1
                err += y * 2 + 1
                if -x == y and e2 <= x:
                    e2 = 0
            if e2 > x:
                x += 1
                err += x * 2 + 1

    def __circle_arc(self, radius, start, end, clockwise=True):
        """Python implementation of the modified Bresenham algorithm
        for complete circles, arcs and pies

        * radius: radius of the circle in pixels;
        * start and end are angles in degrees;

        function will return a list of points (tuple coordinates)
        and the coordinates of the start and end point in a list xy
        """
        start = math.radians(start)
        end = math.radians(end)
        if start >= math.pi * 2:
            start = math.radians(math.degrees(start) % 360)
        if end >= math.pi * 2:
            end = math.radians(math.degrees(end) % 360)
        # always clockwise drawing, if anti-clockwise drawing desired
        # exchange start and end
        if not clockwise:
            s = start
            start = end
            end = s
        # determination which quarters and octants are necessary
        # init vars
        xy = [[0, 0], [0, 0]]  # to locate actual start and end point for pies
        # the x/y border value for drawing the points
        q_x = []
        q_y = []
        # first q element in list q is quarter of start angle
        # second q element is quarter of end angle
        # now determine the quarters to compute
        q = []
        # 0 - 90 degrees = 12 o clock to 3 o clock = 0.0 - math.pi/2 --> q==1
        # 90 - 180 degrees = math.pi/2 - math.pi --> q==2
        # 180 - 270 degrees = math.pi - math.pi/2*3 --> q==3
        # 270 - 360 degrees = math.pi/2*3 - math.pi*2 --> q==4
        j = 0
        for i in [start, end]:
            angle = i
            if angle < math.pi / 2:
                q.append(1)
                # compute the minimum x and y-axis value for plotting
                q_x.append(int(round(math.sin(angle) * radius)))
                q_y.append(int(round(math.cos(angle) * radius)))
                if j == 1 and angle == 0:
                    xy[1] = [0, -radius]  # 90 degrees
            elif angle >= math.pi / 2 and angle < math.pi:
                q.append(2)
                # compute the minimum x and y-axis value for plotting
                q_x.append(int(round(math.cos(angle - math.pi / 2) * radius)))
                q_y.append(int(round(math.sin(angle - math.pi / 2) * radius)))
                if j == 1 and angle == math.pi / 2:
                    xy[1] = [radius, 0]  # 90 degrees
            elif angle >= math.pi and angle < math.pi / 2 * 3:
                q.append(3)
                # compute the minimum x and y-axis value for plotting
                q_x.append(int(round(math.sin(angle - math.pi) * radius)))
                q_y.append(int(round(math.cos(angle - math.pi) * radius)))
                if j == 1 and angle == math.pi:
                    xy[1] = [0, radius]
            else:
                q.append(4)
                # compute the minimum x and y-axis value for plotting
                q_x.append(int(round(math.cos(angle - math.pi / 2 * 3) * radius)))
                q_y.append(int(round(math.sin(angle - math.pi / 2 * 3) * radius)))
                if j == 1 and angle == math.pi / 2 * 3:
                    xy[1] = [-radius, 0]
            j = j + 1
        # print "q", q, "q_x", q_x, "q_y", q_y
        quarters = []
        sq = q[0]
        while 1:
            quarters.append(sq)
            if q[1] == sq and start < end or q[1] == sq and start > end and q[0] != q[1]:
                break  # we reach the final end quarter
            elif q[1] == sq and start > end:
                quarters.extend([(sq + 1) % 5, (sq + 2) % 5, (sq + 3) % 5, (sq + 4) % 5])
                break
            else:
                sq = sq + 1
                if sq > 4:
                    sq = 1
        # print "quarters", quarters
        switch = 3 - (2 * radius)
        points = []
        points1 = set()
        points2 = set()
        points3 = set()
        points4 = set()
        #
        x = 0
        y = int(round(radius))
        # first quarter/octant starts clockwise at 12 o'clock
        while x <= y:
            if 1 in quarters:
                if not (1 in q):
                    # add all points of the quarter completely
                    # first quarter first octant
                    points1.add((x, -y))
                    # first quarter 2nd octant
                    points1.add((y, -x))
                else:
                    # start or end point in this quarter?
                    if q[0] == 1:
                        # start point
                        if q_x[0] <= x and q_y[0] >= abs(-y) and len(quarters) > 1 or q_x[0] <= x and q_x[1] >= x:
                            # first quarter first octant
                            points1.add((x, -y))
                            if -y < xy[0][1]:
                                xy[0] = [x, -y]
                            elif -y == xy[0][1]:
                                if x < xy[0][0]:
                                    xy[0] = [x, -y]
                        if q_x[0] <= y and q_y[0] >= x and len(quarters) > 1 or q_x[0] <= y and q_x[1] >= y and q_y[0] >= abs(-x) and q_y[1] <= abs(-x):
                            # first quarter 2nd octant
                            points1.add((y, -x))
                            if -x < xy[0][1]:
                                xy[0] = [y, -x]
                            elif -x == xy[0][1]:
                                if y < xy[0][0]:
                                    xy[0] = [y, -x]
                    if q[1] == 1:
                        # end point
                        if q_x[1] >= x and len(quarters) > 1 or q_x[0] <= x and q_x[1] >= x:
                            # first quarter first octant
                            points1.add((x, -y))
                            if x > xy[1][0]:
                                xy[1] = [x, -y]
                            elif x == xy[1][0]:
                                if -y > xy[1][1]:
                                    xy[1] = [x, -y]
                        if q_x[1] >= y and q_y[1] <= x and len(quarters) > 1 or q_x[0] <= y and q_x[1] >= y and q_y[0] >= abs(-x) and q_y[1] <= abs(-x):
                            # first quarter 2nd octant
                            points1.add((y, -x))
                            if y > xy[1][0]:
                                xy[1] = [y, -x]
                            elif y == xy[1][0]:
                                if -x > xy[1][1]:
                                    xy[1] = [y, -x]
            if 2 in quarters:
                if not (2 in q):
                    # add all points of the quarter completely
                    # second quarter 3rd octant
                    points2.add((y, x))
                    # second quarter 4.octant
                    points2.add((x, y))
                else:
                    # start or end point in this quarter?
                    if q[0] == 2:
                        # start point
                        if q_x[0] >= y and q_y[0] <= x and len(quarters) > 1 or q_x[0] >= y and q_x[1] <= y and q_y[0] <= x and q_y[1] >= x:
                            # second quarter 3rd octant
                            points2.add((y, x))
                            if y > xy[0][0]:
                                xy[0] = [y, x]
                            elif y == xy[0][0]:
                                if x < xy[0][1]:
                                    xy[0] = [y, x]
                        if q_x[0] >= x and q_y[0] <= y and len(quarters) > 1 or q_x[0] >= x and q_x[1] <= x and q_y[0] <= y and q_y[1] >= y:
                            # second quarter 4.octant
                            points2.add((x, y))
                            if x > xy[0][0]:
                                xy[0] = [x, y]
                            elif x == xy[0][0]:
                                if y < xy[0][1]:
                                    xy[0] = [x, y]
                    if q[1] == 2:
                        # end point
                        if q_x[1] <= y and q_y[1] >= x and len(quarters) > 1 or q_x[0] >= y and q_x[1] <= y and q_y[0] <= x and q_y[1] >= x:
                            # second quarter 3rd octant
                            points2.add((y, x))
                            if x > xy[1][1]:
                                xy[1] = [y, x]
                            elif x == xy[1][1]:
                                if y < xy[1][0]:
                                    xy[1] = [y, x]
                        if q_x[1] <= x and q_y[1] >= y and len(quarters) > 1 or q_x[0] >= x and q_x[1] <= x and q_y[0] <= y and q_y[1] >= y:
                            # second quarter 4.octant
                            points2.add((x, y))
                            if y > xy[1][1]:
                                xy[1] = [x, y]
                            elif x == xy[1][1]:
                                if x < xy[1][0]:
                                    xy[1] = [x, y]
            if 3 in quarters:
                if not (3 in q):
                    # add all points of the quarter completely
                    # third quarter 5.octant
                    points3.add((-x, y))
                    # third quarter 6.octant
                    points3.add((-y, x))
                else:
                    # start or end point in this quarter?
                    if q[0] == 3:
                        # start point
                        if q_x[0] <= x and q_y[0] >= abs(y) and len(quarters) > 1 or q_x[0] <= x and q_x[1] >= x:
                            # third quarter 5.octant
                            points3.add((-x, y))
                            if y > xy[0][1]:
                                xy[0] = [-x, y]
                            elif y == xy[0][1]:
                                if -x > xy[0][0]:
                                    xy[0] = [-x, y]
                        if q_x[0] <= y and q_y[0] >= x and len(quarters) > 1 or q_x[0] <= y and q_x[1] >= y and q_y[0] >= x and q_y[1] <= x:
                            # third quarter 6.octant
                            points3.add((-y, x))
                            if x > xy[0][1]:
                                xy[0] = [-y, x]
                            elif x == xy[0][1]:
                                if -y > xy[0][0]:
                                    xy[0] = [-y, x]
                    if q[1] == 3:
                        # end point
                        if q_x[1] >= x and len(quarters) > 1 or q_x[0] <= x and q_x[1] >= x:
                            # third quarter 5.octant
                            points3.add((-x, y))
                            if -x < xy[1][0]:
                                xy[1] = [-x, y]
                            elif -x == xy[1][0]:
                                if y < xy[1][1]:
                                    xy[1] = [-x, y]
                        if q_x[1] >= y and q_y[1] <= x and len(quarters) > 1 or q_x[0] <= y and q_x[1] >= y and q_y[0] >= x and q_y[1] <= x:
                            # third quarter 6.octant
                            points3.add((-y, x))
                            if -y < xy[1][0]:
                                xy[1] = [-y, x]
                            elif -y == xy[1][0]:
                                if x < xy[1][1]:
                                    xy[1] = [-y, x]
            if 4 in quarters:
                if not (4 in q):
                    # add all points of the quarter completely
                    # fourth quarter 7.octant
                    points4.add((-y, -x))
                    # fourth quarter 8.octant
                    points4.add((-x, -y))
                else:
                    # start or end point in this quarter?
                    if q[0] == 4:
                        # start point
                        if q_x[0] >= y and q_y[0] <= x and len(quarters) > 1 or q_x[0] >= y >= q_x[1] and q_y[0] <= x <= q_y[1]:
                            # fourth quarter 7.octant
                            points4.add((-y, -x))
                            if -y < xy[0][0]:
                                xy[0] = [-y, -x]
                            elif -y == xy[0][0]:
                                if -x > xy[0][1]:
                                    xy[0] = [-y, -x]
                        if q_x[0] >= x and q_y[0] <= abs(-y) and len(quarters) > 1 or q_x[0] >= x >= q_x[1] and q_y[0] <= y <= q_y[1]:
                            # fourth quarter 8.octant
                            points4.add((-x, -y))
                            if -x < xy[0][0]:
                                xy[0] = [-x, -y]
                            elif -x == xy[0][0]:
                                if -y > xy[0][1]:
                                    xy[0] = [-x, -y]
                    if q[1] == 4:
                        # end point
                        if q_x[1] <= y and q_y[1] >= x and len(quarters) > 1 or q_x[0] >= y >= q_x[1] and q_y[0] <= x <= q_y[1]:
                            # fourth quarter 7.octant
                            points4.add((-y, -x))
                            if -x < xy[1][1]:
                                xy[1] = [-y, -x]
                            elif -x == xy[1][1]:
                                if -y > xy[1][0]:
                                    xy[1] = [-y, -x]
                        if q_x[1] <= x and q_y[1] >= abs(-y) and len(quarters) > 1 or q_x[0] >= x >= q_x[1] and q_y[0] <= y <= q_y[1]:
                            # fourth quarter 8.octant
                            points4.add((-x, -y))
                            if -y < xy[1][1]:
                                xy[1] = [-x, -y]
                            elif -y == xy[1][1]:
                                if -x > xy[1][0]:
                                    xy[1] = [-x, -y]
            if switch < 0:
                switch = switch + (4 * x) + 6
            else:
                switch = switch + (4 * (x - y)) + 10
                y = y - 1
            x = x + 1
        if 1 in quarters:
            points1_s = list(points1)
            # points1_s.sort() # if for some reason you need them sorted
            points.extend(points1_s)
        if 2 in quarters:
            points2_s = list(points2)
            # points2_s.sort() # if for some reason you need them sorted
            # points2_s.reverse() # # if for some reason you need in right order
            points.extend(points2_s)
        if 3 in quarters:
            points3_s = list(points3)
            # points3_s.sort()
            # points3_s.reverse()
            points.extend(points3_s)
        if 4 in quarters:
            points4_s = list(points4)
            # points4_s.sort()
            points.extend(points4_s)
        return points, xy

    def draw_circle_arc(self, x, y, radius, start, end, clockwise=True):
        points, xy = self.__circle_arc(radius, start, end, clockwise)
        # draw the arc points
        for p in points:
            self.draw_pixel(y + p[0], y + p[1])
        # draw the pie lines
        self.draw_line(x, y, x + xy[0][0], y + xy[0][1])
        self.draw_line(x, y, x + xy[1][0], y + xy[1][1])
        del points

    def char_width(self, char, font: U8GFont):
        return U8GGlyph.width(font, U8GGlyph.glyph_pos(font, ord(char)))

    def draw_char(self, x0: int, y0: int, char, font: U8GFont):
        return font.draw_char(x0, y0, char, self.draw_pixel)

    def draw_string(self, x0: int, y0: int, string: str, font: U8GFont, hspacing: int = 0):
        return font.draw_string(x0, y0, string, self.draw_pixel, hspacing=hspacing)

    def draw_string_exact(self, x0: int, y0: int, string: str, font: U8GFont, hspacing: int = 0):
        return font.draw_string_exact(x0, y0, string, self.draw_pixel, hspacing=hspacing)

    def draw_xbm(self, x0: int, y0: int, xbm):
        """
        Draw xbm image. Image should be converted from original 'xbm'.

        For example, content of file ``mmhg_xbm.py``::

            width = 17
            height = 40
            bits = [ 0x18, 0x70, ... ]

        :param x0: Horizontal position of left-top position of the bitmap
        :param y0: Vertical position of left-top position of the bitmap
        :param xbm: Bitmap
        :return: Tuple (x0, y0, x1, y1) of bitmap boundary
        """
        byte_pos = 0
        bytes_per_row = math.ceil(xbm.width / 8)
        for row_no in range(xbm.height):
            for col_no in range(bytes_per_row):
                byte = xbm.bits[byte_pos]
                for bit_no in range(8):
                    char_col_pos = bit_no + (col_no * 8)
                    if char_col_pos > xbm.width:
                        break
                    if byte >> bit_no & 0x1:
                        self.draw_pixel(x0 + char_col_pos, y0 + row_no)
                byte_pos += 1
        return x0, y0, x0 + xbm.width, y0 + xbm.height

    def del_xbm(self, xbm):
        del xbm.bits
        del xbm.width
        del xbm.height
