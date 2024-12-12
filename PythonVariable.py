# # declaring variable
# a = 50
# b = a
# a = 25
#
# # multi-word keywords
# # Camel Case
# nameOfStudent = "ABC"
#
# # Pascal Case
# NameOfStudent = "ABC"
#
# # Snake Case
# name_of_student = "ABC"
#
# # Multiple Assignment
# # Assigning single value to multiple variables
# x = y = z = 50
# print(x)
# print(y)
# print(z)
# # Assigning multiple values to multiple variables
# a, b, c = 5, 10, 15
# print(a)
# print(b)
# print(c)

# # Variable Types
# # Local Variable
# def add():
#     a = 20
#     b = 30
#     c = a + b
#     print("The sum is:", c)
#
#
# add()
#
# # Global Variables
# x = 101
#
#
# def mainFunction():
#     print(x)
#
#
# mainFunction()
# print(x)
#
#
# # -----------------------------#
#
# def mainFunction():
#     global x
#     x = 10
#     print(x)
#
#
# mainFunction()
# print(x)

# Delete a variable
x = 10
del x
print(x)
