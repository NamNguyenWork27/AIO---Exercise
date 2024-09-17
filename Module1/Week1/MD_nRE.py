def MD_nRE(y, yhat, n, p):
    return (y ** (1/n) - yhat ** (1/n)) ** p 

if __name__ == "__main__":
    y = float(input("Enter the value of y: "))
    yhat = float(input("Enter the value of yhat: "))
    n = int(input("Enter the value of n: "))
    p= int(input("Enter the value of p: "))
    print(MD_nRE(y, yhat, n, p))