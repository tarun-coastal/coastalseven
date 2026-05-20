# Creating a Dictionary


a = {"x": 1, "y": 2}
print(a)

b = dict(name="Sam", age=20)
print(b)

# Accessing Dictionary Items
d = {"name": "Kat", "age": 21}

print(d["name"])     # Access using key
print(d.get("age"))  # Access using get()


# Adding and Updating Dictionary Items
d = {"name": "Sam"}

d["age"] = 21        # Adding a new key-value pair
d["name"] = "Alex"   # Updating an existing value
print(d)

# Removing Dictionary Items
d = {"a": 1, "b": 2}
del d["a"]
print(d)

#  pop(): removes the item with the given key and returns its value


d = {"a": 1, "b": 2}

val = d.pop("a")
print(val)
print(d)

# popitem
d = {"a": 1, "b": 2}
print(d.popitem())

# clear(): removes all items in dictionary

d = {"a": 1, "b": 2}
d.clear()
print(d)

# Iterate keys
d = {"a": 1, "b": 2}
for key in d:
    print(key)


# Iterate values
d = {"a": 1, "b": 2}
for value in d.values():
    print(value)

#  Iterate key-value pairs
d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)


# Nested Dictionaries
d = {
    "student": {
        "name": "Sam",
        "age": 20
    }
}

print(d["student"]["name"])