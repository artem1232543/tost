def trapezium_area(a, b, h):
    if a <= 0 or b <= 0 or h <= 0:
        raise ValueError("Длины оснований и высота должны быть больше нуля")
    return ((a + b) / 2) * h
