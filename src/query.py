"""GraphQL query"""

import strawberry

from data import PEOPLE
from schemas import Person


@strawberry.type
class Query:
    @strawberry.field
    def people(self) -> list[Person]:
        """Retrieve people list."""
        return PEOPLE
