from django.db import models

LANG = (
    ("en", "English"),
    ("ru", "Russian"),
    ("uz", "Uzbek"),
)

class User(models.Model):
    # id is telegram_id
    username = models.CharField(max_length=150, null=False, blank=False)
    phone_number = models.CharField(max_length=64, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    lang = models.CharField(max_length=2, default="uz", choices=LANG)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.full_name} - {self.phone_number}"
