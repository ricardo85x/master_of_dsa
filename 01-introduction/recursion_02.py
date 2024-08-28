def fibonacci(n):
    if n <=1:
        return n
    
    n1 = n - 1
    oneBack = fibonacci(n1)
    n2 = n - 2
    twoBack = fibonacci(n2)
    return oneBack + twoBack

print(fibonacci(10))