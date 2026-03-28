'''

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

'''

'''
#exception handling...
print("Start")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("The result is:", result)
except Exception as e:
    print(f"Error: {str(e)}")

print("End")'''


print("Start")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter valid integers.")

except Exception as e:
    print(f"An unexpected error occurred: {str(e)}")

finally:
    print("Calculation completed.") #The finally block is always run if there is error or not.

print("End")