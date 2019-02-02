def histogram(a):
    mydi = dict()
    for i in a:
        if i not in mydi:
            mydi[i] = 1
        else:
            mydi[i] += 1
    invert_dict(mydi)

def invert_dict(d):
  #  print(d)
    inverse = dict()
    for key in d:
       # print(key)
        val = d[key]
       # print(inverse)
        if val not in inverse:
            inverse.setdefault(key,val) 
#             inverse[val] = [key]
        else:
#            inverse[val].append(key)
            # print(key)
            inverse.setdefault(key)
    print(inverse)

x = input("Enter string:")
histogram(x)
