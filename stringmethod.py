# # Using single quotes
# str1 = 'Hello Python'
# print(str1)
# print(type(str1))
# #
#
# # Using double quotes
# str2 = "Hello Python"
# print(str2)
# print(type(str2))
#
#
# # # Using triple quotes
# str3 = '''Triple quotes are generally used for
#     represent the multiline or

#     docstring'''
# print(str3)

# str = "HELLO"
# print(str[0])
# print(str[1])
# print(str[2])
# print(str[3])
# print(str[4])

# syntax: [start: stop: step]
#
# str = "JAVATPOINT"
# # Start Oth index to end
# print(str[0:])
# # Starts 1th index to 4th index
# print(str[1:5])
# # Starts 2nd index to 3rd index
# print(str[2:4])
# # Starts 0th to 2nd index
# print(str[:3])
# #Starts 4th to 6th index
# print(str[4:7])
# print(str[::2])

# str = 'JAVATPOINT'
# print(str[-1])
# print(str[-3])
# print(str[-2:])
# print(str[-4:-1])
# print(str[-7:-2])
# # Reversing the given string
# print(str[::-1])

#
# # Reassigning Strings
# str = "HELLO"
# print(str)
# str = "hello"
# print(str)


#
# Deleting the String
# str1 = "JAVATPOINT"
# del str1
# print(str1)

# String Operators
# str = "Hello"
# str1 = " world"
# print(str*3)
# print(str+str1)
# print('w' in str)
# print('wo' not in str1)

# String capitalize() Method
# converts first character of the string into uppercase
# str = "hello python"
# str2 = str.capitalize()
# print(str)
# print(str2)



# # String Casefold() Method
# # Casefold() method returns a lowercase copy of the string
# str = "PYTHON"
# str2 = str.casefold()
# print(str)
# print(str2)




# # String Count() Method
# str = "ab bc ca de ed ad da ab bc ca"
# oc = str.count('a')
# print("occurences:", oc)



# # String find() Method
# # it print its index number
# str = "Hello, world!"
# sub = "world"
# index = str.find(sub)
# print(index)


# String isalnum() Method
# # to check given character is alpha-numeric character
# str = "Welcome"
# str2 = str.isalnum()
# print(str2)



# # String upper() Method
# # Python upper() method converts all the character to uppercase and returns a uppercase string.
# str = "anjali"
# str2 = str.upper()
# print(str2)


# String swapcase() Method
# Python swapcase() method converts case of the string characters from uppercase to lowercase and vice versa.
# str = "HELLO PYTHON"
# str2 = str.swapcase()
# print (str2)


# String split() Method
# Python split() method splits the string into a comma separated list. It separates string based on the separator delimiter.
# string = "Hello World"
# result = string.split(" ")
# print(result)


# String replace() Method
# # Return a copy of the string with all occurrences of substring old replaced by new.
# str = "Java is a programming language"
# str2 = str.replace("Java","C")
# print(str)
# print(str2)



# String lower() Method
# Python lower() method returns a copy of the string after converting all the characters into lowercase.
# str = "PYTHON"
# str = str.lower()
# print(str)



# String join() Method
# lis = ['Hello', 'World', 'Python', 'Programming']
# r = ' '.join(lis)
# print(r)



# The len() function returns the length of a string:
# a = "Hello, World!"
# print(len(a))


# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())

 # returns "Hello, World!"