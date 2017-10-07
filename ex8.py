formatter = "{0} {1} {2} {3}"

print(formatter.format(1, 2, 3, 4))
#prints 1 2 3 4
print(formatter.format("one", "two", "three", "four"))
#prints one two three four
print(formatter.format(True, False, False, True))
#prints true false false true
print(formatter.format(formatter, formatter, formatter, formatter))
#prints {0} {1} {2} {3} times 4.
print(formatter.format(
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))
# prints I had this thing. That you could type up right. But it didn't sing. So I said goodnight.