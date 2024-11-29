import random
from django.core.management.base import BaseCommand
from faker import Faker
from properties.models import Property, PropertyImages, Category
from django.core.files.images import ImageFile
from io import BytesIO
from PIL import Image

class Command(BaseCommand):
    help = 'Generate fake data for Property and PropertiesImages models'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        categories = ["Residential", "Commercial", "Land", "Apartment"]
        for category_name in categories:
            Category.objects.get_or_create(category_name=category_name)
        
        for _ in range(10): 
            category = random.choice(Category.objects.all())
            property = Property.objects.create(
                title=fake.sentence(nb_words=6),
                category=category,
                address=fake.address(),
                old_price=fake.random_number(digits=5),
                new_price=fake.random_number(digits=5),
                description=fake.paragraph(nb_sentences=5),
                yt_link=fake.url(),
                per_aana_price=fake.random_number(digits=3),
                plot_size=fake.random_element(elements=("500 sq ft", "1000 sq ft", "1500 sq ft")),
                total_aana=fake.random_number(digits=3),
                google_map_url=fake.url(),
                status=random.choice(['Rent', 'Buy']),
                is_highlight=random.choice([True, False]),
                is_featured=random.choice([True, False])
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully created property: {property.title}'))

            for _ in range(random.randint(1, 3)): 
                image = self.create_fake_image()
                image_file = ImageFile(image, name=f'{fake.uuid4()}.jpg')
                PropertyImages.objects.create(property=property, image=image_file)
                self.stdout.write(self.style.SUCCESS(f'Created fake image for {property.title}'))

    def create_fake_image(self):
        """
        Create a fake image and return it as a BytesIO object.
        """
        image = Image.new('RGB', (640, 480), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        img_io = BytesIO()
        image.save(img_io, 'JPEG')
        img_io.seek(0)
        return img_io
