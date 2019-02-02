import random
def di_demo(myfile):
    print(myfile)
    fin = open(myfile,"r")
    mydi = dict()
    for fi in fin:
        mydi[fi] = random.randint(0,999999)
    return mydi

x = input("Enter file name to create dictionary:")
print(di_demo(x))
