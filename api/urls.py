from django.urls import path

from api import views

urlpatterns = [
    path('books/', views.BooksAPI.as_view()),
    path('books/<str:id>/', views.BooksAPI.as_view())
]