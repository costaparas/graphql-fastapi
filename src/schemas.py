"""API schema"""

from enum import Enum

import strawberry


@strawberry.enum
class State(Enum):
    """Australian states (in alphabetical order!)"""

    ACT = "Australia Capital Territory"
    NSW = "New South Wales"
    NT = "Northern Territory"
    QLD = "Queensland"
    SA = "South Australia"
    TAS = "Tasmania"
    VIC = "Victoria"
    WA = "Western Australia"


@strawberry.type
class Address:
    """Components of a basic address"""

    number: int
    street: str
    city: str
    state: State


@strawberry.type
class Person:
    """Essential details of a person"""

    email: str
    name: str
    address: Address
