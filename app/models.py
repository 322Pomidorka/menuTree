from django.db import models


class Menu(models.Model):
    title = models.CharField('Название', max_length=80)
    slug = models.SlugField('Слаг', unique=True, db_index=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name="children", on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created', )
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title

