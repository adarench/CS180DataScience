import argparse

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)

def main():
    parser = argparse.ArgumentParser(description="Calculate mean and variance")
    parser.add_argument('--array', nargs='+', type=float, required=True, help="Input array of numbers")
    args = parser.parse_args()

    numbers = args.array
    mean = calculate_mean(numbers)
    variance = calculate_variance(numbers, mean)

    print(f"mean = {mean}")
    print(f"variance = {variance}")

if __name__ == "__main__":
    main()
