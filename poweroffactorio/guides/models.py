from django.db import models


class Paragraph(models.Model):
    guide_name = models.CharField(
        verbose_name='Гайд и номер параграфа',
        max_length=255
    )
    title = models.CharField(
        'Название параграфа',
        max_length=255,
        blank=True, null=True,
    )
    text = models.TextField(
        'Текст параграфа',
        blank=True, null=True,
    )
    image = models.ImageField(
        'Фото для параграфа',
        upload_to='guides/',
        blank=True, null=True,
    )

    class Meta:
        verbose_name = 'Параграф'
        verbose_name_plural = 'Параграфы'

    def __str__(self):
        return self.guide_name


class Guide(models.Model):
    name = models.CharField(
        'Название гайда',
        max_length=255,
    )
    image = models.ImageField(
        'Титульное фото гайда',
        upload_to='guides/'
    )
    description = models.CharField(
        'Описание гайда',
        max_length=1000,
        blank=True, null=True,
    )
    paragraphs = models.ManyToManyField(
        Paragraph,
        verbose_name='Параграфы',
        blank=True,
    )

    class Meta:
        verbose_name = 'Гайд'
        verbose_name_plural = 'Гайды'

    def __str__(self):
        return self.name