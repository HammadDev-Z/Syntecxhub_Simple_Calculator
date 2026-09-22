"""Simple command-line calculator supporting +, -, x, / and clear."""

OPERATORS = {"+", "-", "x", "*", "/"}


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def calculate(a, operator, b):
    if operator == "+":
        return add(a, b)
    if operator == "-":
        return subtract(a, b)
    if operator in ("x", "*"):
        return multiply(a, b)
    if operator == "/":
        return divide(a, b)
    raise ValueError(f"Unsupported operator: {operator}")


def parse_number(text):
    try:
        return float(text)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid number: {text!r}")


def parse_expression(text):
    """Parse 'num operator num' (e.g. '4 + 5') into (a, operator, b)."""
    parts = text.split()
    if len(parts) != 3:
        raise ValueError(
            "Invalid input. Expected format: <number> <operator> <number>, e.g. 4 + 5"
        )

    a_text, operator, b_text = parts
    if operator not in OPERATORS:
        raise ValueError(
            f"Invalid operator: {operator!r}. Use one of + - x /"
        )

    a = parse_number(a_text)
    b = parse_number(b_text)
    return a, operator, b


def format_result(value):
    if value == int(value):
        return str(int(value))
    return str(value)


MENU = """
==== Simple Calculator ====
Enter a calculation, e.g.:  4 + 5   or   10 / 2   or   6 x 3
Commands: 'clear' to reset the screen, 'exit' to quit
============================
"""


def run():
    print(MENU)
    while True:
        try:
            user_input = input("Enter calculation (or command): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        command = user_input.lower()
        if command == "exit":
            print("Goodbye!")
            break
        if command == "clear":
            print("\n" * 50)
            print(MENU)
            continue

        try:
            a, operator, b = parse_expression(user_input)
            result = calculate(a, operator, b)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            print(f"Result: {format_result(a)} {operator} {format_result(b)} = {format_result(result)}")


if __name__ == "__main__":
    run()
