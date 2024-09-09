from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="Product/image",
        verbose_name="Изображение(превью)",
        **NULLABLE,
        help_text="Загрузите изображение продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        **NULLABLE,
        related_name="products"
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену за покупку"
    )
    created_at = models.DateField(
        verbose_name="Дата создания(записи в БД)",
        **NULLABLE,
        help_text="Укажите дату создания"
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения(записи в БД)",
        **NULLABLE,
        help_text="Укажите дату изменения"
    )
    manufactured_at = models.DateField(
        verbose_name="Дата производства продукта",
        **NULLABLE,
        help_text="Укажите дату производства продукта"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category"]

    def __str__(self):
        return self.name
