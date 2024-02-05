# Soduku Solver Algorithms Visualizer

This python-based Sudoku Visualizer uses the pygame library to display how different algorithms (simple backtracking and minimal remaining value) solve Sudoku puzzles.

Support this project by leaving a ⭐

## Existing Algorithms:

-<b>Naive backtracking</b>: Simplest brute-force approach, where you go from left to righ and try every possible number from 1 to 9. If this leads to an invalid board state then backtrack to a previous branch and try the next valid number.

![](/public/naive.gif)

-<b>Minimal Remaining Values</b>: Solution based on constant propagation. We maintain a list of which possible values each square can possibly have, given the other
numbers that have been assigned. Instead of going left to right, we select the next index by the minimal value remaining heuristic - the empty square with the least number of possible values.

![](/public/mrv.gif)

## How to use:

- Clone the GitHub repository `git clone https://github.com/Erhan1706/Soduku-Solver-Visualizer.git`
- Install requirements: `pip install -r requirements.txt`
- Run: `python src/main.py`
 