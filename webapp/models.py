from django.db import models

# Create your models here.

class webuser(models.Model):
    name = models.TextField(max_length=30)
    username = models.TextField(max_length=30)
    mobile = models.TextField(max_length=11)
    email = models.TextField(max_length=30)
    password = models.TextField(max_length=30)

    def __str__(self) -> str:
        return self.name

class post(models.Model):
    name = models.TextField(max_length=30)
    discription = models.TextField()
    postimage = models.ImageField(upload_to="postimage", blank=True, null=True)
    datetime = models.TextField()

    def __str__(self) -> str:
        return self.name