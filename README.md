# Simple Calculator

A command-line calculator built in Python, supporting addition, subtraction,
multiplication, division, and a screen-clear command. Built as Project 1 for
the Syntecxhub Python Programming internship.

## Features

- Supports `+`, `-`, `x` (multiplication), and `/` (division)
- Accepts user input in the form `<number> <operator> <number>` (e.g. `4 + 5`)
- Validates input and reports clear error messages for bad input
- Handles divide-by-zero gracefully
- `clear` command resets the screen, `exit` quits the program
- Calculation logic is kept in standalone functions, separate from I/O, for testability

## Usage

Run the calculator:

```bash
python calculator.py
```

Example session:

```
Enter calculation (or command): 4 + 5
Result: 4 + 5 = 9
Enter calculation (or command): 10 / 0
Error: Cannot divide by zero.
Enter calculation (or command): exit
Goodbye!
```

## Running Tests

```bash
python -m unittest test_calculator.py -v
```

## Project Structure

- `calculator.py` – calculator logic and command-line interface
- `test_calculator.py` – unit tests for the calculator functions
