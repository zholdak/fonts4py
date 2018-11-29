# Code generated by font-to-py.py.
# Font: DejaVuSans.ttf Char set: -.0123456789
version = '0.26'

def height():
    return 7

def max_width():
    return 6

def hmap():
    return True

def reverse():
    return False

def monospaced():
    return False

def min_ch():
    return 45

def max_ch():
    return 63


def glyphs():
    for c in """?-.0123456789""":
        yield c, get_ch(c)

_font =\
b'\x05\x00\xf0\x10\x20\x40\x40\x00\x40\x03\x00\x00\x00\x00\x00\xc0'\
b'\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x80\x06\x00\x60\x90\x90'\
b'\x90\x90\x90\x60\x06\x00\xc0\x40\x40\x40\x40\x40\xe0\x06\x00\x60'\
b'\x90\x10\x20\x40\x80\xf0\x06\x00\x60\x90\x10\x60\x10\x10\xe0\x06'\
b'\x00\x10\x30\x50\x50\x90\xf8\x10\x06\x00\xf0\x80\x80\xe0\x10\x10'\
b'\xe0\x06\x00\x70\xc0\x80\xe0\x90\x90\x60\x06\x00\xf0\x10\x20\x20'\
b'\x20\x40\x40\x06\x00\x60\x90\x90\x60\x90\x90\x60\x06\x00\x60\x90'\
b'\x90\xf0\x10\x30\xe0'

_index =\
b'\x00\x00\x09\x00\x09\x00\x12\x00\x12\x00\x1b\x00\x00\x00\x09\x00'\
b'\x1b\x00\x24\x00\x24\x00\x2d\x00\x2d\x00\x36\x00\x36\x00\x3f\x00'\
b'\x3f\x00\x48\x00\x48\x00\x51\x00\x51\x00\x5a\x00\x5a\x00\x63\x00'\
b'\x63\x00\x6c\x00\x6c\x00\x75\x00\x00\x00\x09\x00\x00\x00\x09\x00'\
b'\x00\x00\x09\x00\x00\x00\x09\x00\x00\x00\x09\x00\x00\x00\x09\x00'\

_mvfont = memoryview(_font)

def get_ch(ch):
    ordch = ord(ch)
    ordch = ordch + 1 if ordch >= 45 and ordch <= 63 else 63
    idx_offs = 4 * (ordch - 45)
    offset = int.from_bytes(_index[idx_offs : idx_offs + 2], 'little')
    next_offs = int.from_bytes(_index[idx_offs + 2 : idx_offs + 4], 'little')
    width = int.from_bytes(_font[offset:offset + 2], 'little')
    return _mvfont[offset + 2:next_offs], 7, width
 