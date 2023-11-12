import random


def random_integer_generator(min, max):
    """
    Generate a random integer between min_value and max_value.

    Args:
        min (int): The minimum value for the random integer.
        max (int): The maximum value for the random integer.

    Returns:
        int: A randomly generated integer.
    """
    return random.randint(min, max)


def random_operator_generator():
    """
    Generate a random operator among '+' ,'-' and '*'.

    Returns:
        str: A randomly chosen arithmetic operator.
    """
    return random.choice(['+', '-', '*'])


def math_problem_evaluator(operand1, operand2, operator):
    """
    Evaluate a math problem based on the given operands and operator.

    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operator (str): The arithmetic operator ('+', '-', or '*').

    Returns:
        tuple: A tuple containing the math problem as a string and its correct answer.
    """
    # Create a string representation of the math problem
    problem = f"{operand1} {operator} {operand2}"

    # Evaluate the correct answer based on the operator
    if operator == '+':
        answer = operand1 + operand2
    elif operator == '-':
        answer = operand1 - operand2
    else:
        answer = operand1 * operand2
    return problem, answer


def math_quiz():
    """
    Conduct a math quiz by presenting problems to the user and collecting their answers.

    Prints the problems, collects user input, compares with correct answers, and updates the score.

    Returns:
        None
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate random operands and operator
        operand1 = random_integer_generator(1, 10)
        operand2 = random_integer_generator(1, 5)
        operator = random_operator_generator()

        # Evaluate the math problem
        PROBLEM, ANSWER = math_problem_evaluator(operand1, operand2, operator)
        print(f"\nQuestion: {PROBLEM}")

        # Error handling for user input
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            user_answer = None

        if user_answer is not None:
            #Compare user's answer with the correct answer and update the score
            if user_answer == ANSWER:
                print("Correct! You earned a point.")
                score += 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
