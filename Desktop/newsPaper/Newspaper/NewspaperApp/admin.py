from django.contrib import admin
from api.models import User, Author, Comment, Article


admin.site.register(User)
admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Article)
