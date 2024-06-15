from django.db import models
#creating tables and establish a relationship between them

#one to one: example of One principal for One College
class college(models.Model):
    College_ID = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    website = models.URLField()

#the pk for the principal will be assigned by default since is not specify 
class principal(models.Model):
    College_ID = models.OneToOneField(
        college,
        on_delete=models.CASCADE
    )
    email = models.CharField(max_length=50)
#on_delete will dictate the behavior on what to do when the foreign key is being deleted from a table
#CASCADE: deletes the object containing the ForeignKey
#PROTECT: Prevent deletion of the referenced object.
#RESTRICT: Prevent deletion of the referenced object by raising RestrictedErro



#one to many: one teacher for many subjects
class Subject(models.Model):
    subject_code = models.IntegerField(primary_key=True)
    subject_name = models.CharField(max_length=50)
    credits = models.IntegerField()


class Teacher(models.Model):
    teacher_ID = models.IntegerField(primary_key=True)
    Subject_code = models.ForeignKey(
        Subject,
        on_delete = models.CASCADE
    )
    email = models.EmailField(max_length=50)



#many to many: many drivers for many cars
class Car(models.Model):
    car_ID = models.IntegerField(primary_key=True)
    car_model = models.CharField(max_length=50)
    driver = models.ManyToManyField(Driver)

class Driver(models.Model):
    driver_ID = models.IntegerField(primary_key=True)
    diver_name = models.CharField(max_length=50)