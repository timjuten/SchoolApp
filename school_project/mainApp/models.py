from django.db import models

STATUS_CHOICES = (
    ("TUTOR", "Куратор"),
    ("TEACHER", "Вчитель"),
    ("STUDENT", "Учень"),
    ("HEADTEACHER", "Директор")
)


class SchoolUser(models.Model):
    class Meta:
        verbose_name = "Users"
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    birth_date = models.DateField(max_length=60)
    password = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)


