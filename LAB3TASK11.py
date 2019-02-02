def histogram(a):
    mydict = dict()
    for i in a:
        if i not in mydict:
            mydict[i] = 1
        else: 
            mydict[i] += 1
    print_hist(mydict)

def print_hist(h):    
    for c in sorted(h):        
        print(c, h[c])

x = input("Enter string:")
histogram(x)
