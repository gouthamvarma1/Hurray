from django.db import models

# Create your models here.
from django.contrib.auth.models import User


# Create your models here.
class Kudo(models.Model):
    from_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user_id')
    to_user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user_id')
    content=models.TextField()
    kudo_date=models.DateField(auto_now_add=True)
    kudo_count=models.IntegerField()