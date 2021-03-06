# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Book_Author(models.Model):
    book = models.ForeignKey(Book,related_name='books')
    author = models.ForeignKey(Author,related_name='authors')
