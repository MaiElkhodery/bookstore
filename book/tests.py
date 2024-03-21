from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Book
from datetime import date
from django.urls import reverse
from rest_framework import status

class BookModelTestCase(TestCase):
    
    @classmethod
    def setUp(self):
        self.book = Book.objects.create(
            title = "clean code",
            description = "A Handbook of Agile Software Craftsmanship",
            author = "Robert C.Martin",
            language="English",
            pages_no = 462,
            publication_date = date(2016,1,1)
        )
        
    def test_fields_values(self):
        book = Book.objects.get(id=1)
        self.assertEqual(
            book.title,"clean code"
        )
        self.assertEqual(
            book.description,"A Handbook of Agile Software Craftsmanship"
        )
        self.assertEqual(
            book.author,"Robert C.Martin"
        )
        self.assertEqual(
            book.language,"English"
        )
        self.assertEqual(
            book.pages_no,462
        )
        self.assertEqual(
            book.publication_date,date(2016,1,1)
        )
        
    def test_fields_values_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field("title").max_length
        self.assertLessEqual(
            len(book.title),max_length
        )
        
        max_length = book._meta.get_field("author").max_length
        self.assertLessEqual(
            len(book.author),max_length
        )
        
        max_length = book._meta.get_field("language").max_length
        self.assertLessEqual(
            len(book.language),max_length
        )
               
class BookCreateApiTest(TestCase):
    
    @classmethod
    def setUp(self):
        self.book = Book.objects.create(
            title = "clean code",
            description = "A Handbook of Agile Software Craftsmanship",
            author = "Robert C.Martin",
            language="English",
            pages_no = 462,
            publication_date = date(2016,1,1)
        )
    
    def test_create_book(self):
        data = {
            "title": "OPERATING SYSTEM CONCEPTS",
            "description": "Operating systems are an essential part of any computer system.",
            "author": "ABRAHAM SILBERSCHATZ",
            "language": "English",
            "pages_no": 1810,
            "publication_date": "2018-10-15"
        }
        response = self.client.post(reverse('create_book'),data)
        self.assertEqual(
            response.status_code,status.HTTP_201_CREATED
        )
        self.assertEqual(
            Book.objects.count(),2
        )
               
class BooksGetApiTest(APITestCase):
    @classmethod
    def setUp(self):
        self.book = Book.objects.create(
            title = "clean code",
            description = "A Handbook of Agile Software Craftsmanship",
            author = "Robert C.Martin",
            language="English",
            pages_no = 462,
            publication_date = date(2016,1,1)
        )
        
    def test_get_books(self):
        response = self.client.get(reverse('list_books'))
        self.assertEqual(
            response.status_code,status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.data),1
        )
        self.assertEqual(
            response.data[0]["title"], "clean code"
        )       
        
class BookDeleteApiTest(APITestCase):
    @classmethod
    def setUp(self):
        self.book = Book.objects.create(
            title = "clean code",
            description = "A Handbook of Agile Software Craftsmanship",
            author = "Robert C.Martin",
            language="English",
            pages_no = 462,
            publication_date = date(2016,1,1)
        )
        
    def test_delete_book(self):
        response = self.client.delete(
            reverse('modify_delete_book',kwargs={'pk':self.book.pk})
        )
        self.assertEqual(
            response.status_code,status.HTTP_204_NO_CONTENT
        )
    
class BookUpdateapiTest(APITestCase):
    
    @classmethod
    def setUp(self):
        self.book = Book.objects.create(
            title = "clean code",
            description = "A Handbook of Agile Software Craftsmanship",
            author = "Robert C.Martin",
            language="English",
            pages_no = 462,
            publication_date = date(2016,1,1)
        )
    def test_update_book(self):
        data = {
            'pages_no': 827,
            'publication_date': '2014-11-15'
        }
        response = self.client.patch(
            path=reverse('modify_delete_book',kwargs={'pk':self.book.pk}),
            data=data,
            format = 'json'
        )
        print(response)
        self.assertEqual(
            response.status_code,status.HTTP_200_OK
        )
        updated_book =  Book.objects.get(pk=self.book.pk)
        self.assertEqual(
            updated_book.pages_no, 827
        )
        self.assertEqual(
            updated_book.publication_date, date(2014,11,15)
        )