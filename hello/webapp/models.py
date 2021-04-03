from django.db import models

# Create your models here.


class Poll(models.Model):
    question = models.TextField(null=False, blank=False)
    date_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'Polls'
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return f'{self.id}. {self.question}: {self.date_time}'



class Choice(models.Model):
    text = models.TextField(max_length=3000, null=False, blank=False)
    poll = models.ForeignKey(
        'webapp.Poll',
        on_delete=models.CASCADE,
        related_name='lists',
        null=False,
        blank=False
    )

    class Meta:
        db_table = 'Choices'
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return f'{self.id}. {self.text}: {self.poll}'