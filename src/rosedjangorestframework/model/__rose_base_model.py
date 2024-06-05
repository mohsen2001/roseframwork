from django.db import models
from django.utils.timezone import now as date_time_now
import uuid


class RoseModel(models.Model):
    user_created = models.BigIntegerField(
        null=False,
        blank=False,
    )
    datetime_created = models.DateTimeField(
        null=False,
        blank=False,
    )
    datetime_updated = models.DateTimeField(
        null=True,
        blank=True,
    )
    ip_created = models.GenericIPAddressField(
        null=False,
        blank=False,
    )
    ip_updated = models.GenericIPAddressField(
        null=True,
        blank=True,
    )
    user_updated = models.BigIntegerField(
        null=False,
        blank=False,

    )

    record_uuid = models.UUIDField(
        null=False,
        blank=False,
        unique=True,
        default=uuid.uuid4(),
        editable=False
    )

    def create(self, *args, **kwargs):
        datetime_created = date_time_now()
        return super(RoseModel, self).create(
            datetime_created=datetime_created, *args, **kwargs)

    def update(self, *args, **kwargs):
        datetime_updated = date_time_now()
        return super(RoseModel, self).update(
            datetime_updated=datetime_updated, *args, **kwargs)

    class Meta:
        abstract = True
