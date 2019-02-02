def capitalize_all(mylist):
  newlist = []
  for my in mylist:
    newlist.append(my.upper())
  return newlist

mylist = ["asd","asdad","gdfgf","wwe","as","asdasd"]
print(capitalize_all(mylist))

