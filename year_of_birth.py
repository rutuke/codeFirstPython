def year_of_birth():
    year = input("Please enter your age: ")
    year_int = int(year)
    answer = 2017 - year_int
    return answer

returned_value = year_of_birth()
print(returned_value)
