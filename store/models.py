from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
# We need category model, customer model, product model, and order model

#create customer profile
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(auto_now=True)  # Removed 'User' from here
    phone = models.CharField(max_length=10, blank=False)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    pincode = models.CharField(max_length=6, blank=False)
    country = models.CharField(max_length=200, blank=True)
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username

# Create user profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

# Automate profile creation
post_save.connect(create_profile, sender=User)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)  # Changed to EmailField and made it unique
    password = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default='', blank=True)  # Removed 'null=True'
    image = models.ImageField(upload_to='uploads/product/', blank=True, null=True, default='uploads/product/Mother_and_Daughter.jpeg')
    
    # Sale Stuff
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=8)

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    phone = models.CharField(max_length=10, default='', blank=True)
    date = models.DateField(auto_now_add=True)  # Automatically set to the current date
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Order of {self.product.name} by {self.customer.first_name} {self.customer.last_name}"
