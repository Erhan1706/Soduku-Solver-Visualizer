# Soduku Solver Algorithms Visualizer

This python-based Sudoku Visualizer uses the pygame library to display how different algorithms (simple backtracking and minimal remaining value) solve Sudoku puzzles.

Support this project by leaving a ⭐

## Existing Algorithms:

-<b>Naive backtracking</b>: The simplest brute-force approach. It involves iterating through each empty square from left to right and trying every possible number from 1 to 9. If a selected number leads to an invalid board state then backtrack to the previous decision point and try the next valid number.

![](/public/naive.gif)

-<b>Minimal Remaining Values</b>: This algorithm relies on constant propagation. It maintains a list of possible values that each square can have, given the other
numbers that have been already assigned. We select the next index by the minimal value remaining heuristic - the empty square with the least number of possible values remaining. 

![](/public/mrv.gif)

## How to use:

- Clone the GitHub repository `git clone https://github.com/Erhan1706/Soduku-Solver-Visualizer.git`
- Install requirements: `pip install -r requirements.txt`
- Run: `python src/main.py`
