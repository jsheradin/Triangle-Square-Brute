#Algebraic solution to generate triangle-square numbers

nums = []
for n in range(0, 200):
    #Math used from https://oeis.org/A001110
    nums.append(round(((1 + 2**0.5)**(2*n) - (1 - 2**0.5)**(2*n))/(4*2**0.5))**2)
with open("triangle_squares.txt", "w") as save_file:
    for item in nums:
        save_file.write("%s\n" % item)
print("done")
