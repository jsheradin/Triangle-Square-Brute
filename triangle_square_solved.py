#Algebraic solution to generate triangle-square numbers

nums = []
a = (1 + 2**0.5)
b = (1 - 2**0.5)
c = (4*2**0.5)
for n in range(0, 200):
    #Math used from https://oeis.org/A001110
    two_n = 2*n
    nums.append(round(((a**two_n - b**two_n)/c)**2))
    #print(n, ":", nums[n])
with open("triangle_squares.txt", "w") as save_file:
    for item in nums:
        save_file.write("%s\n" % item)
print("done")
