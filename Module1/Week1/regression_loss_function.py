import random
import math

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def mae(n):
    mae = 0
    for i in range(n):
        y = random.random()
        yhat = random.random()
        abs_error = abs(y - yhat)
        mae = mae + abs_error
    mae = mae / n
    return mae 

def mse(n):
    mse = 0
    for i in range(n):
        y = random.random()
        yhat = random.random()
        absolute_error = (y - yhat) ** 2
        mse = mse + absolute_error
    mse = mse / n
    return mse 
    
def rmse(n):
    rmse = 0
    for i in range(n):
        y = random.random()
        yhat = random.random()
        absolute_error = (y - yhat) ** 2
        rmse = rmse + absolute_error
    rmse = math.sqrt(rmse / n)
    return rmse  
    
def reg_activation_func(num, loss_name):
    result = None
    if loss_name == 'mae':
        result = mae(num)
    elif loss_name == 'mse':
        result = mse(num)
    elif loss_name == 'rmse':
        result = rmse(num)
    return result    
    
def exercise3(num, loss_name):
    if not is_number(num):
        print('num must be a number')
        return
    
    num = int(num)
    result = reg_activation_func(num, loss_name)
    if result is None:
        print(f'{loss_name} is not supported')
    else:
        print(f'{loss_name}: f({num}) = {result}')

if __name__ == "__main__":
    num_samples = input("Input number of samples (integer number): ")
    loss_name = input("Input loss name (mae|mse|rmse): ")
    exercise3(num_samples, loss_name)