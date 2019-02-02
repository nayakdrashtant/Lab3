import operator
def processdata():
    fin = open("word.txt","r")
    mydict = dict()
    mylist = []
    for f in fin:
        f = f.strip()
        mylist.append(f)
    for f in mylist:
        fs = ''.join(sorted(f))
        for fi in mylist:
            if f != fi:
                fis = ''.join(sorted(fi))
                if fis == fs:
                    if fi not in mydict:
                        mydict[fs] = [fi]
                    else:
                        mydict[fi].append(fs)
 #   sorted_x = sorted(mydict.items(), key=operator.itemgetter(0))
#    sred = sorted(mydict.items(), key=lambda value: value[1])
    print(mydict)

#    return mydict
processdata()        
