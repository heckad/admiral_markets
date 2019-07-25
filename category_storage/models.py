from django.db import models
from mptt.fields import TreeForeignKey


# Create your models here.
from mptt.models import MPTTModel


class Category(MPTTModel):
    name = models.CharField(max_length=100)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
