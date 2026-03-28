#Logical errors

number = int(input("Enter a number: "))

if number > 3:  #1 and 2 are not greater than 3, but they are positive numbers. This condition will not correctly identify all positive numbers.
    print("The number is positive.")
else:
    print("The number is not positive.")


#Logical errors
file = open("hello.txt", "r") #If there is no file named "hello.txt" in the same directory as this script, this will raise a FileNotFoundError.it is run time error

content = file.read()
print(content)

file.close()