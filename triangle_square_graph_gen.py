#Generate a graph to visualize a pattern in triangle_square numbers

import matplotlib.pyplot as plt

nums = [line.rstrip('\n') for line in open("triangle_squares.txt", "r")]
nums = list(map(int, nums))
nums = nums[:150] #Really big bumers break matplotlib :(

plt.plot(nums)
plt.yscale('log')
plt.xscale('linear')
plt.grid(True)
plt.show()
