from tortoise import fields
from tortoise.models import Model

from .._mixins import TimestampMixin


class UserTortoise(Model, TimestampMixin):
    """Base User Model"""

    username = fields.CharField(max_length=50, unique=True, null=False)
    password = fields.CharField(max_length=100, null=False)
    email = fields.CharField(max_length=50)
    first_name = fields.CharField(max_length=50, null=False)
    last_name = fields.CharField(max_length=50)

    class Meta:
        table = "user"


class TokenTortoise(Model, TimestampMixin):
    """User Token Authentication Model"""

    token = fields.CharField(max_length=200, null=False)
    user = fields.ForeignKeyField(
        "models.UserTortoise", on_delete=fields.CASCADE, related_name="user"
    )

    class Meta:
        table = "token"
