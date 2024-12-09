from django.contrib import admin

from application.models import Room, Booking, UserProfile, Contact
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Contact)

# combine profile info and user

class ProfileInline(admin.StackedInline):
    model = UserProfile

# extend user

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

# unregister old user
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

