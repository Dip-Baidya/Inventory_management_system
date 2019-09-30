from django.db import models


class Device(models.Model):
    type = models.CharField(max_length=100, blank=False)  # name of the column
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default="SOLD")  # Available, sold, Restocking
    issues = models.CharField(max_length=100, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} price : {1}'.format(self.type, self.price)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass
