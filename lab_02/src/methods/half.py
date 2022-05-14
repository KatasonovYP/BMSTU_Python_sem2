def half(func, a, b, eps, Nmax):
    cnt = 0
    x = a
    while abs(b - a) > eps and cnt < Nmax:
        cnt += 1
        x = a + (b - a) / 2
        if func(a) * func(x) < 0:
            b = x
        else:
            a = x
    return x, cnt