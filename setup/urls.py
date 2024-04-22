from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('update/<user_id>', views.update, name='update'),
    path('delete/<user_id>', views.delete, name='delete'),
    path('admin/', admin.site.urls),
]
