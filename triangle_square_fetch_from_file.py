#Fetch number from triangle_squares.txt
import sys

#Load numbers from file
nums_file = open("triangle_squares.txt", "r")
nums = nums_file.read().split(',')

print(nums[-1]) #Print the nth number

sys.exit() #Shell is pretty much frozen at this point
