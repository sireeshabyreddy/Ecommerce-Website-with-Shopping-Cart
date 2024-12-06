import requests
from django.core.management.base import BaseCommand
from django.core.files import File
from store.models import Product, Category
from io import BytesIO
from django.core.files.temp import NamedTemporaryFile
import random

class Command(BaseCommand):
    help = 'Fetch books from Open Library API and add them to the database, overriding existing books'

    def handle(self, *args, **kwargs):
        query = 'programming'  # Define your search query
        api_url = f'https://openlibrary.org/search.json?q={query}&limit=10'  # Limit added to avoid huge response

        # Fetch data from Open Library API
        response = requests.get(api_url)

        if response.status_code == 200:
            books_data = response.json()

            for book in books_data.get('docs', []):
                title = book.get('title', 'Unknown Title')
                author = book.get('author_name', ['Unknown'])[0]  # First author in the list
                description = book.get('first_sentence', 'No description available')

                # Check if the book already exists in the Product table
                existing_product = Product.objects.filter(name=title).first()

                if existing_product:
                    product = existing_product
                    created = False
                else:
                    created = True
                    # Define categories for the product dynamically (add categories if needed)
                    category_names = book.get('subject', ['Programming Books'])  # Example: Using 'subject' from Open Library
                    categories = []

                    for category_name in category_names:
                        category, _ = Category.objects.get_or_create(name=category_name)
                        categories.append(category)

                    # Create the product
                    product = Product.objects.create(
                        name=title,
                        price=random.randint(300, 1000),
                        description=description,
                        is_sale=True,
                        sale_price=random.randint(150, 500),
                    )

                    # Set categories for the product
                    product.categories.set(categories)
                    
                # Save the product details
                product.save()

                # Handle cover image if available
                cover_id = book.get('cover_i')
                if cover_id:
                    image_url = f'http://covers.openlibrary.org/b/id/{cover_id}-L.jpg'
                    try:
                        img_response = requests.get(image_url)
                        if img_response.status_code == 200:
                            image_temp_file = NamedTemporaryFile(delete=True)
                            image_temp_file.write(img_response.content)
                            image_temp_file.flush()

                            product.image.save(f'{title}_cover.jpg', File(image_temp_file), save=True)
                            self.stdout.write(self.style.SUCCESS(f'Image for product "{product.name}" saved successfully.'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Failed to download image for "{product.name}": {str(e)}'))
                
                # Output result of product creation or update
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Product "{product.name}" created successfully.'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Product "{product.name}" updated successfully.'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to fetch data from Open Library. Status code: {response.status_code}'))
