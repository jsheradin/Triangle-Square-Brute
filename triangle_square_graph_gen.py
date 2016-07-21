#Generate a graph to visualize a pattern in triangle_square numbers
import matplotlib.pyplot as plt

#Load numbers from triangle_squares.txt
nums = [line.rstrip('\n') for line in open("triangle_squares.txt", "r")]
nums = list(map(int, nums))

#Find last digit of numbers
last_digit = []
for n in range(len(nums)):
    last_digit.append(nums[n]%10)
    
##Plot stuff
#Occurrence
nums = nums[:150] #Really big bumers break matplotlib :(
plt.figure(1)
plt.plot(nums)
plt.title('Occurrence')
plt.yscale('log')
plt.ylabel('Value')
plt.xscale('linear')
plt.xlabel('nth Number')
plt.grid(True)
plt.savefig('triangle_squares_graph_occurrence.png')

#Ending digit
plt.figure(2)
plt.hist(last_digit, bins=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], normed=1)
axes = plt.gca()
axes.set_xlim([0, 10])
plt.grid(True)
plt.title('Terminating Digit')
plt.ylabel('Probability')
plt.xlabel('Digit')
plt.savefig('triangle_squares_graph_terminating_digit.png')

print("done")
#plt.show()
