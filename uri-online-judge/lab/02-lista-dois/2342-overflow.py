maxNumber = int(input())
numberA, operation, numberB = input().split()

if operation == "+":
    numberC = int(numberA) + int(numberB)
elif operation == "*":
    numberC = int(numberA) * int(numberB)

if numberC > maxNumber:
    print("OVERFLOW")
else:
    print("OK")
