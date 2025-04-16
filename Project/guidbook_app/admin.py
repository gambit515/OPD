from django.contrib import admin
from .models import Category, Tag, Record, Block, StudentRequest
from django import forms
# Инлайн-форма для модели Block

from django import forms
from .models import Block


class BlockForm(forms.ModelForm):
    class Meta:
        model = Block
        fields = '__all__'

#   def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#
#         # Скрываем все специфичные поля по умолчанию
#         self.fields['description'].widget.attrs.update({
#             'data-field-type': 'text'
#         }){"type":"chat","id":"f7a6279b-6a87-4301-949c-8897c47e6b20","item":{"id":"f7a6279b-6a87-4301-949c-8897c47e6b20"}}
#         self.fields['image'].widget.attrs.update({
#             'data-field-type': 'image'
#         })
#         self.fields['video_url'].widget.attrs.update({
#             'data-field-type': 'video'
#         })
#         # Показываем поля в зависимости от типа блока
#         if self.instance and self.instance.type:
#             field_name = {
#                 'text': 'description',
#                 'image': 'image',
#                 'video': 'video_url',
#             }.get(self.instance.type)
#
#             if field_name:
#                 self.fields[field_name].widget.attrs['style'] = ''
#
#         # Добавляем JavaScript для обработки изменения типа блока
#         self.fields['type'].widget.attrs.update({
#             'onchange': (
#                 "var block = this.closest('.dynamic-blocks');"
#                 "if (block) {"
#                 "   block.querySelectorAll('[data-field-type]').forEach(function(field) {"
#                 "       field.closest('.form-row').style.display = 'none';"
#                 "   });"
#                 "   var selectedType = this.value;"
#                 "   if (selectedType) {"
#                 "       var targetField = block.querySelector('[data-field-type=\"' + selectedType + '\"]');"
#                 "       if (targetField) {"
#                 "           targetField.closest('.form-row').style.display = '';"
#                 "       }"
#                 "   }"
#                 "}"
#             )
#         })
#
#     class Media:
#         js = ('admin/js/jquery.init.js', 'admin/js/block_form_init.js')  # Подключаем собственный JS файл


class BlockInline(admin.StackedInline):
    model = Block
    form = BlockForm  # Используем кастомную форму
    extra = 1  # Количество дополнительных пустых форм для новых блоков
    fields = ['order','type', 'description', 'image', 'video_url', 'file']   # Все поля
    readonly_fields = ()  # Если нужно сделать какие-то поля только для чтения





# Админка для модели Record
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category', 'tags')
    search_fields = ('title', 'content')
    inlines = [BlockInline]  # Добавляем инлайн-форму для блоков

# Админка для других моделей
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'item_count')
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе name

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение slug на основе name

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    form = BlockForm
    list_display = ('record', 'type', 'order')
    list_filter = ('type',)
    readonly_fields = ()  # Если нужно сделать какие-то поля только для чтения

    # Добавляем JavaScript для динамического переключения полей
    class Media:
        js = ('admin/js/block_form_init.js',)

@admin.register(StudentRequest)
class StudentRequestAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'faculty', 'course', 'subject', 'work_type', 'status', 'created_at')
    list_filter = ('status', 'faculty', 'course')
    search_fields = ('student_name', 'subject', 'work_type')
    list_editable = ('status',)