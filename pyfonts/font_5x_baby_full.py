# len=1240, width=10, height=10, x_offset=-1, y_offset=-2, cap_A_height=5, start_cap_A=364, start_sm_a=705, enc_start=32, enc_end=190, desc_g=-2, max_ascent=8, min_descent=-2, xascent=6, xdescent=-2
all_chars = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}~¤§©«°±²³µ¹»¼½¾"""
data = [
    0,10,10,255,254,5,1,108,2,193,32,190,254,8,254,6,
    254,0,0,0,2,0,0,1,6,6,3,1,0,128,128,128,
    128,0,128,3,3,3,4,0,4,160,160,160,5,5,5,6,
    0,0,80,248,80,248,80,3,7,7,4,0,255,64,96,128,
    64,32,192,64,5,5,5,6,0,0,200,208,32,88,152,5,
    6,6,6,0,0,64,160,64,160,144,104,1,3,3,2,0,
    4,128,128,128,2,7,7,3,0,255,64,128,128,128,128,128,
    64,2,7,7,3,0,255,128,64,64,64,64,64,128,3,3,
    3,4,0,3,160,64,160,3,3,3,5,1,1,64,224,64,
    2,3,3,3,0,254,192,64,128,3,1,1,4,0,2,224,
    1,1,1,2,0,0,128,3,6,6,4,0,255,32,32,64,
    64,128,128,3,5,5,4,0,0,64,160,160,160,64,2,5,
    5,3,0,0,64,192,64,64,64,4,5,5,5,0,0,96,
    144,32,64,240,4,5,5,5,0,0,224,16,96,16,224,4,
    5,5,5,0,0,144,144,144,112,16,4,5,5,5,0,0,
    240,128,224,16,224,4,5,5,5,0,0,96,128,224,144,96,
    4,5,5,5,0,0,240,16,32,64,128,4,5,5,5,0,
    0,96,144,96,144,96,4,5,5,5,0,0,96,144,112,16,
    96,1,3,3,3,1,0,128,0,128,2,5,5,3,0,254,
    64,0,64,64,128,4,5,5,5,0,0,16,96,128,96,16,
    3,3,3,4,0,1,224,0,224,4,5,5,5,0,0,128,
    96,16,96,128,4,6,6,5,0,0,96,144,32,64,0,64,
    5,6,6,6,0,0,112,136,168,176,128,112,4,5,5,5,
    0,0,96,144,144,240,144,4,5,5,5,0,0,224,144,224,
    144,224,4,5,5,5,0,0,96,144,128,144,96,4,5,5,
    5,0,0,224,144,144,144,224,4,5,5,5,0,0,240,128,
    224,128,240,4,5,5,5,0,0,240,128,224,128,128,4,5,
    5,5,0,0,96,128,176,144,96,4,5,5,5,0,0,144,
    144,240,144,144,3,5,5,4,0,0,224,64,64,64,224,4,
    5,5,5,0,0,112,16,16,144,96,4,5,5,5,0,0,
    144,144,144,224,144,3,5,5,4,0,0,128,128,128,128,224,
    5,5,5,6,0,0,216,168,168,168,136,4,5,5,5,0,
    0,144,144,208,176,144,4,5,5,5,0,0,96,144,144,144,
    96,4,5,5,5,0,0,224,144,144,224,128,4,5,5,5,
    0,0,96,144,144,80,224,4,5,5,5,0,0,224,144,144,
    224,144,3,5,5,4,0,0,96,128,64,32,192,3,5,5,
    4,0,0,224,64,64,64,64,4,5,5,5,0,0,144,144,
    144,144,96,5,5,5,6,0,0,136,80,80,80,32,5,5,
    5,6,0,0,136,136,136,168,80,4,5,5,5,0,0,144,
    144,144,96,144,4,6,6,5,0,255,144,144,144,112,16,96,
    4,5,5,5,0,0,240,32,64,128,240,2,7,7,3,0,
    255,192,128,128,128,128,128,192,3,6,6,4,0,255,128,128,
    64,64,32,32,2,7,7,3,0,255,192,64,64,64,64,64,
    192,3,2,2,4,0,4,64,160,4,1,1,5,0,255,240,
    255,4,4,4,5,0,0,96,144,144,112,4,5,5,5,0,
    0,128,224,144,144,96,3,4,4,4,0,0,96,128,128,96,
    4,5,5,5,0,0,16,112,144,144,96,4,4,4,5,0,
    0,96,144,160,112,4,5,5,5,0,0,96,144,128,192,128,
    4,6,6,5,0,254,96,144,144,112,16,96,4,5,5,5,
    0,0,128,224,144,144,144,1,5,5,2,0,0,128,0,128,
    128,128,3,7,7,3,255,254,32,0,32,32,32,32,192,3,
    5,5,4,0,0,128,160,192,160,160,1,5,5,2,0,0,
    128,128,128,128,128,5,4,4,6,0,0,208,168,168,136,4,
    4,4,5,0,0,224,144,144,144,4,4,4,5,0,0,96,
    144,144,96,4,6,6,5,0,254,96,144,144,224,128,128,4,
    6,6,5,0,254,96,144,144,112,16,16,4,4,4,5,0,
    0,224,144,128,128,4,4,4,5,0,0,112,64,32,224,3,
    5,5,4,0,0,64,224,64,64,64,4,4,4,5,0,0,
    144,144,144,112,4,4,4,5,0,0,144,144,144,96,5,4,
    4,6,0,0,136,168,168,80,4,4,4,5,0,0,144,144,
    96,144,4,6,6,5,0,254,144,144,144,112,16,96,4,4,
    4,5,0,0,240,32,64,240,3,7,7,4,0,255,32,64,
    64,128,64,64,32,1,7,7,2,0,255,128,128,128,128,128,
    128,128,3,7,7,4,0,255,128,64,64,32,64,64,128,5,
    3,3,6,0,1,64,168,16,255,255,255,255,255,255,255,255,
    255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
    255,255,255,255,255,255,255,255,255,255,255,255,255,4,4,4,
    5,0,1,240,144,144,240,255,255,4,7,7,5,0,255,112,
    128,96,144,96,16,224,255,7,7,7,8,0,255,56,68,154,
    162,154,68,56,255,4,3,3,5,0,1,80,160,80,255,255,
    255,255,3,3,3,4,0,4,64,160,64,3,5,5,4,0,
    0,64,224,64,0,224,3,4,4,4,0,4,192,32,64,224,
    3,4,4,4,0,4,224,32,96,224,255,5,6,6,6,0,
    254,144,144,144,248,128,128,255,255,255,3,4,4,4,0,4,
    64,192,64,224,255,4,3,3,5,0,1,160,80,160,7,6,
    6,8,0,0,136,144,160,42,78,130,7,6,6,8,0,0,
    136,144,164,42,68,142,9,6,12,10,0,0,226,0,100,0,
    232,0,10,128,19,128,32,128
]
