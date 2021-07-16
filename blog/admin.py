from django.contrib import admin

from django.contrib.auth.models import Group, User
from .models import Post, Book, Telawa

from django.utils.translation import gettext_lazy as _





class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'status', 'content', 'slug', 'img')
    list_display = ('title','status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'content', 'slug', 'img')
    list_display = ('title','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class TelawaAdmin(admin.ModelAdmin):
    fields = ('title', 'status', 'youtube_url', 'slug', 'img')
    list_display = ('title','status','created_on')
    list_filter = ("status",)
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)}


admin.site.site_header = _('my admin')
admin.site.register(Post, PostAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Telawa, TelawaAdmin)


admin.site.unregister(Group)
admin.site.unregister(User)




