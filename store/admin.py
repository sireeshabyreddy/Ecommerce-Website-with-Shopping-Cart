from django.contrib import admin

# Register your models here.
from .models  import Category,Customer,Product,Order,Profile
from django.contrib.auth.models import User
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


#mix profile info and user info
class ProfileInline(admin.StackedInline):
    model=Profile
#extend user model
class UserAdmin(admin.ModelAdmin):
    model=User
    field=["username","first_name","last_name",'emainl']
    inlines=[ProfileInline]
#unregister the old way
admin.site.unregister(User)

#re-Register the new Way
admin.site.register(User,UserAdmin)

