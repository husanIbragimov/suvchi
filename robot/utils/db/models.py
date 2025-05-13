from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=150, null=True)
    phone_number = fields.CharField(max_length=64, null=True)
    full_name = fields.CharField(max_length=255, null=True)
    first_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    lang = fields.CharField(max_length=2, default="uz", choices=[("en", "English"), ("ru", "Russian"), ("uz", "Uzbek")])
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users"
