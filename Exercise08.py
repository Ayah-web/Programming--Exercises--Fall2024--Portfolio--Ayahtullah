# exercise eight, simple search

# list of names
names = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]

# predifined value
search_term = "Sam"

# if else statement on whether search term is in list
if search_term in names:
    print(f"{search_term} is found in this list")
else:
    print(f"{search_term} is not found in this list")
    
# user input instead of predefined value
user_input = input("Enter a name that you want to search: ")

#if-else statement wether user input is in the list
if user_input in names:
    print(f"{user_input} is found in this list")
else:
    print(f"{user_input} is not found in this list")
