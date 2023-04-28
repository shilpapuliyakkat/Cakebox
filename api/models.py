from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.

class Cakes(models.Model):
    name=models.CharField(max_length=100)
    options=(
        ("circle","circle"),
        ("square","square"),
        ("oval","oval"),
        ("rectange","rectangle")
    )
    shape=models.CharField(max_length=150,choices=options,default="circle")
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images",default=True)
    weight=models.CharField(max_length=150)
    price=models.PositiveBigIntegerField()
    layers_choices=(
        ("one","one"),
        ("two","two"),
        ("three","three")
    )
    layers=models.CharField(max_length=150,choices=layers_choices,default="three")
    
    def __str__(self):
        return self.name

class Carts(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    order=(
        ("in-carts","in-carts"),
        ("order-placed","order-placed"),
        ("cancelled","cancelled")
    )
    Order_status=models.CharField(max_length=150,choices=order,default="order-placed")
    quantity=models.PositiveIntegerField(default=1)


class Orders(models.Model):
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    shipping=(
        ("shipped","shipped"),
        ("order-placed","order-place"),
        ("in-transit","in-transit"),
        ("delivered","delivered"),
        ("cancelled","cancelled"),
        ("return","return")
    )
    shipping_status=models.CharField(max_length=100,choices=shipping,default="shipped")
    curDtae=datetime.date.today()
    expDate=curDtae+datetime.timedelta(days=1)
    expected_deliverydate=models.DateField(default=expDate)
    address=models.CharField(max_length=260,null=True)

class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(Cakes,on_delete=models.CASCADE)
    comment=models.CharField(max_length=240)
    rating=models.FloatField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return self.comment




