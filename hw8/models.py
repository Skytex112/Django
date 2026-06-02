import uuid
from django.db import models
from django.core.validators import MinValueValidator

class Client(models.Model):
    """Покупатели"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255, verbose_name="ФИО Покупателя")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)

    class Meta:
        db_table = 'hw_clients_v2'
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.full_name

class Seller(models.Model):
    """Продавцы"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=255, verbose_name="ФИО Продавца")
    badge_number = models.CharField(max_length=50, unique=True, verbose_name="Номер удостоверения")

    class Meta:
        db_table = 'hw_sellers_v2'
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'

    def __str__(self):
        return self.full_name

class Product(models.Model):
    """Товары"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, verbose_name="Название товара")
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01)], verbose_name="Цена")
    stock = models.PositiveIntegerField(default=0, verbose_name="Остаток на складе")

    class Meta:
        db_table = 'hw_products_v2'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

class Sale(models.Model):
    """Продажи"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="sales")
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="sales")
    buyer = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="purchases")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Итоговая сумма")
    sale_date = models.DateField(verbose_name="Дата продажи")

    class Meta:
        db_table = 'hw_sales_v2'
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def save(self, *args, **kwargs):
        if not self.total_price and self.product:
            self.total_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Продажа {self.product.name} ({self.sale_date})"
