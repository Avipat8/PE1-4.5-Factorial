def factorial(n):
    """
    Recursive function to calculate the factorial of a number.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number.
    """
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    else:
        return n * factorial(n - 1)


def main():
    """
    Main function to drive the program.
    """
    # Prompt the user for a non-negative integer
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            # Calculate the factorial
            result = factorial(num)
            # Display the result
            print(f"The factorial of {num} is: {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


# Launch the program
if __name__ == "__main__":
    main()