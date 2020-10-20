from django.db import models

class Users_library(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    id_citizen = models.CharField(max_length=20, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    grade = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.first_name


class Authors(models.Model):
    nationality = models.CharField(max_length=80, blank=True, default='')
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.name, self.nationality)

class Operations(models.Model):
    id_user = models.ForeignKey(Users_library, on_delete=models.DO_NOTHING)
    date_borrowed = models.DateTimeField(auto_now_add=True)
    date_returned = models.DateTimeField(blank=True, null=True, default=None)
    books = models.ManyToManyField('Books', blank=True)

class Alertemail(models.Model):
    email = models.CharField(max_length=50, blank=False)
    name = models.CharField(max_length=80, blank=True, default='')

    def __str__(self) -> str:
        return '{} - {}'.format(self.email, self.name)

class Books(models.Model):
    id_tag_rfid = models.CharField(max_length=100, blank=True, default='', unique=True)
    title = models.CharField(max_length=100, blank=False)
    isbn = models.CharField(max_length=100, blank=False, unique=True)
    language = models.CharField(max_length=50, blank=True, default='')
    id_author = models.ForeignKey(Authors, on_delete=models.DO_NOTHING)
    publisher = models.CharField(max_length=80, blank=True, default='')
    status = models.BooleanField(blank=False, default=False)
    alarm = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return '{} - disponible: {}'.format(self.title, self.status)
