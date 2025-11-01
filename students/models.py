from django.db import models

class Student(models.Model):
    admission_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    roll_number = models.IntegerField()
    class_name = models.IntegerField()
    section = models.CharField(max_length=5)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    mathematics = models.IntegerField()
    computer = models.IntegerField()
    english = models.IntegerField()
    total = models.IntegerField()
    average = models.FloatField()
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.admission_number})"