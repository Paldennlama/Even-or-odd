#Exercise 1

Grade = int(input("Enter your grade: "))

if Grade >= 90:
    print("You got an A")
elif Grade >= 80:
    print("You got a B")
elif Grade >= 70:
    print("You got a C")
elif Grade >= 60:
    print("You got a D")
elif Grade < 60:
    print("You got an F")
else:
    print("Invalid grade")

#Exercise 2

age = int(input("Enter your age please:"))

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a Teenager")
elif age >= 3:
    print("You are a child")
elif age >= 0:
    print("You are a toddler")
elif age < 0:
    print("You haven't been born yet")
elif age >= 30:
    print("You are old")

else:
    print("You are a minor")

#Execise 3

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

#Exercise 4

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
elif number % 3 == 0:
    print("The number is odd")
else:
    print("The number is neither even nor odd")

#Exercise 5

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
