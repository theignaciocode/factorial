def factorial(number: int) -> int:
    factorial = 1
    for i in range(number, 0, -1):
        factorial *= i
    return factorial

print(factorial(5))     # 120
print(factorial(12))    # 479001600

# developer: theIGNACIOcode
