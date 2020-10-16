from django.contrib import admin
from .models import Picture, Article, Category, Service, Action


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','category']


admin.site.register(Picture)
admin.site.register(Action)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Service)

