from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField('pic')
    desc=models.TextField()

    def __str__(self):
        return self.name
class abouts(models.Model):
    name1 = models.CharField(max_length=250)
    about = models.TextField()
    img=models.ImageField('picture')


    def __str__(self):
        return self.name1
