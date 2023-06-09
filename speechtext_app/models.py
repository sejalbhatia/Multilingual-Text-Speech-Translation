from django.db import models

# Create your models here.
class Feedback(models.Model):
    fullname = models.CharField(max_length=200)
    email= models.EmailField(max_length=100)
    age=models.IntegerField ()
    phone=models.BigIntegerField()
    message=models.TextField(max_length=1000)
    exp = (
        ('E', 'Excellent'),
        ('G', 'Good'),
        ('N','Neutral'),
        ('B', 'Bad'),

    )
    experiences = models.CharField(max_length=10, choices=exp)

    def __str__(self):
        return self.fullname





