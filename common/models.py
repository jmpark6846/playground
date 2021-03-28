import uuid

from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField('생성일자', auto_now_add=True)
    updated_at = models.DateTimeField('수정일자', auto_now=True)
    deleted_at = models.DateTimeField('삭제일자', default=None, null=True)

    class Meta:
        abstract = True

    @property
    def is_deleted(self):
        return self.deleted_at is not None

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()