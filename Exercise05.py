# exercise five, days of the month

# defining a dictionary for the days in each month in a normal year
# each month is represented by their number of order
days_in_month = {
    # jan
    1 : 31,
    
    # feb
    2 : 28,
    
    # mar
    3 : 31,
    
    # apr
    4 : 30,
    
    # may
    5 : 31,
    
    # june
    6 : 30,
    
    # july
    7 : 31,
    
    # aug
    8 : 30,
    
    # sept
    9 : 31,
    
    # oct
    10 : 30,
    
    # nov
    11 : 31,
    
    # dec
    12 : 30
}

# days in february in leap year
feb_in_leap = 29

# asks user for a month corresponding with number
month_number = int(input("Please enter a month (from 1-12): "))

# validating user's month input
if month_number < 1 or month_number > 12:
    print("Invalid number of a month! Please enter a number between 1 and 12.")
else: # asks user if it is a leap year
    if month_number == 2:
        leap_year = str(input("Is it a leap year?(Y/N) "))
        yes = "y"
        if leap_year.lower() == yes: # if it is a leap year, gives number of days
            print(f"February has {feb_in_leap} days!")
        else: # if not a leap year
            print("February has 28 days!")
    else: # the rest of the months' days
        print(f"This month has {days_in_month[month_number]} days")
        
