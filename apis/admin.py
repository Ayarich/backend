from django.contrib import admin
from .models import News




class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','updated_at')
    search_fields = ('title','description')


# Register your models here.
admin.site.register(News,NewsModelAdmin)

