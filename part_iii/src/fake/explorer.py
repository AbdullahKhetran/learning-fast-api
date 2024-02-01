from model.explorer import Explorer

# TODO: replace data
# fake data, will be replaced later
_explorers = [
    Explorer(name="Calude Hande",
             country="FR",
             description="Scarce during full moons"),
    Explorer(name="Noah Weiser",
             country="DE",
             description="Myopic machete man"),
]


def get_all() -> list[Explorer]:
    """Return all explorers"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    """Return one explorer"""
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


# These are non-functional since we dont have actual data right now
def create(explorer: Explorer) -> Explorer:
    """Add an explorer"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Partially modify an explorer"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Completely replace an explorer"""
    return explorer


def delete(name: str) -> bool:
    """Deleta an explorer; return None if it existed"""
    return None
