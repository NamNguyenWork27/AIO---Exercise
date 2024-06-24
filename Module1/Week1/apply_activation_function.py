import math

def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

def calc_sig(x):
        return 1.0 / (1 + math.e**(-x))

def calc_elu(x):
        alpha = 0.01
        result = None
        if x < 0:
            result = alpha*(math.e**x - 1)
        else:
            result = x 
        return result 

def calc_relu(x):
    if x <= 0:
        result = 0.0
    else:
        result = x 
    return float(result)
    
def calc_activation_func(x, act_name):
    result = None
    if act_name == 'relu':
        result = calc_relu(x)
    elif act_name == 'sigmoid':
        result = calc_sig(x)
    elif act_name == 'elu':
        result = calc_elu(x)
    return result
 
def exercise2(x, act_name):
    if not is_number(x):
        print('x must be a number')
        return
    
    x = float(x)
    result = calc_activation_func(x, act_name)
    if result is None:
        print(f'{act_name} is not supported')
    else:
        print(f'{act_name}: f({x}) = {result}')

if __name__ == "__main__":
    x = input("Input x = ")
    act_name = input("Input activation Function (sigmoid|relu|elu): ")
    exercise2(x, act_name)       
    