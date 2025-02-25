# Write a Python program that prompts the user for two floating-point values and displays
# the result of the first number divided by the second, with exactly six decimal places
# displayed.

# Input two floating-point numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform division
result = num1 / num2

# Display the result with exactly six decimal places
print(f"The result is: {result:.6f}")
