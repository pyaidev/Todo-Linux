from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'status')
    list_filter = ('status', 'author__username')
    search_fields = ('title', 'author')


admin.site.register(Todo, TodoAdmin)