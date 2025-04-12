def calculator(a: int, b: int, op: str) -> int | float:
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation.")


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

print(f"Result: {calculator(first_number, second_number, operation)}")