from django.core.management.base import BaseCommand
from faker import Faker
from lloguer.models import Automobil  # Asegúrate de importar tu modelo

class Command(BaseCommand):
    help = 'Generates 200 fake automobile models and saves them to the database'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(200):
            marca = fake.company()
            model = fake.word()
            matricula = ''.join(fake.random_letters(length=2)).upper() + str(fake.random_number(digits=4)) + ''.join(fake.random_letters(length=2)).upper()
            # Crea la instancia del modelo Automobil y guárdala en la base de datos
            Automobil.objects.create(marca=marca, model=model, matricula=matricula)
        self.stdout.write(self.style.SUCCESS('200 automobiles created successfully'))
