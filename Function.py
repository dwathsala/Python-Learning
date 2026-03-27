"""def addition(num1, num2):
    sum = num1 + num2
    return sum

a = input("Enter first number: ")
b = input("Enter second number: ")

result = addition(int(a), int(b))
print(result)

'''result =addition(5, 10)
print(result)'''

print(addition(5, 10))"""


"""def Calc_Grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"  
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
    
student_marks = int(input("Enter the marks: "))
grade = Calc_Grade(student_marks)
print(grade)

student_marks = int(input("Enter the marks: "))
grade = Calc_Grade(student_marks)
print(grade)"""

#variable length arguments
"""def intro(name, age, *marks):
    msg = f"My name is {name} and I am {age} years old. My marks are: {marks}"
    total = sum(marks)
    print(total)
    return msg

response = intro("Alice", 25, 85, 90, 78)
print(response)"""


#keyword arguments with variable length arguments
def intro(name, age, **details):
    msg = f"My name is {name} and I am {age} years old. My details are: {details}"
    return msg  

response = intro("Alice", 25, city="New York", profession="Engineer")
print(response)