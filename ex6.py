x ="There are %d types of people."%10
binary = "binary"
do_not = "don't"
y = "Those who know {0} and those who {1}.".format(binary, do_not)

print(x)
print(y)

print("I said: {0}.".format(x))
print("I also said: '{0}'.".format(y))

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)