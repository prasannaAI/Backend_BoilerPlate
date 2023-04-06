from typing import List

import strawberry

from .models import SingUp

from .types import SingUpType

from strawberry.tools import merge_types

from singUp.mutation import singUpMutation


@strawberry.type
class SignUpQuery:
    @strawberry.field
    def singUps(self, info) -> List[SingUpType]:
        singUPs = SingUp.objects.all()
        return singUPs


Queries = merge_types(
    "Queries",
    (
        SignUpQuery,
    )
)

Mutations = merge_types(
    "Mutations",
    (
        singUpMutation,
    )
)

schema = strawberry.Schema(query=Queries, mutation=Mutations)

__all__ = {
    "schema",
    "Queries",
    "Mutations"
}
