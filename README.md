# Crossword Puzzle Solver

## Overview
The Crossword Puzzle Solver is an advanced tool designed to solve challenging 9x9 puzzles, particularly tested on New York Times crossword puzzles. It employs Constraint Satisfaction Problem (CSP) modeling and incorporates sophisticated constraint satisfaction algorithms, including AC-3. The solver is enhanced with a strategic degree heuristic for efficient problem-solving.

## Features
- Solve crossword puzzles with varying levels of complexity.
- Utilizes Constraint Satisfaction Problem (CSP) modeling.
- Implements the AC-3 algorithm for constraint satisfaction.
- Incorporates a strategic degree heuristic for efficient problem-solving.

## Usage

### Prerequisites
Make sure you have the following dependencies installed:
- Python (version 3.x recommended)

### Running the Solver
1. Clone this repository to your local machine.
    ```bash
    git clone https://github.com/your-username/crossword-puzzle-solver.git
    ```
2. Navigate to the project directory.
    ```bash
    cd Crossword-Puzzle-as-a-CSP
    ```
3. Run the solver script.
    ```bash
    python main.py
    ```
4. Follow the on-screen instructions to input the crossword puzzle and initiate the solving process.

## Implementation Details
The solver is implemented with the following key components:

### Constraint Satisfaction Problem (CSP) Modeling
The crossword puzzles are modeled as CSPs, defining variables, domains, and constraints to represent the puzzle-solving process.

### AC-3 Algorithm
The solver utilizes the AC-3 (Arc-Consistency 3) algorithm, a constraint satisfaction algorithm, to enhance efficiency in narrowing down possible solutions.

### Strategic Degree Heuristic
A strategic degree heuristic is employed to prioritize variables and improve the solving strategy, making the solver more adept at handling complex puzzles.

## Contributing
Contributions are welcome! If you have suggestions, enhancements, or bug fixes, please submit a pull request.

## Acknowledgments
- The solver has been tested on New York Times crossword puzzles.
