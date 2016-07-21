# triangle_squares

### About
This is in response to [Puzzle: Is 36 the only triangle-square number?](https://www.youtube.com/watch?v=Gh8h8MJFFdI) It was also just fun to make.

Everything made and tested in Python 3.5.2, use at your own risk.

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
The program features basic multithreading as set by thread_count. It isn't very CPU intensive but it eats RAM like crazy.

### Results
Current configuration found these numbers in about 30 seconds:
[1, 36, 1225, 41616, 1413721, 48024900, 1631432881]

## [triangle_square_solved.py](https://github.com/jsheradin/triangle_squares/blob/master/triangle_square_solved.py)

### Method:
* Using [algebraic solution found by somebody smarter than myself](https://oeis.org/A001110), calculate the numbers

### Program
Runs pretty much immediately, the limiting factor is Python's max number size. I may change it over to a giant library in the future.

### Results
[The first 200 triangle-squares.](https://github.com/jsheradin/triangle_squares/blob/master/triangle_squares.txt) Floating point accuracy is likely a limit and may cause inaccuracies in the larger numbers.

## [triangle_square_graph_gen.py](https://github.com/jsheradin/triangle_squares/blob/master/triangle_square_graph_gen.py)
Dependencies:
* Matplotlib

### Results

![screenshot](https://raw.githubusercontent.com/jsheradin/triangle_squares/master/triangle_squares_graph_occurrence.png)

![screenshot](https://raw.githubusercontent.com/jsheradin/triangle_squares/master/triangle_squares_graph_terminating_digit.png)
