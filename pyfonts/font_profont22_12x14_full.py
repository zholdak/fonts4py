# len=3155, width=12, height=21, x_offset=0, y_offset=-4, cap_A_height=14, start_cap_A=885, start_sm_a=1896, enc_start=32, enc_end=190, desc_g=-4, max_ascent=18, min_descent=-4, xascent=16, xdescent=-4
all_chars = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_abcdefghijklmnopqrstuvwxyz{|}~¤§©«°±²³µ¹»¼½¾"""
data = [
    0,12,21,0,252,14,3,117,7,104,32,190,252,18,252,16,
    252,0,0,0,12,0,0,2,14,14,12,4,0,192,192,192,
    192,192,192,192,192,192,192,0,0,192,192,6,6,6,12,2,
    10,204,204,204,204,204,204,10,10,20,12,0,4,51,0,51,
    0,255,192,255,192,51,0,51,0,255,192,255,192,51,0,51,
    0,10,18,36,12,0,254,12,0,12,0,63,0,127,128,237,
    192,204,192,204,0,236,0,127,0,63,128,13,192,12,192,204,
    192,237,192,127,128,63,0,12,0,12,0,10,14,28,12,0,
    0,63,192,127,192,204,192,205,192,207,128,207,0,127,0,63,
    128,60,192,124,192,236,192,204,192,199,128,195,0,10,14,28,
    12,0,0,62,0,127,0,227,0,199,0,206,0,252,0,120,
    0,120,0,252,192,207,192,199,128,231,128,127,192,60,192,2,
    6,6,12,4,10,192,192,192,192,192,192,6,18,18,12,2,
    254,12,28,56,112,224,192,192,192,192,192,192,192,192,224,112,
    56,28,12,6,18,18,12,2,254,192,224,112,56,28,12,12,
    12,12,12,12,12,12,28,56,112,224,192,10,10,20,12,0,
    4,12,0,12,0,204,192,255,192,63,0,63,0,255,192,204,
    192,12,0,12,0,10,10,20,12,0,2,12,0,12,0,12,
    0,12,0,255,192,255,192,12,0,12,0,12,0,12,0,5,
    9,9,12,2,252,48,120,120,56,24,56,112,224,64,6,2,
    2,12,2,6,252,252,4,4,4,12,3,1,96,240,240,96,
    11,20,40,12,0,252,0,96,0,96,0,192,0,192,1,128,
    1,128,3,0,3,0,6,0,6,0,12,0,12,0,24,0,
    24,0,48,0,48,0,96,0,96,0,192,0,192,0,10,14,
    28,12,0,0,63,0,127,128,225,192,193,192,195,192,199,192,
    206,192,220,192,248,192,240,192,224,192,225,192,127,128,63,0,
    10,14,28,12,0,0,12,0,12,0,124,0,124,0,12,0,
    12,0,12,0,12,0,12,0,12,0,12,0,12,0,255,192,
    255,192,10,14,28,12,0,0,63,0,127,128,225,192,192,192,
    0,192,1,192,3,128,7,0,14,0,28,0,56,0,112,0,
    255,192,255,192,10,14,28,12,0,0,63,0,127,128,225,192,
    192,192,0,192,1,128,15,0,15,128,1,192,0,192,192,192,
    225,192,127,128,63,0,10,14,28,12,0,0,3,0,7,0,
    15,0,31,0,59,0,115,0,227,0,195,0,255,192,255,192,
    3,0,3,0,15,192,15,192,10,14,28,12,0,0,255,192,
    255,192,192,0,192,0,255,0,255,128,1,192,0,192,0,192,
    0,192,192,192,225,192,127,128,63,0,10,14,28,12,0,0,
    63,0,127,0,224,0,192,0,255,0,255,128,193,192,192,192,
    192,192,192,192,192,192,225,192,127,128,63,0,10,14,28,12,
    0,0,255,192,255,192,0,192,0,192,0,192,1,192,3,128,
    7,0,14,0,12,0,12,0,12,0,12,0,12,0,10,14,
    28,12,0,0,63,0,127,128,225,192,192,192,192,192,97,128,
    63,0,127,128,225,192,192,192,192,192,225,192,127,128,63,0,
    10,14,28,12,0,0,63,0,127,128,225,192,192,192,192,192,
    192,192,192,192,224,192,127,192,63,192,0,192,1,192,63,128,
    63,0,4,10,10,12,3,1,96,240,240,96,0,0,96,240,
    240,96,5,15,15,12,2,252,48,120,120,48,0,0,48,120,
    120,56,24,56,112,224,64,8,14,14,12,2,0,3,7,14,
    28,56,112,224,224,112,56,28,14,7,3,10,6,12,12,0,
    4,255,192,255,192,0,0,0,0,255,192,255,192,8,14,14,
    12,2,0,192,224,112,56,28,14,7,7,14,28,56,112,224,
    192,10,14,28,12,0,0,63,0,127,128,225,192,192,192,0,
    192,1,192,3,128,7,0,14,0,12,0,0,0,0,0,12,
    0,12,0,10,14,28,12,0,0,63,0,127,128,225,192,192,
    192,199,192,207,192,204,192,204,192,207,192,199,128,192,0,224,
    0,127,192,63,192,10,14,28,12,0,0,12,0,30,0,30,
    0,51,0,51,0,97,128,97,128,192,192,255,192,255,192,192,
    192,192,192,192,192,192,192,10,14,28,12,0,0,255,0,255,
    128,193,192,192,192,192,192,193,128,255,0,255,128,193,192,192,
    192,192,192,193,192,255,128,255,0,10,14,28,12,0,0,63,
    0,127,128,225,192,192,192,192,0,192,0,192,0,192,0,192,
    0,192,0,192,192,225,192,127,128,63,0,10,14,28,12,0,
    0,255,0,255,128,193,192,192,192,192,192,192,192,192,192,192,
    192,192,192,192,192,192,192,193,192,255,128,255,0,10,14,28,
    12,0,0,255,192,255,192,192,0,192,0,192,0,192,0,255,
    0,255,0,192,0,192,0,192,0,192,0,255,192,255,192,10,
    14,28,12,0,0,255,192,255,192,192,0,192,0,192,0,192,
    0,255,0,255,0,192,0,192,0,192,0,192,0,192,0,192,
    0,10,14,28,12,0,0,63,0,127,128,225,192,192,192,192,
    0,192,0,195,192,195,192,192,192,192,192,192,192,225,192,127,
    128,63,0,10,14,28,12,0,0,192,192,192,192,192,192,192,
    192,192,192,192,192,255,192,255,192,192,192,192,192,192,192,192,
    192,192,192,192,192,10,14,28,12,0,0,255,192,255,192,12,
    0,12,0,12,0,12,0,12,0,12,0,12,0,12,0,12,
    0,12,0,255,192,255,192,10,14,28,12,0,0,0,192,0,
    192,0,192,0,192,0,192,0,192,0,192,0,192,192,192,192,
    192,192,192,225,192,127,128,63,0,10,14,28,12,0,0,193,
    192,195,128,199,0,206,0,220,0,248,0,240,0,248,0,220,
    0,206,0,199,0,195,128,193,192,192,192,10,14,28,12,0,
    0,192,0,192,0,192,0,192,0,192,0,192,0,192,0,192,
    0,192,0,192,0,192,0,192,0,255,192,255,192,10,14,28,
    12,0,0,192,192,225,192,243,192,255,192,222,192,204,192,204,
    192,204,192,192,192,192,192,192,192,192,192,192,192,192,192,10,
    14,28,12,0,0,192,192,224,192,240,192,248,192,220,192,206,
    192,199,192,195,192,193,192,192,192,192,192,192,192,192,192,192,
    192,10,14,28,12,0,0,63,0,127,128,225,192,192,192,192,
    192,192,192,192,192,192,192,192,192,192,192,192,192,225,192,127,
    128,63,0,10,14,28,12,0,0,255,0,255,128,193,192,192,
    192,192,192,193,192,255,128,255,0,192,0,192,0,192,0,192,
    0,192,0,192,0,10,16,32,12,0,254,63,0,127,128,225,
    192,192,192,192,192,192,192,192,192,192,192,192,192,192,192,204,
    192,239,192,127,128,63,128,1,192,0,192,10,14,28,12,0,
    0,255,0,255,128,193,192,192,192,192,192,193,128,255,0,255,
    128,193,192,192,192,192,192,192,192,192,192,192,192,10,14,28,
    12,0,0,63,0,127,128,225,192,192,192,192,0,224,0,127,
    0,63,128,1,192,0,192,192,192,225,192,127,128,63,0,10,
    14,28,12,0,0,255,192,255,192,12,0,12,0,12,0,12,
    0,12,0,12,0,12,0,12,0,12,0,12,0,12,0,12,
    0,10,14,28,12,0,0,192,192,192,192,192,192,192,192,192,
    192,192,192,192,192,192,192,192,192,192,192,192,192,225,192,127,
    128,63,0,10,14,28,12,0,0,192,192,192,192,192,192,192,
    192,192,192,192,192,97,128,97,128,51,0,51,0,30,0,30,
    0,12,0,12,0,10,14,28,12,0,0,192,192,192,192,192,
    192,192,192,192,192,192,192,204,192,204,192,204,192,222,192,255,
    192,243,192,225,192,192,192,10,14,28,12,0,0,192,192,192,
    192,192,192,225,192,115,128,63,0,30,0,30,0,63,0,115,
    128,225,192,192,192,192,192,192,192,10,14,28,12,0,0,192,
    192,192,192,192,192,192,192,192,192,225,192,115,128,63,0,30,
    0,12,0,12,0,12,0,12,0,12,0,10,14,28,12,0,
    0,255,192,255,192,0,192,1,192,3,128,7,0,14,0,28,
    0,56,0,112,0,224,0,192,0,255,192,255,192,4,18,18,
    12,4,254,240,240,192,192,192,192,192,192,192,192,192,192,192,
    192,192,192,240,240,11,20,40,12,1,252,192,0,192,0,96,
    0,96,0,48,0,48,0,24,0,24,0,12,0,12,0,6,
    0,6,0,3,0,3,0,1,128,1,128,0,192,0,192,0,
    96,0,96,4,18,18,12,2,254,240,240,48,48,48,48,48,
    48,48,48,48,48,48,48,48,48,240,240,10,6,12,12,0,
    8,12,0,30,0,63,0,115,128,225,192,64,128,12,2,4,
    12,0,252,255,240,255,240,255,10,10,20,12,0,0,63,192,
    127,192,224,192,192,192,192,192,193,192,195,192,231,192,126,192,
    60,192,10,14,28,12,0,0,192,0,192,0,192,0,192,0,
    255,0,255,128,193,192,192,192,192,192,192,192,192,192,193,192,
    255,128,255,0,10,10,20,12,0,0,63,0,127,128,225,192,
    192,192,192,0,192,0,192,0,224,0,127,192,63,192,10,14,
    28,12,0,0,0,192,0,192,0,192,0,192,63,192,127,192,
    224,192,192,192,192,192,192,192,192,192,224,192,127,192,63,192,
    10,10,20,12,0,0,63,0,127,128,225,192,192,192,255,192,
    255,192,192,0,224,0,127,192,63,192,8,14,14,12,2,0,
    15,31,56,48,252,252,48,48,48,48,48,48,48,48,10,14,
    28,12,0,252,63,192,127,192,224,192,192,192,192,192,192,192,
    192,192,224,192,127,192,63,192,0,192,1,192,63,128,63,0,
    10,14,28,12,0,0,192,0,192,0,192,0,192,0,255,0,
    255,128,193,192,192,192,192,192,192,192,192,192,192,192,192,192,
    192,192,6,14,14,12,2,0,48,48,0,0,240,240,48,48,
    48,48,48,48,252,252,6,18,18,12,0,252,12,12,0,0,
    60,60,12,12,12,12,12,12,12,12,12,28,248,240,10,14,
    28,12,0,0,192,0,192,0,192,0,192,0,195,128,199,0,
    206,0,220,0,252,0,254,0,231,0,195,128,193,192,192,192,
    6,14,14,12,2,0,240,240,48,48,48,48,48,48,48,48,
    48,48,252,252,10,10,20,12,0,0,255,0,255,128,205,192,
    204,192,204,192,204,192,204,192,204,192,204,192,204,192,10,10,
    20,12,0,0,207,0,223,128,249,192,240,192,224,192,192,192,
    192,192,192,192,192,192,192,192,10,10,20,12,0,0,63,0,
    127,128,225,192,192,192,192,192,192,192,192,192,225,192,127,128,
    63,0,10,14,28,12,0,252,255,0,255,128,193,192,192,192,
    192,192,192,192,192,192,193,192,255,128,255,0,192,0,192,0,
    192,0,192,0,10,14,28,12,0,252,63,192,127,192,224,192,
    192,192,192,192,192,192,192,192,224,192,127,192,63,192,0,192,
    0,192,0,192,0,192,10,10,20,12,0,0,207,0,223,128,
    249,192,240,192,224,0,192,0,192,0,192,0,192,0,192,0,
    10,10,20,12,0,0,63,192,127,192,192,0,192,0,127,0,
    63,128,0,192,0,192,255,128,255,0,8,14,14,12,2,0,
    48,48,48,48,252,252,48,48,48,48,48,56,31,15,10,10,
    20,12,0,0,192,192,192,192,192,192,192,192,192,192,193,192,
    195,192,231,192,126,192,60,192,10,10,20,12,0,0,192,192,
    192,192,192,192,97,128,97,128,51,128,51,0,30,0,30,0,
    12,0,10,10,20,12,0,0,204,192,204,192,204,192,204,192,
    204,192,204,192,204,192,204,192,127,128,51,0,10,10,20,12,
    0,0,192,192,225,192,115,128,63,0,30,0,30,0,63,0,
    115,128,225,192,192,192,10,14,28,12,0,252,192,192,192,192,
    192,192,192,192,192,192,192,192,192,192,224,192,127,192,63,192,
    0,192,1,192,63,128,63,0,10,10,20,12,0,0,255,192,
    255,192,3,128,7,0,14,0,28,0,56,0,112,0,255,192,
    255,192,6,22,22,12,2,252,12,28,56,48,48,48,48,48,
    48,112,224,224,112,48,48,48,48,48,48,56,28,12,2,18,
    18,12,4,254,192,192,192,192,192,192,192,192,192,192,192,192,
    192,192,192,192,192,192,6,22,22,12,2,252,192,224,112,48,
    48,48,48,48,48,56,28,28,56,48,48,48,48,48,48,112,
    224,192,10,4,8,12,0,6,48,192,124,192,207,128,195,0,
    255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
    255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,
    255,255,255,255,255,10,10,20,12,0,0,64,128,225,192,127,
    128,63,0,51,0,51,0,63,0,127,128,225,192,64,128,255,
    255,10,20,40,12,0,254,31,0,127,128,97,192,224,192,112,
    192,56,192,220,0,206,0,199,0,227,128,113,192,56,192,28,
    192,14,192,199,0,195,128,193,192,225,128,127,128,62,0,255,
    10,14,28,12,0,0,120,0,254,0,135,0,1,128,61,128,
    124,192,192,192,192,192,124,192,61,128,1,128,135,0,254,0,
    120,0,255,10,10,20,12,0,255,48,192,113,192,97,128,227,
    128,195,0,195,0,227,128,97,128,113,192,48,192,255,255,255,
    255,8,8,8,12,2,8,60,126,231,195,195,231,126,60,10,
    12,24,12,0,0,12,0,12,0,12,0,12,0,255,192,255,
    192,12,0,12,0,12,0,12,0,255,192,255,192,5,7,7,
    12,3,11,112,136,8,16,32,64,248,5,7,7,12,3,11,
    112,136,8,48,8,136,112,255,10,14,28,12,0,252,195,0,
    195,0,195,0,195,0,195,0,195,0,195,0,199,128,255,192,
    252,192,192,0,192,0,192,0,192,0,255,255,255,5,7,7,
    12,3,11,32,224,32,32,32,32,248,255,10,10,20,12,0,
    255,195,0,227,128,97,128,113,192,48,192,48,192,113,192,97,
    128,227,128,195,0,12,18,36,12,0,0,16,0,112,0,16,
    0,16,0,16,16,16,32,124,64,0,128,1,0,2,0,4,
    0,8,64,16,192,33,64,66,64,131,224,0,64,0,224,12,
    18,36,12,0,0,16,0,112,0,16,0,16,0,16,16,16,
    32,124,64,0,128,1,0,2,0,4,0,9,192,18,32,32,
    32,64,64,128,128,1,0,3,224,12,18,36,12,0,0,56,
    0,68,0,4,0,24,0,4,16,68,32,56,64,0,128,1,
    0,2,0,4,0,8,64,16,192,33,64,66,64,131,224,0,
    64,0,224
]
