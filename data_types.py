# Integer

a = 10
b = -5
c = 1254833454442121545488997121215876111469

print(a) 
print(type(a))
print(c.__sizeof__())
print(a.__sizeof__())

print('\n')

# Float

x = 3.14

print(x)
print(type(x))
print(x.__sizeof__())

print('\n')

# boolean
p = True
q = False

print(p)
print(type(p))
print(p.__sizeof__())

print('\n')

# complex
z = 2 + 3j
print(z)
print(type(z))
print(z.__sizeof__())

print('\n')

print(z.real)
print(z.imag) 

y = complex(2, 3)
print(y)

print(id(z))
