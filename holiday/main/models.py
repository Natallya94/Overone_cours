from django.db import models

# Create your models here.
class Check(models.Model):

    fname = models.CharField('Имя', max_length=20)
    lname = models.CharField('Фамилия', max_length=20)
    data = models.EmailField('дата')

    class Meta:
        verbose_name = 'Подпищик'
        verbose_name_plural = 'Подпищики'

    def __str__(self):
        return self.data

class Slider(models.Model):


    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/img')

class ManagersList(models.Model):


    name = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/img')
    description = models.CharField(max_length=50)
    twitter_url = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=100)

class Tours(models.Model):


    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/img')
    description = models.TextField()
    twitter_url = models.CharField(max_length=100)
    facebook_url = models.CharField(max_length=100)
