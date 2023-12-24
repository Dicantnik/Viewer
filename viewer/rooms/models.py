from django.db import models
from django.contrib.auth.models import User
from .func import generate_random_code
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length = 40)
    code = models.CharField(max_length = 20, default = generate_random_code())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.URLField(max_length = 150)
    videocode = models.CharField(max_length = 20, default ='ERROR', editable = True)


    def save(self, *args, **kwargs):
        while Room.objects.filter(code = self.code):
            self.code = generate_random_code()  
        super(Room, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

