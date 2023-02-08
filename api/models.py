from django.db import models


class Product(models.Model):
    
        REGULAR = 'R'
        GOLD = 'G'
        PLATINUM = 'P'
        DIMOND = 'D'
        ACCOUNT_TYPE_CHOICES = [
        (REGULAR, 'Regular'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
        (DIMOND, 'Diimond'),
    ]
        name = models.CharField(max_length=20,default='')
        price = models.IntegerField()
        account_type = models.CharField(max_length=1,choices=ACCOUNT_TYPE_CHOICES,default=REGULAR,)
        
        def __str__(self):
            return self.name

class Client(models.Model):
    REGULAR = 'R'
    GOLD = 'G'
    PLATINUM = 'P'
    ACCOUNT_TYPE_CHOICES = [
        (REGULAR, 'Regular'),
        (GOLD, 'Gold'),
        (PLATINUM, 'Platinum'),
    ]
    name = models.CharField(max_length=50)
    registered_on = models.DateField()
    account_type = models.CharField(max_length=1,choices=ACCOUNT_TYPE_CHOICES,default=REGULAR,)
    product_id = models.ForeignKey(Product, blank = True, null = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.name
    