from tortoise.models import Model
from tortoise import fields


class BlogTortoise(Model):
    title = fields.CharField(max_length=100, null=False)
    description = fields.TextField(null=False)
    user = fields.ForeignKeyField("models.UserTortoise", on_delete=fields.CASCADE)
    created = fields.DatetimeField(auto_now=True)
    updated = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "blog"
