# Pydantic provides ways to specify any combination of these checks:
# • Required versus optional
# • Default value if unspecified but required
# • The data type or types expected
# • Value range restrictions
# • Other function-based checks if needed

# model.py - Pydantic model

from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


thing = Creature(
    name="yetti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominale Snowman"
)

print("Name is", thing.name)
