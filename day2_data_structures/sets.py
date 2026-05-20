

# typecasting list to set
s = set(["a", "b", "c"])
print(s)

# Adding element to the set
s.add("d")
print(s)

# Frozen Sets
# Normal set (mutable)
s = set(["a", "b", "c"])
print("Normal Set:", s)

# Frozen set (immutable)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)

# Adding elements to Sets:

s = {"a", "b", "c"}
s.add("d")
print(s)


#  Union of Sets
a = {"x", "y"}
b = {"y", "z"}
u = a.union(b)
print(u)

# Intersection of Sets:
a = {1, 2, 3}
b = {2, 3, 4}
i = a.intersection(b)
print(i)

# Difference of Sets

a = {1, 2, 3}
b = {2, 3, 4}
d = a.difference(b)
print(d)

# Clearing a Set

s = {1, 2, 3}
s.clear()
print(s)