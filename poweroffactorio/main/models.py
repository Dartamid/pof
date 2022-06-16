from django.db import models


class TeamMember(models.Model):
    name = models.CharField(
        'Имя члена команды',
        max_length=255,
    )
    image = models.ImageField(
        'Фотография члена команды',
        upload_to='team/'
    )
    role = models.CharField(
        'Роль',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Члены команды'

    def __str__(self):
        return self.name
