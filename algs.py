
def alg10 (a, b, c, d, x):
    if c + d == 0 or a + b * x**3 ==0:
        return "Error division to 0"
    else:
        return (((a+b*x)**2)/(c+d)) + (c + d) / (a + b*x)**3


def alg20 (x, y, z):
    if x > 0:
        if z != 0:
            return (123 * x ** 3 + 124 * y ** 4) / 125 * z ** 5
        else:
            return "Error division to 0"
    elif y > 0:
        if x != 0:
            return (123 * y ** 3 + 124 * z ** 4) / 125 * x ** 5
        else:
            return "Error division to 0"
    elif z > 0:
        if x != 0:
            return (123 * z ** 3 + 124 * y ** 4) / 125 * x ** 5
        else:
            return "Error division to 0"
    else:
        return "Underfined, more then one variable bigger than 0"

def alg30 (a, b, n):
    f = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            f += a ** i + b ** j
    return f


