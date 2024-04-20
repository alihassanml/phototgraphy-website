


from django.db import models

# Create your models here.

class image(models.Model):
    title = models.CharField(max_length=300, unique=True)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media')
    summary = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return self.title
    def __str__(self) :
        return self.name
    def __str__(self) :
        return self.photo
    def __str__(self) :
        return self.summary
        