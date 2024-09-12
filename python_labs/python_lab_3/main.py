import argparse
import numpy as np
import os
import math

def main(number: int) -> None:
    # Creating an array of numbers from 1 to n and cube them
    cubes = np.arange(1, number + 1) ** 3

    # Filter out cubes where the first digit is even
    # Convert cubes to strings, take the first character, convert back to int and check if even
    even_first_digit_cubes = cubes[np.array([int(str(cube)[0]) % 2 == 0 for cube in cubes])]

    # Sum the filtered cubes
    total_sum = np.sum(even_first_digit_cubes)

    print(f"cube({number}) = {total_sum}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Cube Counter")
    parser.add_argument("--n", type=int, required=True, help="Input a number to sum the cube counts")
    arguments = parser.parse_args()
    main(arguments.n)
