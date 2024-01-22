# incorrect types are not caught by python interpreter

# >>> thing1: str = "yeti"
# >>> thing1 = 47


# but they will be caught by mypy
thing1: str = "yeti"
thing1 = 47

# now run mypy stuff.py in terminal
