# exercise four, primitive quiz

# variables for france
question = input("What is the capital of France? ")
correct_answer = "paris"

# if-else statement, .lower() used to accept any type of capitalization of input
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for portugal
question = input("What is the capital of Portugal? ")
correct_answer = "lisbon"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for spain
question = input("What is the capital of Spain? ")
correct_answer = "madrid"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for ireland
question = input("What is the capital of Ireland? ")
correct_answer = "dublin"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for italy
question = input("What is the capital of Italy? ")
correct_answer = "rome"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for belarus
question = input("What is the capital of Belarus? ")
correct_answer = "minsk"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for iceland
question = input("What is the capital of Iceland? ")
correct_answer = "reykjavik"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for malta
question = input("What is the capital of Malta? ")
correct_answer = "valleta"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for monaco
question = input("What is the capital of Monaco? ")
correct_answer = "monaco"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for montenegro
question = input("What is the capital of Montenegro? ")
correct_answer = "podgorica"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# variables for albania
question = input("What is the capital of Albania? ")
correct_answer = "tirana"

# if-else statement
if question.lower() == correct_answer:
    print("Correct answer!")

else:
    print("Wrong answer!")
    
# extra, i made the primitive quiz for france looped

# defining
def quiz():
    # variables for france
    correct_answer = "paris"  
    question = "What is the capital of France?" 

    # using while for infinite looping
    while True: 
        # asks the user the question 
        user_answer = input(question + " ")  

        # if-else statement and .lower() used for user input
        if user_answer.lower() == correct_answer:  
            print("Correct! Moving to the next question.")
            # makes the user exit loop when answer is correct
            break 
        else:  
            print("Wrong answer! Try again?")  

# calling the quiz funtion
quiz()


    
