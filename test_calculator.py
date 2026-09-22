import unittest

from calculator import (
    add,
    subtract,
    multiply,
    divide,
    calculate,
    parse_number,
    parse_expression,
    format_result,
)


class TestArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)


class TestCalculate(unittest.TestCase):
    def test_calculate_all_operators(self):
        self.assertEqual(calculate(2, "+", 3), 5)
        self.assertEqual(calculate(2, "-", 3), -1)
        self.assertEqual(calculate(2, "x", 3), 6)
        self.assertEqual(calculate(2, "*", 3), 6)
        self.assertEqual(calculate(6, "/", 3), 2)

    def test_calculate_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(5, "/", 0)

    def test_calculate_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate(2, "%", 3)


class TestParsing(unittest.TestCase):
    def test_parse_number_valid(self):
        self.assertEqual(parse_number("4"), 4.0)
        self.assertEqual(parse_number("-3.5"), -3.5)

    def test_parse_number_invalid(self):
        with self.assertRaises(ValueError):
            parse_number("abc")

    def test_parse_expression_valid(self):
        self.assertEqual(parse_expression("4 + 5"), (4.0, "+", 5.0))
        self.assertEqual(parse_expression("10 / 2"), (10.0, "/", 2.0))

    def test_parse_expression_invalid_format(self):
        with self.assertRaises(ValueError):
            parse_expression("4 5")
        with self.assertRaises(ValueError):
            parse_expression("4 + 5 + 6")

    def test_parse_expression_invalid_operator(self):
        with self.assertRaises(ValueError):
            parse_expression("4 % 5")

    def test_parse_expression_invalid_number(self):
        with self.assertRaises(ValueError):
            parse_expression("a + 5")


class TestFormatResult(unittest.TestCase):
    def test_integer_like_result(self):
        self.assertEqual(format_result(4.0), "4")

    def test_decimal_result(self):
        self.assertEqual(format_result(3.5), "3.5")


if __name__ == "__main__":
    unittest.main()
