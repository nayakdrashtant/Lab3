def cumulative_sum(mylist):
    newlist = []
    for i in range(len(mylist)):
        if i == 0:
           newlist.append(mylist[i])
        else:
        #  print(i)
            cumu = mylist[i] + newlist[i-1]
            newlist.append(cumu)
    print("Input:",mylist)
    print("Output:",newlist)

cumulative_sum([1,2,3,4,5])
