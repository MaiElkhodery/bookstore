from django.urls import path
from .views import *

urlpatterns = [
    path('books', BooksListApi.as_view(), name='list_books'),
    path('book/<int:pk>', BookApi.as_view(), name='modify_delete_book'),
    path('book', BookCreateApi.as_view(), name='create_book')
]