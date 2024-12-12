# function without arguments without return value
def add():
    num1 = 12
    num2 = 23
    res = num1 + num2
    print(res)


add()


# function with arguments without return value
def add(num1, num2):
    res = num1 + num2
    print(res)


num1 = int(input("enter the number"))
num2 = int(input("enter the number"))
add(num1, num2)


# function with arguments with return value
def add(num1, num2):
    res = num1 + num2
    return res


x = add(12, 45)
# print(add(12, 45))
print(x)


# function without arguments with return value
def Add():
    num1 = 12
    num2 = 23
    res = num1 + num2
    return res


x = Add()
print(x)


# Default arguments
def print_name(name="anjali"):
    print("hello", name)


print_name("achu")
