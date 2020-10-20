from books.models.models import Books
from django.db import models

class Logger(models.Model):
    id_tag_rfid = models.CharField(max_length=100, blank=True, default='', unique=False)
    date_created = models.DateTimeField(auto_now_add=True)
    book_title = models.CharField(max_length=100, blank=True, null=True, default="No book")
    book_id_author = models.CharField(max_length=200, blank=True, default='', null=True)
    book_isbn = models.CharField(max_length=100, blank=True, null=True, default="No book")

    def __str__(self):
        return 'ID: {}  Date: {}'.format(self.id_tag_rfid, self.date_created)
