from math import sqrt


def line_to_rectangle(p1, p2, thickness):
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    length = sqrt(dx ** 2 + dy ** 2)

    dx /= length
    dy /= length

    px = 0.5 * thickness * -dy
    py = 0.5 * thickness * dx

    ux = thickness * 0.5 * dx
    uy = thickness * 0.5 * dy

    return [
        (x1 + px - ux, y1 + py - uy),
        (x2 + px + ux, y2 + py + uy),
        (x2 - px + ux, y2 - py + uy),
        (x1 - px - ux, y1 - py - uy),
    ]
