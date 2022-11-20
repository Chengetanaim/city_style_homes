from django.db import models


class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
        

class Review(models.Model):
    image = models.ImageField(upload_to='uploads/')
    name = models.CharField(max_length=100)
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name