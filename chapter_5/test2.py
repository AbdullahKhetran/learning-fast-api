from pydantic import BaseModel, constr


class Creature(BaseModel):
    name: constr(min_length=2)
    # alternate is `Field[..., min_length=2]`
    country: str
    area: str
    description: str
    aka: str


bad_creature = Creature(
    # this will result in validation error
    name="!",
    description="it's a racoon",
    area="your attic",
    country="US",
    aka="rac"
)
