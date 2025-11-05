from django.db import models

class Student(models.Model):
    admission_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    roll_number = models.IntegerField()
    student_class = models.IntegerField()
    section = models.CharField(max_length=5)
    physics = models.IntegerField()
    chemistry = models.IntegerField()
    maths = models.IntegerField()
    computer = models.IntegerField()
    english = models.IntegerField()
    total = models.IntegerField()
    average = models.FloatField()
    percentage = models.FloatField()
    grade = models.CharField(max_length=2)
    result = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
