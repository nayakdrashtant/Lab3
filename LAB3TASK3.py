import functools
def list_sum(x,y):
    return x + y

def generat_square_nums():
    mylist = []
    for i in range(0,10):
        if i % 2 ==0:
            i = i ** 2
            mylist.append(i)
    return mylist

print(functools.reduce(list_sum,generat_square_nums()))
