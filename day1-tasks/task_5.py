#  Create a Python set such that it shows the element from both lists in a pair

list1 = [1,2,3,4,5,6,7,8,9,9,9,45]
list2 = [1,2,3,4,5,6,7,8,9,9,9,45]

result = set()
if len(list1) < len(list2):
    big = list1
else:
    big = list2

for i in range(len(big)):
    result.add((list1[i],list2[i]))
print(result)