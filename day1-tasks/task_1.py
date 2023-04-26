
# Create a list by picking an odd-index items from the first list and even index items from the second

list1 = [0,1,2,3,4,5,6,7,8,9]
list2 = [0,1,2,3,4,5,6,7,8,9]


len1 = len(list1)
len2 = len(list2)

loop = 0

list3 = []
list4 = []

if len1 > len2:
    loop = len1
else:
    loop = len2
    
for i in range (1,loop):
    if i % 2 == 0:
        if i < len2:
            list4.append(list2[i])
    else:
        if i < len1: 
            list3.append(list1[i])
    
print(list3)
print(list4)
