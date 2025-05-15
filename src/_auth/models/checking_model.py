from django.db import models

from .user_model import User


class CheckPhone(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name="check_phone"
    )
    code = models.IntegerField()

    def __str__(self):
        return f"{self.user} - {self.code}"

    class Meta:
        db_table = "check_phone"
        verbose_name = "Check Phone"
        verbose_name_plural = "Check Phones"
