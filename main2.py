def triangle_area_base_height(base, height):
    if base < 0 or height < 0:
        raise ValueError("Основание и высота должны быть неотрицательными")
    return 0.5 * base * height
