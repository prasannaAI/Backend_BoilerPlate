from typing import Optional

import strawberry

import singUp
from singUp.types import SingUpType


@strawberry.input
class SingUpInput:
    userName: str
    emailId: str
    password: str
    conformPassword: str


@strawberry.type
class singUpMutation:
    @strawberry.mutation
    def create_user(self, info, Input: SingUpInput) -> SingUpType:
        from singUp.models import SingUp
        add_user = SingUp.objects.create(
            userName=Input.userName,
            emailId=Input.emailId,
            password=Input.password,
            conformPassword=Input.conformPassword,
        )
        return add_user

