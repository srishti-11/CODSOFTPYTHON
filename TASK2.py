print("CALCULATOR")
num1 = int(input("Enter your first number "))
num2 = int(input("Enter your second number "))
opr = input("Enter the operator (+ , - , * , /) ")
if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1*num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("Invalid input") 