from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Books(models.Model):
    CONDTITON = [
        ("new","New"),
        ("good","Good"),
        ("average","Averge"),
        ("poor","Poor")
    ]
    RATING = [
        ("1"),
        ("2"),
        ("3"),
        ("4"),
        ("5"),
    ]
    STATUS = [
        ("available"),
        ("waiting for responce"),
        ("exchnaged")
    ]
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="books")
    condition = models.Choices(choices=CONDTITON)
    city = models.CharField(max_length=100)
    descirption = models.TextField(null=True,blank=True)
    phone_number = models.CharField(max_length=15)
    rating = models.Choices(choices=RATING)
    status = models.Choices(choices=STATUS)
    def __str__(self):
        return self.title