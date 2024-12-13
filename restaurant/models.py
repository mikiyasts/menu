from django.db import models
from django.contrib.auth.models import User



#models for restaurant

class Restaurant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="restaurant")
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to="restaurant_logos/")
    primary_color = models.CharField(max_length=7, )
    secondary_color = models.CharField(max_length=7)
    slogan = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Menu Categories
class Category(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="categories")
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="category_icons/")

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"
    
# Menu Items
class MenuItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="menu_items")
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="menu_items/", blank=True, null=True)
    is_special = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.category.restaurant.name})"