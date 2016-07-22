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
* Using ![screenshot](https://wikimedia.org/api/rest_v1/media/math/render/svg/ca7e8212d48865d696c7bdabf9c28508d3df67b0) with ![screenshot](https://wikimedia.org/api/rest_v1/media/math/render/svg/a60c168417a797edeccbb2990524bf29c0bd0acc) and ![screenshot](https://wikimedia.org/api/rest_v1/media/math/render/svg/769837e6f47fab8d3a05dad584fd3503a31c3565) calculate numbers

### Program
It is not multithreaded as the algebra relies on recursion. RAM and CPU usage is moderate with the longest operation being str(nums) to write the numbers to file.

### Results
[The first 10000 triangle squares (really big file use caution opening)](https://github.com/jsheradin/triangle_squares/blob/master/triangle_squares.txt)

## [triangle_square_graph_gen.py](https://github.com/jsheradin/triangle_squares/blob/master/triangle_square_graph_gen.py)

Dependencies:
* Matplotlib

### Results

![screenshot](https://raw.githubusercontent.com/jsheradin/triangle_squares/master/triangle_squares_graph_occurrence.png)

![screenshot](https://raw.githubusercontent.com/jsheradin/triangle_squares/master/triangle_squares_graph_terminating_digit.png)

## [triangle_square_fetch_from_file.py](https://github.com/jsheradin/triangle_squares/blob/master/triangle_square_fetch_from_file.py)

### Program

Fetch numbers from the massive files that triangle_square_solved.py can spit out. Uses twice the RAM as the size of triangle_squares.txt

### Results

The [one-hundred-thousandth triangle-square](https://github.com/jsheradin/triangle_squares/blob/master/hundred_thousandth_triangle_square.txt) (if 0 is 1st, 1 is 2nd, 36 is 3rd, etc.) pulled from the output of a tweaked triangle_square_solved.py.

The full output file is >7GB and can't be uploaded to GitHub due to file size limits.
