"""
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""


def main():
    user_input = int(input("Please enter number of digits: "))
    first_number = 0
    second_number = 1

    i = 2
    while True:
        sum = first_number + second_number
        first_number = second_number
        second_number = sum

        digit_count = len(str(sum))

        if digit_count == user_input:
            print(f"Digit count is {digit_count} for fibonacci number {i}")
            break
        i += 1


if __name__ == "__main__":
    main()
