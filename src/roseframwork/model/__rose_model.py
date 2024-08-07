from django.db import models
from django.utils.timezone import now as date_time_now
import uuid


class RoseModel(models.Model):
    """Rose Model is an abstract base Model that define in project

            This is particularly helpful when you want to create a model.
            .

            ```python

            class StudentModel(RoseModel):
                name: models.CharField()

            student = StudentModel(name="Alex")
            print(student.datetime_created)
            #> show datetime that this record was created
            ```

            Attributes:
                user_created: The user that insert this record.
                datetime_created: datetime that this record was created
                datetime_updated: datetime that this record was updated
                ip_created: user ip that this record was created
                ip_updated: user ip that updated this record
                user_updated: user that update this record
                record_uuid: unique id for this record  in project


            """
    user_created = models.BigIntegerField(
        null=True,
        blank=True,
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
    user_updated = models.CharField(
        null=True,
        blank=True,

    )

    record_uuid = models.UUIDField(
        null=False,
        blank=False,
        unique=True,
        default=uuid.uuid4(),
        editable=False
    )

    def create(self, *args, **kwargs):
        """ automatically assigned datetime_created  when creating
        """
        datetime_created = date_time_now()
        return super(RoseModel, self).create(
            datetime_created=datetime_created, *args, **kwargs)

    def update(self, *args, **kwargs):
        """ automatically assigned datetime_updated when updating
                """
        datetime_updated = date_time_now()
        return super(RoseModel, self).update(
            datetime_updated=datetime_updated, *args, **kwargs)

    class Meta:
        abstract = True
