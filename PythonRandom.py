import random
num=random.random()
print(num)


num = random.randint(1, 500)
print(num)


num = random.randrange(1, 10)
print( num )
num = random.randrange(1, 10, 2)
print( num )




list1 = [34, 23, 65, 86, 23, 43]
random.shuffle( list1 )
print( list1 )


import os

# posix', 'nt', 'os2', 'ce', 'java' and 'riscos'.
print(os.name)

os.mkdir("d:\\newdir")

print(os.getcwd())