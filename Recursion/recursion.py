def factorial(number: int):
    if number == 1:
        # Base case
        return 1
    return number * factorial(number - 1)


if __name__ == "__main__":
    print(factorial(7))
    print(factorial(2))
    print(factorial(1))
