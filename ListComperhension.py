Person = ["Piyali", "Hiya", "Rudrashish", "Badsha", "Lipi"]
newlist = [x for x in Person if "i" in x]
print(newlist)

numbers = [3, 5, 1, 7, 3, 9]
num = [n ** 2 for n in numbers]
print(num)

letters = [alpha for alpha in 'javatpoint']
print(letters)

number_list = [num for num in range(30) if num % 2 != 0]
print(number_list)