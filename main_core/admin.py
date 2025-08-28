from django.contrib import admin
from .models import NewsCategory, NewsArticle, Comment, FlickrPhoto
# Register your models here.
admin.site.register(NewsCategory)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_breaking', 'is_featured', 'is_trending', 'created_at')
    list_filter = ('is_breaking', 'is_featured', 'is_trending', 'category')

admin.site.register(NewsArticle, ArticleAdmin)


admin.site.register(Comment)

class FlickrPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title',)

admin.site.register(FlickrPhoto, FlickrPhotoAdmin)
