string = "Python Exceptions"

for s in string:
    if (s != o:
        print( s )

string = "Python Exceptions"

for s in string:
    if (s != o):
        print( s )



a = ["Python", "Exceptions", "try and except"]
try:
     for i in range(4):
        print(a[i])
except NameError:
    print ("Index out of range")
else:
    print("not error occured")
finally:
    print("okayy")

num = [3, 4, 5, 7]
if len(num) > 3:
    raise Exception(f"Length of the given list must be less than or equal to 3 but is {len(num)}")