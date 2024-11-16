# exercise three, biography

# my dictionary
my_dict = {
    "Name": "Ayahtullah",
    "Hometown":"Taguig and Al Haram",
    "Age":17
}

# prints my dictionary in seperate lines
print("\n".join(f"{key}:{value}" for key, value in my_dict.items()))

#advanced exercise three

# asks user for name
name = str(input("What's your name? ")).strip().title()

# greets user
print(f"Hello, {name}")

# asks for user's hometown
hometown = str(input("What's your hometown?")).strip().title()

# comments on input of hometown
print("That's cool!!")

# asks for user's age
age = int(input("What's your age? "))

# comment on user's age
print("Alrighty!")

# end of primitive quiz
print("Thank you for participating in this mini quiz!!")




