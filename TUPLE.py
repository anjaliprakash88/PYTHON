empty_tuple = ()
print(empty_tuple)

# Creating tuple having integers
int_tuple = (4, 6, 8, 10, 12, 14)
print(int_tuple)

# Creating a tuple having objects of different data types
mixed_tuple = (4, "Python", 9.3)
print(mixed_tuple)

# Creating a nested tuple
nested_tuple = ("Python", {4: 5, 6: 2, 8: 2}, (5, 3, 5, 6))
print(nested_tuple)
print(type(nested_tuple))

tuple_ = ("Python", "Tuple", "Ordered", "Collection")
print(tuple_[0])
print(tuple_[1])
nested_tuple = ("Tuple", [4, 6, 2, 6], (6, 2, 6, 7))
# Accessing the index of a nested tuple
print(nested_tuple[0][3])
print(nested_tuple[1][1])


tuple_ = ("Python", "Tuple", "Ordered", "Collection")
print(tuple_[-1])
print(tuple_[-4])


tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")
print(tuple_[1:3])
print(tuple_[:-4])
print(tuple_[:])

tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Objects")
del tuple_

tuple_ = tuple_ * 3

T1 = (0, 1, 5, 6, 7, 2, 2, 4, 2, 3, 2, 3, 1, 3, 2)
res = T1.count(2)

tuple_ = ("Python", "Tuple", "Ordered", "Immutable", "Collection", "Ordered")
print('Tuple' in tuple_)
print('Immutable' not in tuple_)


tuple_ = ("Python", "Tuple", "Ordered", "Immutable")
for item in tuple_:
    print(item)


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
