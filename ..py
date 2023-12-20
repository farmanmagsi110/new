# num1=int(input("Enter a number"))
# num2=int(input("Enter a number"))
# if num1 % 2==1 and num2 % 2==1:
#     result=(num*num1)+(num2*num2)
#     print(result)
# else:
#     print("calculation is not performed")


# def factorial(n):
#     # Check if the input is negative
#     if n < 0:
#         print("Factorial is not defined for negative numbers.")
#         return None
    
#     result = 1
#     while n > 1:
#         result *= n
#         n -= 1
#     return result

# # Input from the user
# num = int(input("Enter a number: "))

# # Calculate and print the factorial
# result = factorial(num)
# if result is not None:
#     print(f"The factorial of {num} is {result}.")

# import random

# def number_guessing_game():
#    secret_number = random.randint(1, 100)
#    attempts = 5

#    for  aatempt in range(attempts):
#       guess = int(input("Guess the number (between 1 and 100:"))

#       if guess == secret_number:
#          print("Congratulations! you guessed the number.")

#          break
#       elif guess < secret_number:
#          print("Too low. try again.")
         
#       else:
#          print("Too high. Try again.")
#    else:
#        print("Game over! You ran out of guesses. The correct number was:", secret_number) 

# number_guessing_game()


num_people = int(input("Enter the number of people:"))
cost_per_meal = float(input("Enter the cost of each meal:"))
tip_percentage = float(input("Enter the  tip percentage:"))
sales_tax_percentage = float(input("Enter the sales tax percentage:"))



total_cost_of_food = num_people * cost_per_meal
total_sales_tax = total_cost_of_food * (sales_tax_percentage/100)
total_tip_amount = total_cost_of_food * (tip_percentage / 100)
total_bill_amount_per_person = (total_cost_of_food + total_sales_tax + total_tip_amount) / num_people

print(f"\nTotal cost of Food: ${total_cost_of_food:.2f}")
print(f"Total Sales Tax: ${total_sales_tax:.2f}")
print(f"Total Tip Amount: ${total_tip_amount:.2f}")
print(f"total Bill Amount per Person: ${total_bill_amount_per_person:.2f}")












    



