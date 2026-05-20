# Used for decision making

# Example 1 - Voting Eligibility
age = 18

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Example 2 - Even or Odd
number = 7

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Example 3 - Pass or Fail
marks = 75

if marks >= 35:
    print("Pass")
else:
    print("Fail")




# nested if-else statement
age = 70
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")




# match case
number = 2

match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")