# List Comprehension

a = [2, 3, 4, 5]
res = [val ** 2 for val in a]
print(res)


# Conditional Statements in List Comprehension
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)