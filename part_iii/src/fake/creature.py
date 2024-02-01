from model.creature import Creature

# TODO: replace data
# fake data, will be replaced later
_creatures = [
    Creature(name="Yeti",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan",
             aka="Abominable Snowman"),
    Creature(name="Bigfoot",
             country="US",
             area="*",
             description="Yeti's Cousin Eddie",
             aka="Sasquatch"),
]


def get_all() -> list[Creature]:
    """Return all creatures"""
    return _creatures


def get_one(name: str) -> Creature | None:
    """Return one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


# These are non-functional since we dont have actual data right now
def create(creature: Creature) -> Creature:
    """Add a creature"""
    return creature


def modify(creature: Creature) -> Creature:
    """Partially modify an creature"""
    return creature


def replace(creature: Creature) -> Creature:
    """Completely replace an creature"""
    return creature


def delete(name: str) -> bool:
    """Deleta an creature; return None if it existed"""
    return None
