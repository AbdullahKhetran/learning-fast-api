# plain sql VS SQLAlchemy from chapter 14

from model.explorer import Explorer
from .init import curs
from sqlalchemy import Metadata, Table, Column, Text
from sqlalchemy import connect, insert


# SQLAlchemy Expression Langauge
# example 14-2
conn = connect("sqlite:///cryptid.db")
meta = Metadata()
explorer_table = Table(
    "explorer",
    meta,
    Column("name", Text, primary_key=True),
    Column("country", Text),
    Column("description", Text),
)
insert(explorer_table).values(
    name="Beau Buffette",
    country="US",
    description="..."
)


# Straight SQL
# example 14-1

def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(name=name, country=country, description=description)


def get_one(name: str) -> Explorer:
    qry = "select * from explorer where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    return row_to_model(curs.fetchone())
