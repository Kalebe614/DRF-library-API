from django.db import models

class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PublisherModel(BaseModel):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description')

    def __str__(self):
        return self.name
