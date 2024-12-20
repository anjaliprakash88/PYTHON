# Lambda Functions in Python are anonymous functions,
# A lambda function can take number of arguments at a time.But it returns only one argument at a time.
#
#
# Syntax
# lambda arguments: expression

a = lambda num: num + 4
print(a(6))

a = lambda x, y: (x * y)
print(a(4, 5))

a = lambda x, y, z : (x + y + z)
print(a(4, 5, 5))

# Using Lambda Function with filter()
list_ = [35, 12, 69, 55, 75, 14, 73]
odd_list = list(filter(lambda num: (num % 2 != 0), list_))
print('The list of odd number is:', odd_list)

# Using Lambda Function with map()
numbers_list = [2, 4, 5, 1, 3, 7, 8, 9, 10]
squared_list = list(map( lambda num: num ** 2 , numbers_list ))
print( 'Square of each number in the given list:' ,squared_list)

# Using Lambda Function with if-else
Minimum = lambda x, y: x if (x < y) else y
print('The greater number is:', Minimum(35, 74))