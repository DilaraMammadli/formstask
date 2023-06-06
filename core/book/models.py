from django.db import models


class Book(models.Model):
    name = models.CharField(max_length = 100)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    price = models.FloatField()
    dis_price = models.FloatField()
    

    def __str__(self):
        return self.name