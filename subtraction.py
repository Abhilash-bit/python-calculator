
MIN_VALUE = -100
MAX_VALUE = 100

num1 = float(input(f"Enter first number ({MIN_VALUE} to {MAX_VALUE}): "))
if not (MIN_VALUE <= num1 <= MAX_VALUE):
    print(f"Error: Number must be between {MIN_VALUE} and {MAX_VALUE}")
    exit()

num2 = float(input(f"Enter second number ({MIN_VALUE} to {MAX_VALUE}): "))
if not (MIN_VALUE <= num2 <= MAX_VALUE):
    print(f"Error: Number must be between {MIN_VALUE} and {MAX_VALUE}")
    exit()

result = num1 - num2

print("The difference is:", result)
