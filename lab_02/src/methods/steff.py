from typing import Callable, Iterator
Func = Callable[[float], float]

def g(f: Func, x: float, fx: float) -> Func:
    """First-order divided difference function.

    Arguments:
        f: Function input to g
        x: Point at which to evaluate g
        fx: Function f evaluated at x 
    """
    return lambda x: f(x + fx) / fx - 1

def steff(f: Func, x: float) -> Iterator[float]:
    """Steffenson algorithm for finding roots.

    This recursive generator yields the x_{n+1} value first then, when the generator iterates,
    it yields x_{n+2} from the next level of recursion.

    Arguments:
        f: Function whose root we are searching for
        x: Starting value upon first call, each level n that the function recurses x is x_n
    """
    while True:    
        fx = f(x)
        gx = g(f, x, fx)(x)
        if gx == 0:
            break
        else:
            x = x - fx / gx     # Update to x_{n+1}
            yield x         # Yield value
