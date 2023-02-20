from django.db import models


# Create your models here.
class ContactModel(models.Model):
    """Класс модели обратной связи"""
    class Meta:
        verbose_name = 'Создать контакт'
        verbose_name_plural = "Создать контакты"
        ordering = ['-create_at']

    name = models.CharField(max_length=64, verbose_name="Имя")
    email = models.EmailField(verbose_name="Email")
    # website = models.URLField(default='https://www.google.com', verbose_name="Сайт")
    website = models.URLField(blank=True, null=True, verbose_name="Сайт")
    message = models.TextField(max_length=5000, verbose_name="Сообщение")
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.email}"

