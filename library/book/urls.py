from django.urls import path, include
from . import views
from .views import BookAllView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Book', views.BookView)


urlpatterns = [
    # path('', include(router.urls)),
    # path('', views.all_books, name='books'),
    path('', BookAllView.as_view()),
    path('<int:id>/', views.book_form, name='book'),
    path('<int:id>/view', views.book_by_id, name='book_by_id'),
    path('<int:id>/delete/', views.book_delete, name='book_delete'),

]