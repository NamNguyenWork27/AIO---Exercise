def factorial_func(value):
    res = 1 
    for i in range(value):
        res *= (i+1)
    return res 
    
def approx_sin(x, n):
    sin_approx = 0
    for i in range(n+1):
        coef = (-1) ** i
        num = x ** (2*i+1)
        denom = factorial_func(2*i+1)
        sin_approx += (coef) * (num/denom)
    return sin_approx

def approx_cos(x, n):
    cos_approx = 0
    for i in range(n+1):
        coef = (-1) ** i 
        num = x ** (2*i)
        denom = factorial_func(2*i)
        cos_approx += coef * (num/denom)
    return cos_approx

def approx_sinh(x, n):
    sinh_approx = 0
    for i in range(n+1):
        coef = 1  
        num = x ** (2*i+1)
        denom = factorial_func(2 * i + 1)
        sinh_approx += (coef) * (num/denom)
    return sinh_approx

def approx_cosh(x, n):
    cosh_approx = 0
    for i in range(n+1):
        coef = 1 
        num = x**(2*i)
        denom = factorial_func(2*i)
        cosh_approx += coef * (num/denom)
    return cosh_approx
    

if __name__ == "__main__":
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the number of terms to approximate: "))
    print("Approximations:")
    print(f"sin({x}) ≈ {approx_sin(x, n)}")
    print(f"cos({x}) ≈ {approx_cos(x, n)}")
    print(f"sinh({x}) ≈ {approx_sinh(x, n)}")
    print(f"cosh({x}) ≈ {approx_cosh(x, n)}")  