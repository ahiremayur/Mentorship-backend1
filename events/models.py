from django.db import models


class Event(models.Model):
    conducting_body = models.CharField(max_length=50)
    title = models.CharField(max_length=200, primary_key=True)
    description = models.CharField(max_length=1000)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    venue = models.CharField(max_length=500)
    image = models.ImageField(default=FileNotFoundError)
    favs_option = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' by '+self.conducting_body
