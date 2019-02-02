known = {0:0, 1:1}
def fibonacci(n):
    n = int(n)
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)    
    known[n] = res
    return res

x = input("Enter no:")
print(fibonacci(x))
