# Pascal's Triangle

This project contains a Python function that generates Pascal's Triangle up to a given number of rows. Pascal's Triangle is a triangular array of numbers, where each number is the sum of the two numbers directly above it.

## Files

- `0-pascal_triangle.py`: This file contains the `pascal_triangle(n)` function that returns a list of lists of integers representing Pascal’s triangle of size `n`.
- `0-main.py`: This is the main script used to test the `pascal_triangle(n)` function.

## Usage

To run the function and display Pascal's Triangle, follow these steps:

1. Clone the repository or download the files.
2. Run the `0-main.py` file, which will print Pascal's Triangle for `n = 5`.

```bash
./0-main.py


The output will look like this:

[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]


Function Description
pascal_triangle(n)
Parameters: n (int) – the number of rows in Pascal's Triangle.
Returns: A list of lists of integers representing Pascal's Triangle.
If n <= 0, the function returns an empty list.

Example

>>> from 0-pascal_triangle import pascal_triangle
>>> print(pascal_triangle(5))
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


Repository
GitHub repository: alx-interview
Directory: 0x00-pascal_triangle


