# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# n= int(input("enter a number"))
# re = fact(n)
# print(re)


def display(num):
    if num > 0:
        print(num)
        display(num-1)

display(5)




