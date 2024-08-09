from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Book
# ▪ book_list для отображения списка всех книг.
# ▪ book_detail для отображения деталей конкретной книги.
# ▪ book_create для создания новой книги.
# ▪ book_update для редактирования существующей книги.
# ▪ book_delete для удаления книги.



def book_list(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})

def book_create(request):
    if request.method == 'POST':
        book = Book.objects.create(title = request.POST['title'], author = request.POST['author'], published_date = request.POST['published_date'],isbn = request.POST['isbn'], price = request.POST['price'])
        return redirect(reverse('home'))
    return render(request, 'create.html')

def book_update(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.isbn = request.POST['isbn']
        book.price = request.POST['price']
        book.save()
        return redirect(reverse('home'))
    return render(request, 'update.html', {'book':book})

def book_delete(request, id):
    task = Book.objects.get(id=id)
    task.delete()
    return redirect(reverse('home'))