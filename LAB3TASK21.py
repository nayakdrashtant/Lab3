import operator
def histogram(a):
    mydict = dict()
    for c in a :
        if c not in mydict:
            mydict[c] = 1
        else:
            mydict[c] += 1
    return mostfrequant(mydict)

def mostfrequant(dic):
    sorted_x = sorted(dic.items(), key=operator.itemgetter(1))
    for e in sorted_x:
        print(e[0])
    return sorted_x

x = input("Enter String:")
print(histogram(x))
