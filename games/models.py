from django.db import models


class Credential(models.Model):
    name = 'Credential'
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Feedback(models.Model):
    name = 'Feedback'
    try:
        username = models.CharField(max_length=100)
    except:
        username = False
    try:
        feedback = models.CharField(max_length=1000)
    except:
        feedback = False
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.username


