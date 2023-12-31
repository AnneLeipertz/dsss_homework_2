import unittest
from math_quiz import random_int, random_operator, math_operation

class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        """
        Test the random_int function.

        This test checks if random numbers generated by the random_int function are within the specified range.

        Side Effects:
            Prints error message if the generated number is outside the specified range.
        """
        # Test if random numbers generated are within the specified range
        min_val = -10
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        """
        Test the random_operator function.

        This test checks if the random_operator function returns one of the expected mathematical operators.

        Side Effects:
            Prints error message if the returned operator is not in the expected set.
        """
        for _ in range(1000):
            rand_operat = random_operator()
            self.assertIn(rand_operat, ["+", "-", "*"])

    def test_math_operation(self):
        """
        Test the math_operation function with various test cases.

        This test checks if the math_operation function produces the expected formatted problem and result for different input values.

        Side Effects:
            Prints error message if the result doesn't match the expected values or if an exception is not raised when expected.
        """
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (4, 3, '-', '4 - 3', 1),
            (-9, 0, '*', '-9 * 0', 0),
            (10, -1, '+', '10 + -1', 9),
            (6, -4, '*', '6 * -4', -24),
            (-7, 6, '+', '-7 + 6', -1),
            (2, 3, '*', '2 * 3', 6),
            (1, -9, '-', '1 - -9', 10),
            (5, 4, '*', '5 * 4', 20),
            (-2, 7, '+', '-2 + 7', 5)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            with self.subTest(num1=num1, num2=num2, operator=operator):
                if isinstance(expected_answer, type) and issubclass(expected_answer, Exception):
                    # If the expected answer is an exception, check if the function raises it
                    with self.assertRaises(expected_answer):
                        math_operation(num1, operator, num2)
                else:
                    # Otherwise, check if the result matches the expected values
                    result = math_operation(num1, operator, num2)
                    problem, answer = result
                    self.assertEqual(problem, expected_problem)
                    self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()