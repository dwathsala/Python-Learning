#overriding....
class parent:
    x = 50
    def display(self):
        print("This is the parent class method")

class child(parent): #inherite child class from parent class
    x=100 #overriding parent class variable in child class
    def display(self): #overriding parent class method in child class
        print("This is the child class method")

obj1 = child()
print(obj1.x) #accessing parent class variable using child class object
obj1.display() #calling overridden method


#overloading....
class subjectMarks:
    def total_marks(self, sub1, sub2):
        print(sub1+sub2)

    def total_marks(self, sub1, sub2, sub3):
        print(sub1+sub2+sub3)

obj = subjectMarks()
#obj.total_marks(50, 60)

obj.total_marks(50, 60, 70) #this will call the second method as it has three parameters