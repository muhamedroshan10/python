# a=10
# b=20
# print("addition of 2 numbers:",a+b)

# str1 = 'Hello'
# str2 = 'Python'
# print('concatenation of 2 strings:',str1 + str2)

# list1 = [1,2,3]
# list2 = ['A','B']
# print('concatenation of 2 lists:', list1 + list2)


# print(len("hello friends"))
# print(len(["python","java","C++","C#"]))
# print(len({"Name":"thundarii","Age":542,"City":"Angamaaly"}))


#method overriding

# class shape:
#     def area(self):
#         return 0
# class Circle(shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14 * self.radius **2
# circle=Circle(radius=2)
# print(circle.area())



# class shape:
#     def area(self):
#         return 0
# class square(shape):
#     def __init__(self,length):
#         self.length=length
#     def area(self):
#         return self.length **2
# square=square(length=2)
# print(square.area())


#program to illustrate public access modifier in 



class Geek:
    def __init__(self, name,age):
        self.geekName = name 
        self.geekAge = age 
    def displayAge(self):
        print("Age:", self.geekAge)
obj = Geek("kettyol", 27)
print("Name: ",obj.geekName)
obj.displayAge()

