# FOR LOOPS

# Example 1 - Print numbers from 0 to 4
for i in range(5):
    print(i)


# Example 2 - Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# Example 3 - Print multiplication table of 2
for i in range(1, 11):
    print("2 x", i, "=", 2 * i)



# WHILE LOOPS

# Example 1 - Print numbers from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1


# Example 2 - Print even numbers from 2 to 10
num = 2

while num <= 10:
    print(num)
    num += 2


# Example 3 - Countdown
number = 5

while number > 0:
    print(number)
    number -= 1

# nested loops
for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()