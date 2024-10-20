from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from tasks.models import ToDoList, ToDoItem
from users.models import User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ToDoList)
admin.site.register(ToDoItem)
