from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(unique=True, verbose_name="URL категории")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    item_count = models.PositiveIntegerField(default=0, verbose_name="Количество записей")
    color_class = models.CharField(max_length=50, default="color-teal", verbose_name="CSS-класс цвета")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# Модель Тегов
class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название тега")
    slug = models.SlugField(unique=True, verbose_name="URL тега")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


# Модель Записи
class Record(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок записи")
    content = models.TextField(verbose_name="Содержимое записи (HTML)")
    short_content = models.TextField(verbose_name="Краткое содержание записи (HTML)")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория"
    )
    tags = models.ManyToManyField(Tag, blank=True, verbose_name="Теги")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Block(models.Model):
    BLOCK_TYPES = (
        ('text', 'Текстовый блок'),
        ('image', 'Фото блок'),
        ('video', 'Видео блок'),
        ('file', 'Файловый блок'),
    )

    record = models.ForeignKey(
        'Record', related_name='blocks', on_delete=models.CASCADE, verbose_name="Запись"
    )
    type = models.CharField(
        max_length=50, choices=BLOCK_TYPES, verbose_name="Тип блока"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    description = models.TextField(blank=True, null=True, verbose_name="Описание/Содержимое")
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Изображение")
    video_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")
    file = models.FileField(upload_to='files/', blank=True, null=True, verbose_name="Файл")  # Новое поле

    class Meta:
        ordering = ['order']
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"

    def __str__(self):
        return f"{self.get_type_display()} для записи {self.record.title}"


class StudentRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'На рассмотрении'),
        ('approved', 'Одобрено'),
        ('rejected', 'Отклонено'),
    )

    faculty = models.CharField(max_length=200, verbose_name="Факультет")
    course = models.CharField(max_length=100, verbose_name="Курс")
    subject = models.CharField(max_length=200, verbose_name="Предмет")
    work_type = models.CharField(max_length=100, verbose_name="Тип работы")
    student_name = models.CharField(max_length=200, verbose_name="ФИО студента")
    contact_info = models.CharField(max_length=200, verbose_name="Контактные данные")
    file = models.FileField(upload_to='student_requests/', verbose_name="Прикрепленный файл")  # Теперь обязательное поле
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Статус"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Запрос от {self.student_name} ({self.subject})"

    class Meta:
        verbose_name = "Запрос студента"
        verbose_name_plural = "Запросы студентов"