empty_list = []
list_of_numbers = [0,1,2,3,4,5]
my_favourite_fruits = ["pineapples", "oranges", "bananas"]
mixed_list = [15, "sunshine", "jumper", 4, "sky"]

print(my_favourite_fruits)

print("oranges" in my_favourite_fruits)
my_favourite_fruits.append("apples")
print("apples" in my_favourite_fruits)
print(my_favourite_fruits)

big_list = list_of_numbers + mixed_list
print(big_list)

big_list.pop()
print(big_list)

big_list.pop()
print(big_list)

for item in big_list:
    print(item)

for integer in range(10):
    print(integer*integer)

color = ["pink", "blue"]
# eg enumerate gives you the index of the value
for color, index in enumerate(color):
    print(color)

numbers = range(10)

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)