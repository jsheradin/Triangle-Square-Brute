#Algebraic solution to generate triangle-square numbers
print("Starting calculation... ", end="")
nums = [0, 1]
for n in range(2, 10000):
    nums.append(34*nums[n-1] - nums[n-2] + 2)

print("done\nStarting write to disk... ", end="")
with open("triangle_squares.txt", "w") as save_file:
    save_file.write(str(nums))
print("done")
