# Python Generators

# Dialouges from Simpson episode
def doh():
    return ["Homer: D'oh!", "Marge: A deer!", "Lisa: A female deer!"]


for line in doh():
    print(line)


# What if we large list, like all the diaoulges of episode
# List take memory, so yield comes handy in this case
def doh2():
    yield "Homer: D'oh!"
    yield "Marge: A deer!"
    yield "Lisa: A female deer!"


for line in doh2():
    print(line)

# doh2() returns a generator function, and we are iterating over that instead of list
