"""Dummy list of people for using/testing the API"""

from schemas import Address
from schemas import Person
from schemas import State

PEOPLE = [
    Person(
        email="costa@person.com",
        name="Costa",
        address=Address(number=123, street="Fake Street", city="Springfield", state=State.NSW),
    ),
    Person(
        email="jake@person.com",
        name="Jake",
        address=Address(number=99, street="Ned Lane", city="Shelbyville", state=State.VIC),
    ),
    Person(
        email="sarah@person.com",
        name="Sarah",
        address=Address(number=1, street="Krusty Avenue", city="Ogdenville", state=State.QLD),
    ),
]
