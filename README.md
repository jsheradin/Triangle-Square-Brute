# Triangle-Square-Brute

### About
This is a brute force solution to find triangle-square numbers in a given range. It calculates all triangle numbers, all square numbers, and then finds the ones in common.

This is in response to [Puzzle: Is 36 the only triangle-square number?](https://www.youtube.com/watch?v=Gh8h8MJFFdI).

### Math
Square numbers (duh):
f(x)=x*x

Triangle numbers:
![screenshot](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/First_six_triangular_numbers.svg/220px-First_six_triangular_numbers.svg.png)
![screenshot](https://wikimedia.org/api/rest_v1/media/math/render/svg/25483dd341ee5ef3b10a6594c60d7366d4dffe8b)

### Program
Tested in Python 3.5.2 but should run in any Python 3 version. The program features basic multithreading as set by thread_count. It isn't very CPU intensive but it eats RAM like crazy.

### Results
Current configuration found these numbers in about 30 seconds:
[1, 36, 1225, 41616, 1413721, 48024900, 1631432881]