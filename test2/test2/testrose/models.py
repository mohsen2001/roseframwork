from django.db import models

from roseframwork import model


# Create your models here.







class TestMyModel(model.RoseModel):
    __test__ = False  # Indicates this model is for testing
    field1 = models.CharField(max_length=20)
    field2 = models.CharField(max_length=20)
    user_created = models.IntegerField()
    ip_created = models.CharField(max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    record_uuid = models.UUIDField(unique=True)
    ip_updated = models.CharField(max_length=15, null=True, blank=True)
    user_updated = models.IntegerField(null=True, blank=True)
    date_updated = models.DateTimeField(auto_now=True)


