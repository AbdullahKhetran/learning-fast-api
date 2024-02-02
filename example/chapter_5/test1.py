from model import Creature

dragon = Creature(
    name="dragon",
    # this should generate an error when you run test `python test1.py`
    description=["incorrect", "string", "list"],
    country="*",
    area="*",
    aka="firedrake"
)
