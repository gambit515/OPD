from django.contrib import admin
from django.urls import path, include  # Импортируем include для подключения маршрутов приложения
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Админка Django
    path('', include('guidbook_app.urls')),  # Подключаем маршруты приложения
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)