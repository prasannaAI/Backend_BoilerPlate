import strawberry
from strawberry import auto

from singUp.models import models


@strawberry.django.type(models.SingUp)
class SingUpType:
    id: auto
    userName: str
    emailId: str
    password: str
    conformPassword: str


__all__ = {
    "SingUpType"
}
