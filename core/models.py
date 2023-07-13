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
    
class AuthorModel(BaseModel):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    about = models.TextField('About')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class BookModel(BaseModel):
    isbn10 = models.IntegerField('Isbn 10', primary_key=True)
    title = models.CharField('Title', max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    publisher = models.ForeignKey(PublisherModel, on_delete=models.CASCADE)
    language = models.CharField('Language', max_length=50)
    pages = models.IntegerField('Pages')
