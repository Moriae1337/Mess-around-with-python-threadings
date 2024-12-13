import math
def taylor_exp(x, n):
    """Compute e^x using the Taylor series expansion."""
    return (x**n) / math.factorial(n)

def taylor_sin(x, n):
    """Compute sin(x) using the Taylor series expansion."""
    return ((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)

def taylor_cos(x, n):
    """Compute cos(x) using the Taylor series expansion."""
    return ((-1)**n * x**(2*n)) / math.factorial(2*n)