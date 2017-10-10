def add_two_numbers():
    number1 = 1
    number2 = 2
    answer = number1 + number2
    print("{0} plus {1} is {2}".format(number1, number2, answer))
add_two_numbers()

def add_two_numbers_from_args(number3, number4):
    answer1 = number3 + number4
    print("{0} plus {1} is {2}".format(number3,number4,answer1))
add_two_numbers_from_args(10,5) #needs two arguments