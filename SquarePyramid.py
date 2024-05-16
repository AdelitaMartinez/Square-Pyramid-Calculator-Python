# MartinezP1
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Make a program to calculate the surgace area and volume of a square pyramid
# Volume of a pyramid
# Python Version:

# Display a header explaing the program
print("\n This program calculates the surface area and volume of a square pyramid. \n")

# Get the length of the base from user
a = float(input("Enter the length of the base of the pyramid in feet:"))

# Get the height of the pyramid from user
h = float(input("Enter the height of the pyramid in feet: "))

# Formula: 
  # volume = a**2h / 3
  # slantheight = sqrt(h**2 + (a / 2)**2)
  # Area of one pyramid side = slantheight * a /2

# Calculate the volume
volume = (a**2 * h) / 3

# Calculate the slant height
slant_height = math.sqrt(h**2 + (a / 2)**2)

# Calculate the area of one pyramid side
area_one_side = (slant_height * a) / 2

# Calculate the surface area of the four sides
surface_area = 4 * area_one_side

# Display the results with three decimal places
print("\n Results: \n")
