from django.contrib import admin
from django.urls import path
from app.views import book_create,book_detail,book_list,book_update, book_delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', book_list, name='home'),
    path('book_detail/<int:id>', book_detail, name='book_detail'),
    path('book_create/<int:id>', book_create, name='create'),
    path('book_update/<int:id>', book_update, name='update'),
    path('book_delete/<int:id>', book_delete, name='delete')
]
