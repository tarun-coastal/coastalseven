# Creating a Tuple
tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)


# Accessing of Tuples
tup = tuple("Geeks")
print(tup[0])
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a, b, c = tup
print(a)
print(b)
print(c)

# Concatenation of Tuples
tup1 = (0, 1, 2, 3)
tup2 = ('Geeks', 'For', 'Geeks')
tup3 = tup1 + tup2
print(tup3)


# Slicing of Tuple
tup = tuple('GEEKSFORGEEKS')
print(tup[1:])
print(tup[::-1])
print(tup[4:9])


# Deleting a Tuple
tup = (0, 1, 2, 3, 4)
del tup
print(tup)