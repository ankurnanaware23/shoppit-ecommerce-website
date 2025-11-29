from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    CATEGORY = (
        ('Electronics', 'ELECTRONICS'),
        ('Clothing', 'CLOTHING'),
        ('Groceries', 'GROCERIES'),
    )   
    # First value is stored in DB (Electronics) and Second value is displayed in UI (ELECTRONICS)

    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    slug = models.SlugField(unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY, blank=True, null=True)

    def __str__(self):
        return self.name
    

    # Override save method to auto-generate slug from name
    # this function will create unique slugs for products
    # it checks if the slug already exists in the DB if yes then it appends a number to make it unique
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            unique_slug = self.slug
            num = 1
            while Product.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{self.slug}-{num}'
                num += 1   
            self.slug = unique_slug

        super().save(*args, **kwargs)