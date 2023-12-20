# a= 1.0
# b= "1"
# c= "1.1"
# a + float(b)
# float(b) + float(c)
# a + int(c)
# a + int(float(c))
# int(a) + int(float(c))
# 2.0 * b

# a,b= 'red' ,'blue'
# a,b=b,a
# print(a,b)

# a='10'
# print(a+a)

# str = 'hello world!'
# print (str)
# print(str[0])
# print(str[2:5])
# print(str[2:])
# print(str * 2)
# print(str + "Test")


# First_name="farman"
# last_name="ali"
# print("First name is: farman")
# print("last name is: ali")


# first_name=input("Enter  first name")
# last_name=input("Enter  last name")
# print("welcome:farman ali")
# len_of_first_name=len(first_name)
# len_of_last_name=len(last_name)
# print("Length of first name is : ", len_of_first_name)
# print("Length of last name is : ", len_of_last_name)


# a=input("Enter first number")
# b=input("Enter second number")
# print()
# a+b
# a-b
# a*b
# a/b 

# num1= float(input("Enter the first number:"))
# num2= float(input("Enter the second number:"))

# addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2

# if num2 !=0:
#     division = num1/num2
# else:
#     division = "Undefined (division by zero)"

# print(f"additon: {addition}")
# print(f"subtraction: {subtraction}")
# print(f"multiplication: {multiplication}")
# print(f"division: {division}")

# user_input=input("Enter something")

# data_type= type(user_input)
# print(f"The type of '{user_input}' is :{data_type}")

user_input= ("Enter a number:")
try:
    integer_value= int(user_input)
    print(f"Integer value: {integer_value}")

    float_value = float(user_input)
    print(f"Float value: {float_value}")

    string_value = str(user_input)
    print(f"String value: '{string_value}'")

# except valueError:
    # print("Invalid input. Please enter a valid number.")
