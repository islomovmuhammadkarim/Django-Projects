from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
# Create your views here.


def home(request):
    books = Book.objects.filter(available=True).order_by('title')  # 'title' bo‘yicha o‘sish tartibida
    template = loader.get_template('home.html')
    context = {'books': books}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    
    return render(request, 'book_form.html', {'form': form, 'title': "Yangi Kitob Qo‘shish"})

@login_required
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    return render(request, "book_edit.html", {
        "form": form,
        "book": book,
        "title": "Kitobni Tahrirlash"
    })


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect('home')  # O‘chirilgandan so‘ng home sahifaga yo‘naltirish

    return render(request, 'book_confirm_delete.html', {'book': book})
