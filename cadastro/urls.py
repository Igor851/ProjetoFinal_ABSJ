from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path('aluno/<int:id>', views.aluno, name='aluno'),
    path('form/', views.form, name='form'),
    path('aluno/Remove/<int:id>/', views.remove, name= 'remove'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)