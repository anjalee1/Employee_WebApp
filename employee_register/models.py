from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)#ON DELETE CASCADE is used in to delete the
                                                                  #rows from the child table automatically, when the rows 
                                                                  # from the parent table are deleted
