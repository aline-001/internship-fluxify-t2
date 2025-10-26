from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)

    def _str_(self):
        return self.title


class Librarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    def _str_(self):
        return self.name


class Borrower(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def _str_(self):
        return self.name


class BorrowerBook(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField()
    return_date = models.DateField()

    def _str_(self):
        return self.borrower.name + " borrowed " + self.book.title
