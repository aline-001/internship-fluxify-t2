from django.contrib import admin

from .models import*

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Librarian)
admin.site.register(Borrower)
admin.site.register(BorrowerBook)


# Register your models here.
