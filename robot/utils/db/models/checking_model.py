from tortoise import fields
from tortoise.models import Model


class CheckPhone(Model):
    id = fields.IntField(pk=True)
    user = fields.OneToOneField(
        "models.User", related_name="check_phone",
        on_delete=fields.CASCADE
    )
    code = fields.IntField()

    class Meta:
        table = "check_phone"
