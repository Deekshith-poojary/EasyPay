from django.db import models

# Create your models here.
class payments(models.Model):
    payment_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    ammount=models.IntegerField()
