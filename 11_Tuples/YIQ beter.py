def yiq(rgb):
    r, g, b = rgb

    y = (0.299 * r) + (0.587 * g) + (0.114 * b)
    i = (0.596 * r) + (-0.274 * g) + (-0.322 * b)
    q = (0.211 * r) + (-0.523 * g) + (0.312 * b)

    return round(y, 4), round(i, 4), round(q, 4)
