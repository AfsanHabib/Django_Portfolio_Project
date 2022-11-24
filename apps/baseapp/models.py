from operator import mod
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Timeline(models.Model):
    work_date = models.CharField(max_length=100)
    work_role = models.CharField(max_length=100)
    work_company =models.CharField(max_length=100)
    work_description =models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.work_company


class Home_Bio(models.Model):
    bio_name = models.CharField(max_length=100)
    bio = models.TextField()
    # cv_link=models.CharField(max_length=200)
    featured = models.BooleanField()

    def __str__(self):
        return self.bio_name


class About_Me(models.Model):
    bio_name = models.CharField(max_length=100)
    about_me = models.TextField()
    # cv_link=models.CharField(max_length=200)
    featured = models.BooleanField()

    def __str__(self):
        return self.bio_name


class DownloadCV(models.Model):
    title = models.CharField(max_length=100)
    cv_link=models.CharField(max_length=200)
    featured = models.BooleanField()

    def __str__(self):
        return self.title


 


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    git_link=models.CharField(max_length=200)
    web_link=models.CharField(max_length=200)
    pic = models.ImageField(upload_to="portfolio_image",blank=True)
    date=models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField()
    
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="blog_image",blank=True)
    description=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(max_length=200)
    
    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title


class Link_Address(models.Model):
    facebook=models.CharField(max_length=100)
    github=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    language=models.CharField(max_length=100)

    
    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email =models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name