from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils import timezone


class Command(BaseCommand):
    help = 'Удаляет все данные и добавляет тестовые категории и продукты'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.WARNING("Все категории и продукты удалены."))

        electronics = Category.objects.create(name="Электроника", description="Гаджеты и устройства")
        books = Category.objects.create(name="Книги", description="Разные книги")
        clothes = Category.objects.create(name="Одежда", description="Одежда для всех")

        Product.objects.create(
            name="Смартфон",
            description="Современный смартфон",
            category=electronics,
            price=29990.0,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        Product.objects.create(
            name="Ноутбук",
            description="Мощный ноутбук для работы и игр",
            category=electronics,
            price=79990.0,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        Product.objects.create(
            name="Футболка",
            description="Хлопковая футболка",
            category=clothes,
            price=990.0,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )
        Product.objects.create(
            name="Книга по Django",
            description="Учебник по Django для начинающих",
            category=books,
            price=1490.0,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

        self.stdout.write(self.style.SUCCESS("Тестовые категории и продукты успешно добавлены."))
