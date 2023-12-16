print("1.sign Up")
print("2.sign In")

signup_password = "admin"
signin_username = "0789"

yes ='y'

while yes =='y':
    print("1.Sign Up")
    print("2.Sign In")


    val = input("Select an Option: ")


    if val == "1":

        print("sign Up")
        print("Create Account")

        signup_username = input("Enter username: ")
        signup_password = input("Enter password: ")
        print("Your account has been created successfully")


    elif val == "2":
        print("Sign In")
        login_username = input("Enter your username: ")
        login_password = input("Enter your password: ")
        

        if signup_username == login_username and signup_password == login_password:
            print("Logged In")
    #

    else:
        print("invalid Option")


        print("thank for using ATM")