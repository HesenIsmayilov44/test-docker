from statistics import mode
from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


class Catagories(models.Model):
    article = models.ForeignKey(Article, related_name='categories', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='description')

    def __str__(self) -> str:
        return self.name


    