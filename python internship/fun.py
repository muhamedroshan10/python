def my_function():
    print("my name is soummmbiiii")

my_function()


def add_num(a,b):
    sum=a+b
    return sum
num1=25
num2=45
print("the sum is",add_num(num1,num2))

def divide_num(c,d):
    divide=c/d
    return divide
num1=10
num2=5
print("the divide is",divide_num(num1,num2))

def check_odd_even(number):
    if number % 2 ==0:
        return "even"











def find_square(num):
    result=num * num
    return result 
square=find_square(3)

print(square)




def find_cube(num):
    result=num*num*num
    return result
cube=find_cube(2)

print(cube)




# def add_numbers(a=7,b=8):
#     sum=a+b
#     ("sum",sum)


def find_sum(*numbers):
    result = 0
    for num in numbers:
        result = result + num 

    print("sum =",result)
find_sum(1,2,3)
find_sum(4,9)

   