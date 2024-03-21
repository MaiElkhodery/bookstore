from django.db import models

# class Category(models.Model):
#     CATEGORY = (
#      ('fiction','Fiction'),
#      ('thriller','Thriller'),
#      ('mystery','Mystery'),
#      ('history','History'),
#      ('travel','Travel'),
#      ( 'religion','Religion'),
#      ('cooking','Cooking'),
#      ('art','Art'),
#      ('health','Health'),
#      ('business','Business')
#     )
#     name = models.CharField(max_length = 100,choices=CATEGORY)
    
    
class Book(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(max_length = 150,default="")
    author = models.CharField(max_length = 50,default="")
    language = models.CharField(max_length = 50)
    pages_no = models.IntegerField()
    publication_date = models.DateField()
    


    
    
    