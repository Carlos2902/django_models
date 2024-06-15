from django.db import models

#Defining a table: primaryKey is assigned by default
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

#Create
user_1 = User(id=1, "John", "Jones")
user_1.save()

#Read
User.objects.get(id=1)

#Update
user = User.objects.get(id=1)
user.last_name = "Smith"
user.save()

#Delete
User.objects.filter(id=1).delete()