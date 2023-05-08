# Generator
# In Python, a generator is a function that returns an iterator that produces 
# a sequence of values when iterated over.

# Generators are useful when we want to produce a large sequence of values, 
# but we don't want to store all of them in memory at once.

def multiple_generator(n,m):
    value = 1
    while value < n:
        yield value * m
        value += 1


# Here, we created a generator with name multiple_generator,
# now, we can create an iterable object with the help of this generator    
an = multiple_generator(10,2)

print(f"iterable object/generator object created with the help of generator is {an}\n\n")

# by creating a object like this, we can save memory space until we actually need all those values later

# to generator only one value from a generator, we can use, next. but, there is a possibily for getting error

print(next(an))
print("\n")


# when we need, we can generate values from this generator as we do bellow.. 
# but, as we generated one value with next function, generator will generate value from there.
# here, it is 4

result_list = []
for i in an:
    result_list.append(i)
    
print(f"values generated from generator object assigned to list  :- {result_list}\n")



# same like list comprehension syntax, we can simplify a generator as given bellow

generator = (i*3 for i in range(10))


print(list(generator))