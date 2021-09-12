from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Kudo(models.Model):
    from_user=models.ForeignKey(User, on_delete=True, related_name='from_user_id')
    to_user=models.ForeignKey(User, on_delete=True, related_name='to_user_id')
    content=models.TextField()
    kudo_date=models.DateField(auto_now_add=True)
    kudo_count=models.IntegerField()