from django.db import models


# Create your models here.
class create(models.Model):
    user = models.CharField(max_length=200)
    shop = models.TextField()
    img = models.ImageField(upload_to='pictures')


class prod(models.Model):
    CATEGORY = (
        ('DELIVERY NOT AVAILABLE', 'DELIVERY NOT AVAILABLE'), ('DELIVERY AVAILABLE', 'DELIVERY AVAILABLE')
    )
    products = models.TextField()
    pricing = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=200, choices=CATEGORY)
    img1 = models.ImageField(upload_to='pictures', default="C:Users\91939\Pictures")
    offer = models.BooleanField(default=False)


class orders(models.Model):
    STATUS = (
        ('PENDING', 'PENDING'),
        ('OUT FOR DELIVERY', 'OUT FOR DELIVERY'),
        ('CONFIRMED', 'CONFIRMED')
    )
    customer = models.ForeignKey(create, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(prod, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
