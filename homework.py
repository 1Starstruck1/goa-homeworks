# Get the user's name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# Print name and age
print("Name:", name, ", Age:", age)

# Get the width and height of the rectangle
width = int(input("Enter the rectangle's width: "))
height = int(input("Enter the rectangle's height: "))

# Calculate area and perimeter
area = width * height
perimeter = 2 * (width + height)

# Print the results
print("Rectangle area:", area)
print("Rectangle perimeter:", perimeter)

# Additional message for the user
print("Thank you, " + name + "! The program completed the calculations successfully.")
