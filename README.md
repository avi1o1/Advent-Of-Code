# Advent of Code

This repository contains my solutions for [Advent of Code](https://adventofcode.com/) challenges.

## Structure

The repository is organized by year, with each day's challenge in its own folder:

```
2024/
├── Day1/
│   ├── input1.txt    # Part 1 input data
│   ├── input2.txt    # Part 2 input data (if different)
│   ├── sol1.py       # Part 1 solution
│   └── sol2.py       # Part 2 solution
├── Day2/
│   └── ...
└── Day25/
    └── ...
```

## Running Solutions

Each solution is contained in its respective Python file. To run a specific day's solution:

```bash
cd 2024/Day1
python sol1.py  # Run part 1
python sol2.py  # Run part 2
```

## Setup Script

The [`script.py`](script.py) file contains a utility script that automatically creates the folder structure for new days:

```bash
python script.py
```

This creates folders Day2 through Day31 with the standard file structure for each day.

## About Advent of Code

[Advent of Code](https://adventofcode.com/) is an annual set of Christmas-themed programming puzzles that can be solved in any programming language. Each day from December 1st to 25th features a two-part puzzle that gets progressively more challenging.

## Language

All solutions are implemented in **Python**.