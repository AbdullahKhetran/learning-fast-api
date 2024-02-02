from typing import Any, Union
# typing module provides some useful types like Any, Union

# syntax for vairbale types
name: str

# can also initialize directly
name2: str = "john"

# examples
physics_magic_number: float = 1.0/137.03599913
hp_lovecraft_noun: str = "ichor"
exploding_sheep: tuple = "sis", "boom", "bah!"


responses: dict = {"Macro": "Polo", "answer": 42}

# syntax for dict subtype
# name: dict[keytype, valtype] = {key1: val1, key2: val2}
responses2: dict[str, Any] = {"Macro": "Polo", "answer": 42}
# this helped with type narrowing

# more narrowing with types from typing module
responses3: dict[str, str | int] = {"Macro": "Polo", "answer": 42}


# function return type uses arrow instead of colon
# function(args) -> type

def greet() -> str:
    return "hello"
