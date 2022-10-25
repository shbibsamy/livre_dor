""" Defines models """
from django.db import models

class Comment(models.Model):
    """ Defines Comment model """
    comment = models.CharField(max_length=400)
    email = models.EmailField()
    date = models.DateTimeField(auto_now=True)

    def str(self):
        """ Defines entry name """
        return self.email