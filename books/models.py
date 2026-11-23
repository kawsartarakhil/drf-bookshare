from django.db import models
from accounts.models import Customuser

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Books(models.Model):
    CONDTITON = (
        ("new","New"),
        ("good","Good"),
        ("average","Averge"),
        ("poor","Poor")
    )
    RATING = (
        ("1","one star"),
        ("2","two star"),
        ("3","three star"),
        ("4","four star"),
        ("5","five star"),
    )
    STATUS = (
        ("pending","pending"),
        ("returned","retunrned"),
        ("exchnaged","exchange")
    )
    title = models.CharField(max_length=150)
    owner = models.ForeignKey(Customuser,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="books")
    condition = models.CharField(choices=CONDTITON)
    city = models.CharField(max_length=100)
    descirption = models.TextField(null=True,blank=True)
    phone_number = models.CharField(max_length=15)
    rating = models.CharField(choices=RATING)
    status = models.CharField(choices=STATUS)
    def __str__(self):
        return self.title

class Trade(models.Model):
    user = models.ForeignKey(Customuser,on_delete=models.CASCADE)
    book = models.ForeignKey(Books,on_delete=models.CASCADE)
    traded_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()

    def __str__(self):
        return f"{self.book} {self.traded_at}"