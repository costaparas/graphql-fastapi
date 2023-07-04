"""API boilerplate"""

import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

from query import Query

app = FastAPI()

schema = strawberry.Schema(query=Query)
graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
