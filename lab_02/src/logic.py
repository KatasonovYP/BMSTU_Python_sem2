from src.methods.half import half
from sympy import diff
from math import *

def make_func(a):
    return lambda x: eval(a)


def find_roots(func, a, b, h, Nmax, eps):
    print(a, b)
    f = make_func(func)
    error_code = None
    cnt = 0
    x = a
    result = []
    points = [[], []]
    while x < b:
        if f(x) * f(x + h) <= 0:
            x, cnt = half(f, x, x + h, eps, Nmax)
            result.append((
                f'[{x:.1f}; {x + h:.1f}]', 
                f'{x:.1f}', 
                f'{f(x):.1f}', 
                str(cnt), 
                str(error_code)
            ))
        points[0].append(x)
        points[1].append(f(x))
        x += h
    return {'roots': result, 'points': points}


def calculate_result(func: str, a: float, b: float, h: float, Nmax: int, eps: float):
    df = f'{diff(func)}'
    ddf = f'{diff(df)}'
    return {
        'f': find_roots(func, a, b, h, Nmax, eps),
        'df': find_roots(df, a, b, h, Nmax, eps),
        'ddf': find_roots(ddf, a, b, h, Nmax, eps)
    }




