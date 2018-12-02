# len=1497, width=12, height=19, x_offset=-1, y_offset=-5, cap_A_height=8, start_cap_A=438, start_sm_a=883, enc_start=32, enc_end=190, desc_g=-2, max_ascent=11, min_descent=-2, xascent=8, xdescent=-2
all_chars = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}~¤§©«°±²³µ¹»¼½¾"""
data = [
    0,12,19,255,251,8,1,182,3,115,32,190,254,11,254,8,
    254,0,0,0,3,0,1,2,8,8,4,1,0,192,192,192,
    192,128,128,0,192,3,3,3,5,1,5,160,160,160,7,7,
    7,6,255,0,40,40,126,40,252,80,80,5,10,10,6,0,
    255,32,112,168,224,112,56,40,168,112,32,7,8,8,8,0,
    0,98,180,104,16,16,44,86,140,7,8,8,8,0,0,112,
    216,216,112,222,204,220,118,1,3,3,3,1,5,128,128,128,
    3,10,10,4,0,254,32,96,64,192,192,192,192,64,96,32,
    3,10,10,4,0,254,128,192,64,96,96,96,96,64,192,128,
    3,3,3,4,0,5,160,64,160,6,5,5,6,0,1,48,
    48,252,48,48,2,4,4,3,0,254,192,192,64,128,4,1,
    1,5,0,3,240,2,2,2,3,0,0,192,192,4,8,8,
    4,0,0,16,16,32,32,64,64,128,128,5,8,8,6,0,
    0,112,216,216,216,216,216,216,112,3,8,8,6,1,0,96,
    224,96,96,96,96,96,96,5,8,8,6,0,0,112,216,24,
    24,48,96,192,248,5,8,8,6,0,0,112,216,24,48,24,
    24,216,112,6,8,8,6,0,0,8,24,56,88,152,252,24,
    24,5,8,8,6,0,0,248,192,192,240,24,152,216,112,5,
    8,8,6,0,0,112,216,192,240,216,216,216,112,5,8,8,
    6,0,0,248,24,24,48,48,96,96,96,5,8,8,6,0,
    0,112,216,216,112,216,216,216,112,5,8,8,6,0,0,112,
    216,216,216,120,24,216,112,2,6,6,3,0,0,192,192,0,
    0,192,192,2,8,8,3,0,254,192,192,0,0,192,192,64,
    128,4,5,5,5,0,1,48,96,192,96,48,5,3,3,6,
    0,2,248,0,248,4,5,5,5,0,1,192,96,48,96,192,
    5,8,8,6,0,0,112,216,24,48,96,96,0,96,10,9,
    18,11,0,255,31,0,96,128,77,64,146,64,162,64,164,128,
    155,0,64,0,62,0,7,8,8,8,0,0,56,56,108,108,
    108,254,198,198,6,8,8,7,0,0,248,204,204,248,204,204,
    204,248,7,8,8,8,0,0,60,102,194,192,192,194,102,60,
    6,8,8,7,0,0,240,216,204,204,204,204,216,240,5,8,
    8,6,0,0,248,192,192,248,192,192,192,248,5,8,8,6,
    0,0,248,192,192,240,192,192,192,192,7,8,8,8,0,0,
    60,102,194,192,206,198,102,58,6,8,8,7,0,0,204,204,
    204,252,204,204,204,204,2,8,8,3,0,0,192,192,192,192,
    192,192,192,192,5,8,8,6,0,0,24,24,24,24,24,24,
    216,112,7,8,8,7,0,0,204,216,240,224,240,216,204,198,
    5,8,8,6,0,0,192,192,192,192,192,192,192,248,9,8,
    16,10,0,0,193,128,227,128,227,128,247,128,213,128,221,128,
    201,128,201,128,7,8,8,8,0,0,198,230,230,214,214,206,
    206,198,7,8,8,8,0,0,56,108,198,198,198,198,108,56,
    6,8,8,7,0,0,248,204,204,204,248,192,192,192,7,9,
    9,8,0,255,56,108,198,198,198,214,108,60,2,6,8,8,
    7,0,0,248,204,204,204,248,204,204,204,6,8,8,7,0,
    0,120,204,224,120,28,140,204,120,6,8,8,7,0,0,252,
    48,48,48,48,48,48,48,6,8,8,7,0,0,204,204,204,
    204,204,204,204,120,7,8,8,8,0,0,198,198,108,108,108,
    56,56,16,10,8,16,11,0,0,204,192,204,192,204,192,109,
    128,109,128,127,128,51,0,51,0,7,8,8,8,0,0,198,
    198,108,56,56,108,198,198,8,8,8,9,0,0,195,195,102,
    102,60,24,24,24,6,8,8,7,0,0,252,12,24,48,112,
    96,192,252,3,10,10,4,0,254,224,192,192,192,192,192,192,
    192,192,224,4,8,8,4,0,0,128,128,64,64,32,32,16,
    16,3,10,10,4,0,254,224,96,96,96,96,96,96,96,96,
    224,4,4,4,5,0,4,96,240,144,144,6,1,1,6,0,
    254,252,255,6,6,6,6,0,0,112,152,120,216,216,108,5,
    8,8,6,0,0,192,192,240,216,216,216,216,240,4,6,6,
    5,0,0,112,208,192,192,208,112,5,8,8,6,0,0,24,
    24,120,216,216,216,216,120,5,6,6,6,0,0,112,216,248,
    192,216,112,5,8,8,4,255,0,56,96,240,96,96,96,96,
    96,5,8,8,6,0,254,104,216,216,216,216,120,24,112,5,
    8,8,6,0,0,192,192,240,216,216,216,216,216,2,8,8,
    3,0,0,192,0,192,192,192,192,192,192,3,10,10,3,255,
    254,96,0,96,96,96,96,96,96,96,192,6,8,8,6,0,
    0,192,192,216,240,224,240,216,204,2,8,8,3,0,0,192,
    192,192,192,192,192,192,192,8,6,6,9,0,0,182,219,219,
    219,219,219,5,6,6,6,0,0,176,216,216,216,216,216,5,
    6,6,6,0,0,112,216,216,216,216,112,5,8,8,6,0,
    254,176,216,216,216,216,240,192,192,5,8,8,6,0,254,104,
    216,216,216,216,120,24,24,4,6,6,4,0,0,176,224,192,
    192,192,192,5,6,6,6,0,0,112,216,112,24,216,112,4,
    8,8,4,255,0,96,96,240,96,96,96,96,48,5,6,6,
    6,0,0,216,216,216,216,216,104,5,6,6,6,0,0,216,
    216,216,80,112,32,7,6,6,8,0,0,214,214,214,108,108,
    108,6,6,6,7,0,0,204,120,48,120,204,204,5,8,8,
    6,0,254,216,216,216,216,120,48,48,96,5,6,6,6,0,
    0,248,24,48,96,192,248,4,10,10,5,0,254,48,96,96,
    96,192,96,96,96,96,48,1,10,10,3,1,254,128,128,128,
    128,128,128,128,128,128,128,4,10,10,5,0,254,192,96,96,
    96,48,96,96,96,96,192,5,2,2,6,0,3,104,176,255,
    255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
    255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
    255,255,255,255,6,6,6,6,0,1,132,120,72,72,120,132,
    255,255,5,10,10,6,0,254,112,200,224,112,152,200,112,56,
    152,112,255,8,8,8,10,1,0,60,66,153,165,161,157,66,
    60,255,6,3,3,7,0,1,108,216,108,255,255,255,255,3,
    3,3,4,0,5,96,160,192,6,7,7,6,0,0,48,48,
    252,48,48,0,252,3,4,4,3,0,4,96,160,64,224,3,
    4,4,3,0,4,224,64,32,192,255,5,8,8,6,0,254,
    216,216,216,216,216,232,192,192,255,255,255,2,4,4,3,0,
    4,64,192,64,64,255,6,3,3,7,0,1,216,108,216,8,
    8,8,9,0,0,68,196,72,72,18,38,47,66,7,8,8,
    9,0,0,68,196,72,72,22,42,36,78,8,8,8,9,0,
    0,228,68,40,200,18,38,47,66
]
