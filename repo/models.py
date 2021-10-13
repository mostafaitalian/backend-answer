from django.db import models

# Create your models here.


class Repo(models.Model):
    repo_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    owner = models.CharField(max_length=200)

    def __str__(self):
        return self.repo_name

