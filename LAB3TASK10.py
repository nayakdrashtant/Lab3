def histogram(a,b,c):
    mydict = dict()
    for i in a:
    #    mydict[i] = i in mydict ? mydict[i] += 1 : mydict[i] = 1
        if a not in mydict:
           mydict[i] = 1
        else:
           mydict[i] += 1
    print("Key value is:",mydict.get(b,u))
    return mydict

x=input("Enter string:")
z=input("Enter elemenet to check:")
#y=input("Enter key of dictonary to check element is there or not:")
u=input("Enter default value:")
print(histogram(x,z,u))
