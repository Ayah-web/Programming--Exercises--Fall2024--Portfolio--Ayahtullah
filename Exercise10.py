# exercise ten, is it even?

# asks user input
number = int(input("Please enter a number in order to find out whether it is even or odd:"))

if number % 2 == 0:
    print(f"{number} is an even number!!")
else:
    print(f"{number} is an odd number!!")
    
# def function and if-else statement on whether number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is an even number!"
    else:
        return f"{number} is an odd number!"
    
# def main() function
def main():
    # asks for user input in integer type
    user_number = int(input("Please enter a number, in order to find out whether it is even or odd"))
    
    # try function
    try:
        number = int(user_number)
        
        result = check_even_or_odd(number)
        
        # print result
        print(result)
        # if input is not an integer
    except ValueError:
        print("Invalid. Please enter an integer only!")
 
 # calling main function       
if __name__ == " __main__":
    main()