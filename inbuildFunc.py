#Lambda Function

'''def addition(num1, num2):
    sum = num1 + num2
    return sum'''


'''lambda num1, num2: num1 + num2

y = lambda r : "Even" if r%2 == 0 else "Odd"
r = int(input("Enter a number: "))

print(y(r))'''


#filter function
def identifyEven(num):
    if num%2 == 0:      #return num%2 == 0
        return True
    else:
        return False
    
response1 = list(filter(identifyEven, range(1, 11)))
print(response1)


#map function
def getDouble(num):
    return num*3
    
response = list(map(getDouble, range(1, 11)))
print(response)

#reduece function
from functools import reduce

def addition(num1, num2):
    return num1 + num2

response = reduce(addition, [5,6,7,8,9,10])
print(response)

response = reduce(lambda a, b: a * b, [5,6,7,8,9,10])
print(response)

