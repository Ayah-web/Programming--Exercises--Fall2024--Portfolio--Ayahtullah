# exercise six, brute force attack

# variable for correct password
correct_password = "12344"

# the maximum attempts a user can have and attempts
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    # asks user for the correct password
    user_input = input("Please enter the correct password: ")
    
    # if-else statement on whether user has inputed the correct password or not
    if user_input == correct_password:
        print("You have been granted access!")
        break
    else: # decreasing in attempts after inputs
        attempts += 1
        attempts_remaining = max_attempts - attempts
        
        # if-else statement on whether user has attempts remaining or not
        if attempts_remaining > 0:
            print(f"The password you have entered is incorrect! You have {attempts_remaining} attempts left!")
        else: # alerting the authorities after user has exhausted inputs of password
            print("No attempts left. The authorities have been alerted. Please standby.")