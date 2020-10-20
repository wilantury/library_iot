from django.contrib import admin

#Models
from books.models.models import (Books, Operations, Authors, Users_library, Alertemail)
from books.models.logger import Logger

#Serializers
from books.serializers.books import BooksModelSerializer

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    """Books admin"""
    list_display = ('id_tag_rfid', 'title', 'isbn', "language",
                    "id_author", "publisher", "status", "alarm")

@admin.register(Users_library)
class UsersLibraryAdmin(admin.ModelAdmin):
    """Users library admin"""

@admin.register(Operations)
class OperationsAdmin(admin.ModelAdmin):
    """Borrow operations admin"""
    filter_horizontal = ('books',)
    list_display = ('id_user', 'date_borrowed', 'date_returned',)

    def save_model(self, request, obj, form, change):
        data = request.POST.getlist('books')
        if len(data) > 0:
            if change:
                for book_id in data:
                    book_to_lend = Books.objects.get(pk=int(book_id))
                    book_to_lend.status = False
                    book_to_lend.save()
            else:
                for book_id in data:
                    book_to_lend = Books.objects.get(pk=int(book_id))
                    book_to_lend.status = True
                    book_to_lend.save()
        else: return
        super().save_model(request, obj, form, change)

@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    """Authors admin"""

@admin.register(Alertemail)
class AlertEmail(admin.ModelAdmin):
    """Alert emails"""

@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    """Logger admin"""
    list_display = ('id_tag_rfid', 'date_created', 'book_title', 'book_id_author', 'book_isbn')
