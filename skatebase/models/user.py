from tortoise.models import Model
from tortoise import fields

class User(Model):
    name = fields.CharField(max_length=255)
