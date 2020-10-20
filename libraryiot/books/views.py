"""Views to manage books endpoint"""
#Django Rest Framework
from asyncio import exceptions
from os import error
from django.db.utils import Error
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#Models
from books.models.models import Books, Operations, Alertemail
from books.models.logger import Logger

#Serializers
from books.serializers.books import BooksModelSerializer
from books.serializers.operations import OperationsModelSerializer
from books.serializers.emails import EmailModelSerializer

#utils
from books.email.email import Sendemail
#async IO
import asyncio


def send_alert_email(option, result):
    query_emails = Alertemail.objects.all()
    result_emails = EmailModelSerializer(query_emails, many=True).data
    emails = [i['email'] for i in result_emails]
    if option:
        Sendemail.send_alert_email(book_title=result[0]['title'], book_isbn=result[0]['isbn'],
                                       book_author=result[0]['id_author'], emails=emails)
    else:
        Sendemail.send_alert_email(book_title="No info", book_isbn="No info",
                                               book_author="No info", emails=emails)

# Hello Books
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        try:
            query_book = Books.objects.filter(id_tag_rfid=request.data['id_tag_rfid'])
            result = BooksModelSerializer(query_book, many=True).data

            if len(result) > 0:
                new_event = Logger.objects.create(id_tag_rfid=result[0]['id_tag_rfid'], 
                                                  book_title=result[0]['title'],
                                                  book_id_author=result[0]['id_author'],
                                                  book_isbn=result[0]['isbn'])                                                
                new_event.save()
                if result[0]['status'] == False:
                    send_alert_email(True, result=result)

                return Response({"status":result[0]['status']}, status=status.HTTP_201_CREATED)
            else:
                new_event = Logger.objects.create(id_tag_rfid=request.data['id_tag_rfid'])
                new_event.save()
                send_alert_email(False, result=result)
                return Response({"status":False}, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response({"status":"error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'GET':
        #query = Books.objects.all()
        #result = BooksModelSerializer(query, many=True).data
        query = Operations.objects.all()
        result = OperationsModelSerializer(query, many=True).data

        return Response(result)
    return Response({"error":"Method no allowed"}, status=status.HTTP_200_OK)
