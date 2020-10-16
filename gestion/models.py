from django.db import models
import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 20)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "product/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name


class Picture(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=256, null=True, blank=True )
    body = models.TextField()
    publication = models.BooleanField(default=True)
    create_at = models.DateField(auto_now=True, null=True, blank=True)
    update_at = models.DateField(auto_now_add=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Service(models.Model):
    name=models.CharField(max_length=100)
    detail=models.TextField()
    picto=models.CharField(max_length=250)


class Action(models.Model):
    title=models.CharField(max_length=100)
    detail=models.TextField()




