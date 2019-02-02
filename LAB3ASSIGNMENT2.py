def checkdup(mylist):
    mylist = list(mylist)
    flag = False
    dups = dict()
    for myl in mylist:
        if myl not in dups:
             dups[myl] = 1
        else:
             dups[myl] += 1
  #  print(dups)
    if 2 in dups.values():
        flag = True
    else:
        flag = False
    return flag

x = input("Enter string to check")
print(checkdup(x))
