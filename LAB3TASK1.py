import functools
def nested_sum(x,y):
    return x + y

print(functools.reduce(nested_sum,[1,2,3,4,5,6,7]))

