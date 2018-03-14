from django.contrib import admin

# Register your models here.
from .models import User, Buys

class BuysInstanceInline(admin.TabularInline):
    model = Buys

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'display_buys', 'display_totalamount')
    inlines = [BuysInstanceInline]

admin.site.register(User, UserAdmin)

class BuysAdmin(admin.ModelAdmin):
    list_filter = ('amount', 'user')

admin.site.register(Buys, BuysAdmin)