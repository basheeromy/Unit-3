# Remove and add item in a list. 

# There are multiple methods to add a new elements to list
# first one :- with append() method

mylist = ["one","two","three"]
mylist.append("added with append method")
print(mylist)

# to add an element to a desired position, we can use insert() method

mylist.insert(1,"inserted")
print(mylist)

# to remove list item form last position and assign the same to a variable

last = mylist.pop()
print(last)
print(mylist)

# to remove a list item item from desired position and assign it into a variable

removed = mylist.pop(2)
print (removed)
print(mylist)

# to remove an item by passing the element itself

mylist.remove('three')
print(mylist)
