import unittest
from math_quiz import random_integer_generator, random_operator_generator, math_problem_evaluator


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if the generated operator is one of '+', '-', or '*'
        operators = set()
        for _ in range(1000):  # Test a large number of random values
            operator = random_operator_generator()
            operators.add(operator)
            self.assertIn(operator, {'+', '-', '*'})

        # Ensure all three operators are present at least once
        self.assertEqual(operators, {'+', '-', '*'})

    def test_function_C(self):
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '*', '8 * 3', 24),
            (10, 4, '-', '10 - 4', 6),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = math_problem_evaluator(num1, num2, operator)

            # Check if the generated problem and answer match the expected values
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
