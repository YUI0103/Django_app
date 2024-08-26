from django.urls import path
from Django import views

app_name='Django'
urlpatterns = [
    # http://127.0.0.1:8000/
    path('', views.Django, name='Django'),
    path('edit/<int:id>', views.edit, name='edit'), 
    path('delete/<int:id>', views.delete, name='delete'),
]