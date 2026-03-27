counter = 0
while (counter < 5):
    print(str(counter) +" Hello!")
    counter += 1
print("\nDone!")


User_input = input("Enter input: ")
while User_input != "exit":
    User_input = input("Enter input: ")


'''
# prompt once before the loop
User_input = input("Enter input (or type exit to quit): ")
while User_input.lower() != "exit":
    # gather several pieces of information each iteration
    name = input("Enter your name: ")
    age  = input("Enter your age: ")
    city = input("Enter your city: ")

    print(f"Hello {name}, you are {age} years old and live in {city}.")

    # ask if user wants to continue or exit
    User_input = input("Type 'exit' to stop or press Enter to continue: ")
'''