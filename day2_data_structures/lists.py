

# Using Square Brackets
a = [1, 2, 3]
print(a)

b = ["apple", "banana"]
print(b)

# Using list() Constructor

a = list((1, 2, 3, 'apple', 4.5))  
print(a)

b = list("GFG")
print(b)

# Creating List with Repeated Elements

a = [2] * 5
b = [0] * 7

print(a)
print(b)


a = [10, 20, 30]
print(a[0])
print(a[-1])


# Adding Elements into List
a = [1, 2]
a.append(3)
print(a)

# insert(): Adds an element at a specific position.

a = [1, 3]
a.insert(1, 2)
print(a)


# extend(): Adds multiple elements to the end of the list.
a = [1, 2]
a.extend([3, 4])
print(a)



#  remove(): Removes the first occurrence of an element.




a = [1, 2, 3]
a.remove(2)
print(a)


# pop(): Removes the element at a specific index or the last element if no index is specified.
a = [1, 2, 3]
a.pop()
print(a)

# del statement: Deletes an element at a specified index.
a = [1, 2, 3]
del a[1]
print(a)

# 4. clear(): removes all items.

a = [1, 2, 3]
a.clear()
print(a)


# Iterating Over Lists
a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)



# Nested Lists
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])


# Iterating Over Lists

a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)



# Nested Lists
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])