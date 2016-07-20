# triangle_squares

### About
This is in response to [Puzzle: Is 36 the only triangle-square number?](https://www.youtube.com/watch?v=Gh8h8MJFFdI)

### Math
Square numbers (duh):
f(x)=x*x

Triangle numbers:

![screenshot](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/First_six_triangular_numbers.svg/220px-First_six_triangular_numbers.svg.png)

![screenshot](https://wikimedia.org/api/rest_v1/media/math/render/svg/25483dd341ee5ef3b10a6594c60d7366d4dffe8b)

## [triangle_square_brute.py](https://github.com/jsheradin/triangle_squares/blob/master/triangle_square_brute.py)

### Method:
* Find square numbers
* Find triangle numbers
* Find the ones in common

### Program
Tested in Python 3.5.2 but should run in any Python 3 version. The program features basic multithreading as set by thread_count. It isn't very CPU intensive but it eats RAM like crazy.

### Results
Current configuration found these numbers in about 30 seconds:
[1, 36, 1225, 41616, 1413721, 48024900, 1631432881]

## [triangle_square_solved.py](https://github.com/jsheradin/triangle_squares/blob/master/triangle_square_solved.py)

### Method:
* Using [algebraic solution found by somebody smarter than myself](https://oeis.org/A001110), calculate the numbers

### Program
Runs pretty much immediately, the limiting factor is Python's max number size. I may change it over to a giant library in the future.

### Results
[triangle_squares.txt](https://github.com/jsheradin/triangle_squares/blob/master/triangle_squares.txt)

## [triangle_square_graph_gen.py](https://github.com/jsheradin/triangle_squares/blob/master/triangle_square_graph_gen.py)
This uses matplotlib, so have that installed to run it.

![screenshot](https://github.com/jsheradin/triangle_squares/blob/master/triangle_squares_graph.png?raw=true)
