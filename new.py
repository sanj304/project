# # # Prompting the user to enter a number
# number = int(input("Enter a number: "))
#
# # Checking if the number is even or odd
# if number % 2 == 0:
#     print(f"{number} is even.")
# else:
#     print(f"{number} is odd.")

# Taking age input from the user
age = int(input("Enter your age: "))

# Classifying age into different life stages
if age < 0:
    print("Invalid age entered. Please enter a positive number.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
