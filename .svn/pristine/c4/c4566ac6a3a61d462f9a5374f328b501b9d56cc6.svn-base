from django.contrib import admin
from models import *
# Register your models here.

class MetaInfoAdmin(admin.ModelAdmin):
    list_display = ('web_keywords','web_description')

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','publish_time','desc','content')

admin.site.register(MetaInfo,MetaInfoAdmin)
admin.site.register(Article,ArticleAdmin)