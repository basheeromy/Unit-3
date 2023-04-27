# Slice list into 3 equal chunks and reverse each chunk

mylist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
length = len(mylist)
sectlen = int(length/3)
sublist1 = mylist[0:sectlen]
sublist2 = mylist[sectlen:(sectlen*2)]
sublist3 = mylist[sectlen*2:sectlen*3]
print(sublist1)
print(sublist2)
print(sublist3)