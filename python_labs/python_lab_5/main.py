import argparse

def is_palindrome(inputString):
    """
    Checks if the given string representation of an integer is a palindrome.
    Prints 'True' if it is a palindrome, 'False' otherwise.
    """
    # Reverse the whole string
    reversed_string = inputString[::-1]
    
    # Check if the original string is equal to its reverse
    if inputString == reversed_string:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    argumentParser = argparse.ArgumentParser(description="Check if an integer is a palindrome.")
    argumentParser.add_argument("--x", type=int, help="Integer to check")
    parsed = argumentParser.parse_args()
    
    # Convert the integer to a string and pass it to the function
    inputString = str(parsed.x)
    is_palindrome(inputString)
