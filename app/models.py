from django.db import models


class Message(models.Model):
    msg = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True,null=True)


    

    def __str__(self):
        return self.msg
class User2(models.Model):
    msg = models.CharField(max_length=500)
    date_posted = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.msg