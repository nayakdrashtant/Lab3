def list_num(mylist):
  newlist = []
  for my in mylist:
    if my % 5 == 0:
      newlist.append(my)
  return newlist

mylist = [5,1,0,10,15,3]
print(list_num(mylist))
