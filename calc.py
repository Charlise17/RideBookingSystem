def calc():
    print(
        "=" * 51, "\n",
        "MENU".center(51), "\n",
        "=" * 51,
        "\n\t 1. Addition",
        "\n\t 2. Subtraction",
        "\n\t 3. Multiplication",
        "\n\t 4. Division",
        "\n\t 5. Modulus",
    )

    def add(x, y): return x + y
    def subtract(x, y): return x - y
    def multiply(x, y): return x * y
    def divide(x, y): return "Math Error: Cannot divide by zero." if y == 0 else x / y
    def modulus(x, y): return "Math Error: Cannot calculate modulus by zero." if y == 0 else x % y
    operations = [add, subtract, multiply, divide, modulus]
    operation_names = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus"]
    while True:
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            if not 1 <= choice <= 5:
                print("Calculator Error: Invalid operation choice.")
                raise ValueError
        except ValueError:
            if input("Press y or Y to try again: ").lower() != "y":
                break
            continue
        while True:
            try:
                x, y = map(int, input("Enter your two numbers: ").split())
                break
            except ValueError:
                print("Error: Please enter two valid numbers.")
        result = operations[choice - 1](x, y)
        print(f"{operation_names[choice - 1]} Result: {result}")

        if input("Press y or Y to continue: ").lower() != "y":
            break
# Run the calculator
calc()
if __name__ == '__main__' :
    main()

