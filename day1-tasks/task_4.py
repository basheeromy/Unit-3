# Count the occurrence of each element from a list

mylist = [1,1,2,2,2,3,3,3,3,4,4,4,4,4]
length = len(mylist)
occurrence = {}
start = 0
for i in mylist:
    start += 1
    if f"{i}" not in occurrence.keys():
        occurrence[f"{i}"] = 1
        
    for j in range(start,length):
        if i == mylist[j]:
            occurrence[f"{i}"] = occurrence[f"{i}"] + 1
            break
        
print(occurrence)