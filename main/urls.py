from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('<int:pk>/', views.NotesDetailView.as_view(), name='detail_blog'),
    path('', views.NotesListView.as_view(), name='index_blog'),
]
