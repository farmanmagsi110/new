# num1=int(input("Enter a number"))
# num2=int(input("Enter a number"))
# if num1 % 2==1 and num2 % 2==1:
#     result=(num*num1)+(num2*num2)
#     print(result)
# else:
#     print("calculation is not performed")


def factorial(n):
    # Check if the input is negative
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Input from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
result = factorial(num)
if result is not None:
    print(f"The factorial of {num} is {result}.")
















    



