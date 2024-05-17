import math

# MartinezP1
# Programmer: Adelita Martinez
# Email: amartinez1013@cnm.edu
# Purpose: Make a program to calculate the surgace area and volume of a square pyramid
# Volume of a pyramid
# Python Version:

# Display a header explaing the program
print("Welcome!")
print("\n This program calculates the surface area and volume of a square pyramid. \n")


# Get the height of the pyramid from user
h = float(input("Enter the height of the pyramid: "))

# Get the length of the base from user
a = float(input("Enter the length of the base of the pyramid:"))

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

# Round the results to three decimal points
volume = round(volume, 3)
surface_area = round(surface_area, 3)

# Display the results 
print("\nResults:\n")
print("The volume of the pyramid is:", volume)
print("The surface area of the four sides is:", surface_area)