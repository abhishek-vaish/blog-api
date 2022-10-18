from tortoise import fields


class TimestampMixin:
    created = fields.DatetimeField(auto_now=True)
    updated = fields.DatetimeField(auto_now_add=True)
