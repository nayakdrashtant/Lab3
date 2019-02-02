import functools
def list_sum(x,y):
    return x + y

def generate_even_num_list():
    mylist = []
    for i in range(100,500):
        if i % 2 == 0:
            mylist.append(i)
    return mylist

mylist = generate_even_num_list()
print(functools.reduce(list_sum,mylist))
