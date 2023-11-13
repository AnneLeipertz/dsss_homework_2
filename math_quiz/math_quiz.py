import random


def random_int(min, max):
    """
    Generate a random integer within the specified range.

    Parameters:
    - min (int): The minimum value of the range (inclusive).
    - max (int): The maximum value of the range (inclusive).

    Returns:
    int: A random integer within the specified range.
    """

    return random.randint(min, max)


def random_operator():
    """
    Choose a random mathematical operator from the set {+, -, *}.

    Returns:
    str: A randomly selected mathematical operator.
    """
    return random.choice(['+', '-', '*'])


def math_operation(randInt1, operator, randInt2):
    """
    Perform a mathematical operation on two integers.

    Parameters:
    - randInt1 (int): The first operand.
    - operator (str): The mathematical operator.
    - randInt2 (int): The second operand.

    Returns:
    tuple: A tuple containing the formatted problem string and the result of the operation.
    """
    output = f"{randInt1} {operator} {randInt2}"
    
    if operator == '+': result = randInt1 + randInt2
    elif operator == '-': result = randInt1 - randInt2
    else: result = randInt1 * randInt2
    return output, result

def math_quiz():
    """
    Run a math quiz game.

    The game presents math problems to the user and checks their answers and 
    at the end prints the user's score of the game.

    Side Effects:
        Prints prompts to the console.

    Raises:
        ValueError: If the user does not enter a valid integer.

    Examples:
        >>> math_quiz()
        Welcome to the Math Quiz Game!
        You will be presented with math problems, and you need to provide the correct answers.
        
        Question: 3 + 4
        Your answer: 7
        Correct! You earned a point.
        
        ...
        
        Game over! Your score is: 8/10
    """
    quizScore = 0
    taskNumbers = 10
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")
    
    for i in range(taskNumbers):
        randInt1 = random_int(-10, 10); randInt2 = random_int(-10, 10); operator = random_operator()
        
        PROBLEM, ANSWER = math_operation(randInt1, operator,randInt2)
        print(f"\nQuestion: {PROBLEM}")
        
        # Allow the user to attempt answering the question (up to 5 attempts)
        attempts = 0
        while attempts < 5:
            useranswer = input("Your answer: ")
            try:
                useranswer = int(useranswer)
                break  # Break the loop if the conversion to int is successful
            except ValueError:
                print("Your given answer must be an integer. Please try again.")
            attempts += 1 
        
        # If the user reaches the maximum attempts, end the quiz
        if attempts ==5:
            print("Too many invalid attempts. The math quiz will stop now.")
            return
        
        useranswer = int(useranswer)
        
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            quizScore += 1

        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
    
    print(f"\nGame over! Your score is: {quizScore}/{taskNumbers}")

if __name__ == "__main__":
    math_quiz()

    
  