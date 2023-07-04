import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from schemas import Person


@strawberry.type
class Query:
    @strawberry.field
    def people(self) -> list[Person]:
        return []


app = FastAPI()

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
