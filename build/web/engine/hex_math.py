import math

HEX_SIZE = 40

def hex_to_pixel(q, r):
    x = HEX_SIZE * (3/2 * q)
    y = HEX_SIZE * (math.sqrt(3) * (r + q / 2))
    return x, y

def pixel_to_hex(x, y):
    q = (2/3 * x) / HEX_SIZE
    r = (-1/3 * x + math.sqrt(3)/3 * y) / HEX_SIZE
    return round(q), round(r)
