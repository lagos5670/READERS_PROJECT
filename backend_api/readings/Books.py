from django.db import models
import datetime


# Create your models here.

class books(models.Model):
    title = models.CharField(max_length = 30)
    author = models.CharField(max_length = 30)
    genre = models.CharField (max_length = 30)
    published_year = models.IntegerField()
    isbn = models.IntegerField()
    publisher = models.CharField(max_length = 30) 
    pages = models.IntegerField()
    lenguage = models.CharField(max_length = 30)
    description = models.TextField()
    over_image_url = models.ImageField(upload_to='books/', null=True, blank=True)
    created_at = models.DateTimeField(default = datetime.datetime.now())
    updated_at = models.DateTimeField(default = datetime.datetime.now())
    deleted_at = models.DateTimeField(null = True, blank = True)
    
    def __str__(self):
        return f"{self.title}-{self.author}-{self.genre}-{self.published_year}
                -{self.isbn}-{self.publisher}-{self.pages}-{self.lenguage}
                -{self.description}-{self.over_image_url}"
