#from django.db import models

# Create your models here.

from mongoengine import *

class Map(Document):
    url_sht = StringField(primary_key=True)
    url_tgt = URLField(verify_exists=True)
    