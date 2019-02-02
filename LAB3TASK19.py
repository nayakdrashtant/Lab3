def multiple_input(a):
    x = []
    for i in range(int(a)):
        n = input("Enter no:")
        x.append(n)
    sum_all(x)

def sum_all(a):
    su = 0
    for i in a:
        su += int(i)
    print(su)


n = input("Enter no of inputs for sumatiion:")
multiple_input(n)
