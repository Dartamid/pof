from django.db import models
from django.db.models.deletion import DO_NOTHING


class ItemType(models.Model):
    name = models.CharField(
        'Название типа объекта',
        max_length=100
    )

    name_plural = models.CharField(
        'Название типа объекта в множественном числе',
        max_length=100
    )
    class Meta:
        verbose_name = 'Тип объекта'
        verbose_name_plural = 'Типы объектов'

    def __str__(self):
        return self.name


class RequiredTechnology(models.Model):
    name = models.CharField(
        'Название необходимой технологии',
        max_length=50
    )

    class Meta:
        verbose_name = 'Необходимая технология'
        verbose_name_plural = 'Необходимые технологии'

    def __str__(self):
        return self.name


class Effect(models.Model):
    name = models.CharField(
        'Название эффекта',
        max_length=255
    )
    value = models.CharField(
        'Значение эффекта',
        max_length=255,
    )
    time = models.CharField(
        'Время эффекта',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Эффект'
        verbose_name_plural = 'Эффекты'
        ordering = ['name', 'value']

    def __str__(self):
        return self.name + self.value



class Item(models.Model):
    name = models.CharField(
        'Название предмета',
        max_length=50,
    )
    image = models.ImageField(
        'Изображение предмета',
        upload_to='items/',
        blank=True, null=True,
    )
    storage_size = models.IntegerField(
        'Размер хранилища',
        blank=True, null=True,
    )
    size = models.CharField(
        'Размер предмета',
        blank=True, null=True,
        max_length=100,
    )
    power_consumption = models.IntegerField(
        'Потребление энергии',
        blank=True, null=True,
    )
    min_power_cons = models.IntegerField(
        'Минимальное потребление энергии',
        blank=True, null=True,
    )
    bonus_inventory_size = models.IntegerField(
        'Бонус размера инвернторя',
        blank=True, null=True,
    )
    calorific_value = models.IntegerField(
        'Теплотворность',
        blank=True, null=True,
    )
    Fuel = models.BooleanField(
        'Топливо',
    )
    item_type = models.ForeignKey(
        ItemType,
        on_delete=DO_NOTHING,
        related_name='items',
        verbose_name = 'Тип предмета'
    )
    health = models.IntegerField(
        'Здоровье',
        blank=True, null=True,
    )
    hand_craft = models.BooleanField(
        'Ручной крафт',
    )
    crafting_time = models.IntegerField(
        'Время создания предмета',
        blank=True, null=True,
    )
    stack_size = models.IntegerField(
        'Размер пачки',
        blank=True, null=True,
    )
    description = models.TextField(
        'Описание',
        blank=True, null=True,
    )
    effects = models.ManyToManyField(
        Effect,
        verbose_name='Эффекты',
        blank=True,
    )

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name',]

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    item = models.ForeignKey(
        'Item',
        on_delete=models.DO_NOTHING,
        verbose_name='Ингредиент',
        related_name='requiredFor',
    )
    value = models.CharField(
        'Количество',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        ordering = ['item', 'value']

    def __str__(self):
        return self.item.name + ' ' + self.value


class Linked(models.Model):
    owner = models.OneToOneField(
        Item,
        on_delete=models.DO_NOTHING,
        related_name='linked',
        verbose_name='Предмет владелец',
    )
    getters = models.ManyToManyField(
        Item,
        related_name='extraction',
        verbose_name = 'Добытчики',
        blank=True,
    )
    add_equipment = models.ManyToManyField(
        Item,
        related_name='setups',
        verbose_name = 'Дополнительное оборудование',
        blank=True,
    )
    craft = models.ManyToManyField(
        Item,
        related_name='createdIN',
        verbose_name = 'Сборщики',
        blank=True,
    )

    class Meta:
        verbose_name = 'Связанный предмет'
        verbose_name_plural = 'Связанные предметы'

    def __str__(self):
        return self.owner.name


class Recipe(models.Model):
    owner = models.ForeignKey(
        Item,
        on_delete=models.DO_NOTHING,
        related_name='recipes',
        verbose_name='Создаваемый предмет',
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        blank=True,
        related_name='needfor'
    )
    ingredients_result = models.IntegerField(
        'Количество'
    )
    number = models.IntegerField(
        'Номер крафта'
    )
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.owner.name