def is_sorted(mylist):
    check =0
    for i in range(len(mylist)):
        if i != 0:
            if mylist[i] < mylist[i-1]:
               check += 0
            else:
               check += 1
        else:
            check += 1
    print(check)
    if check == len(mylist):
        return True
    else:
        return False
   
x = input("Enter string to check:")
x = list(x)
print("Output:",is_sorted(x)) 
