from django.db import models

# Create your models here.

class Join(models.Model):
    #code
    email = models.EmailField()
    created_time = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated_time = models.DateTimeField(auto_now_add = False, auto_now = True)
    
    def __unicode__(self):
        return "Join"
