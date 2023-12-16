# num1=int(input("Enter a number"))
# num2=int(input("Enter a number"))
# num3=int(input("Enter a number"))

# if num1>num2:
#     print("Number1 is greater than num2")
# elif num2>num1:
#     print("Num2 is greater than num1")
# elif num1>num3:
#     print("Num1 greater than num3")
# else:
#     print("All are equal")


number1= input("please enter first number:")
number2= input("please enter  second number:")
operator= input("Select any operator: , +,- ,/, *: ")

number1= int(number1)
number2= int(number2)

if operator== '+':
    print(number1+number2)
elif operator=='-':
    print(nmber1-number2)
elif operator=='*':
    print(number1 * number2)
elif operator=='/':
    print(number1/number2)
else:
    print("Please Select valid operator")
