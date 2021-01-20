from django.db import models
from accounts.models import Users

class Notes(models.Model):
    """ Модель хранит заметки сайта """
    title = models.CharField('Заголовок', max_length=255, unique=True)
    date = models.DateTimeField('Дата создания заметки', auto_now_add=True)
    text = models.TextField("Текст заметки")
    author = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Автор заметки')

    def __str__(self) -> str:
        return ("{}, за авторством {}".format(self.title, self.author))

    class Meta:
        db_table = 'notes'
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
        ordering = ['-date']
