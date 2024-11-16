# exercise seven, some counting

# loop that counts up from 0 to 50 in increments of 1.
print("Counting up from 0 to 50: ") # title before numbers generated
for i in range(0,51,1): # using for i in range function for range of numbers being counted
    print(i, end = " . ") # each number is seperated by a "."
print()
print() # 2 new lines before next code

# loop that counts down from 50 to 0 in decrements of 1.
print("Counting down from 50 to 0: ")
for i in range(50,-1,-1):
    print(i, end = " . ")
print()
print()

# loop that counts up from 30 to 50 in increments of 1.
print("Counting up from 30 to 50:")
for i in range(30,51,1):
    print(i, end = " . ")
print()
print()

# loop that counts down from 50 to 10 in decrements of 2.
print("Counting down from 50 to 10 by a decrement of 2")
for i in range(50,9,-2):
    print(i, end = " . ")
print()
print()

# loop that counts up from 100 to 200 in increments of 5.
print("Counting up from 100 to 200 by an increment of 5")
for i in range(100,201,5):
    print(i, end = " . ")
