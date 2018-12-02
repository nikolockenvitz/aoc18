# Advent of Code 2018
I will publish my solutions for [Advent of Code](https://adventofcode.com/2018) puzzles here.
Main implementation language will be Python 3.

The puzzle inputs for each day are stored in folder _input_. The solutions are written to folder _output_. Each programming language has it's own folder for implementation (currently only Python).

# Python
The class _AOC_ in _aoc.py_ implements some general functionality and can be used in the specific implementations. It will also create (based on the template _day0.py_) a script for each day with basic implementation (getting input, save results, ...). The daily puzzle input will be fetched from [adventofcode.com](https://adventofcode.com/2018) and saved to the corresponding file in _input_. Therefor credentials (cookies) are stored in file _cookie.txt_ to authenticate to Advent of Code and get personal puzzle input.
