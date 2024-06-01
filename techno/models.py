from django.db import models


class TechnoDom(models.Model):
    CATEGORY_TECHNO = (
        ("смартфоны", "смартфоны"),
        ("фототехника", "фототехника"),
        ("бытовая техника", "бытовая техника"),
        ("Другое", "Другое"),
    )

    title = models.CharField( max_length=50, verbose_name="Название", null=True)
    image = models.ImageField(upload_to="images/", verbose_name="Загрузите фото", blank=True, null=True)
    description = models.TextField(verbose_name="Краткое описание и гарантии ",null=True)
    music = models.FileField(upload_to="audio/", verbose_name="Проверка  звук товара", blank=True, null=True)
    video = models.URLField(verbose_name='Укажите видео ссылку про товара',null=True)
    category_techno = models.CharField( max_length=50, choices=CATEGORY_TECHNO, verbose_name="Выберите категорию", null=True,)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.created_at}"

    class Meta:
        verbose_name = "TechnoDom"
        verbose_name_plural = "Электро товары"


class VideoContent(models.Model):
    title = models.CharField(max_length=100)
    url_video = models.URLField()

    def __str__(self):
        return self.title