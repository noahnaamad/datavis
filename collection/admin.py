from django.contrib import admin

# Register your models here.

#import the model
from collection.models import Post

#set up automated slug creation
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}


#register it
admin.site.register(Post, PostAdmin)
