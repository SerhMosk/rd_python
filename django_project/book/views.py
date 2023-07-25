from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from book.forms import BookForm
from book.models import Book


def book_list(request):
    return render(request, 'book/partials/list.html', {
        'books': Book.objects.all(),
    })


def book_add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'bookListChanged'})
    else:
        form = BookForm()

    return render(request, 'partials/form.html', {
        'title': 'Add Book',
        'form': form,
    })


def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'bookListChanged'})
    else:
        form = BookForm(instance=book)

    return render(request, 'partials/form.html', {
        'title': 'Edit Book',
        'form': form,
        'book': book,
    })


def book_remove(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'bookListChanged'})

    return render(request, 'book/partials/confirm_delete.html', {
        'title': 'Delete Book',
        'book': book,
    })


class BookListView(ListView):
    model = Book
    extra_context = {
        'title': 'Book List',
        'active': 'books'
    }
    context_object_name = 'books'
    template_name = 'book/book_list.html'


class BookCreateView(CreateView):
    model = Book
    extra_context = {
        'title': 'Create Book',
        'active': 'books'
    }
    # fields = ('title', 'author', 'year', 'price')
    form_class = BookForm
    template_name = 'book/book_create.html'
    success_url = reverse_lazy('books:book-index')


class BookDetailView(DetailView):
    model = Book
    extra_context = {
        'title': 'Book Detail',
        'active': 'books'
    }
    context_object_name = 'book'
    template_name = 'book/book_detail.html'


class BookUpdateView(UpdateView):
    model = Book
    extra_context = {
        'title': 'Update Book',
        'active': 'books'
    }
    # fields = ('title', 'author', 'year', 'price')
    form_class = BookForm
    template_name = 'book/book_update.html'
    success_url = reverse_lazy('books:book-index')


class BookDeleteView(DeleteView):
    model = Book
    extra_context = {
        'title': 'Delete Book',
        'active': 'books'
    }
    context_object_name = 'book'
    template_name = 'book/book_delete.html'
    success_url = reverse_lazy('books:book-index')
