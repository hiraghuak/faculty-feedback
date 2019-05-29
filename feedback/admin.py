from django.contrib import admin

from .models import Post

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','NAME_OF_THE_LESSON','SUBJECT','timestamp']


admin.site.register(Post,UserProfileAdmin)
