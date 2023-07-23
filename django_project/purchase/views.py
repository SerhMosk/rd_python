from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from book.models import Book
from purchase.forms import PurchaseForm
from purchase.models import Purchase
from user.models import User


def purchase_list(request):
    return render(request, 'purchase/partials/list.html', {
        'purchases': Purchase.objects.all(),
    })


def purchase_add(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'purchaseListChanged'})
    else:
        form = PurchaseForm()

    return render(request, 'partials/form.html', {
        'title': 'Add Purchase',
        'form': form,
    })


def purchase_edit(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'purchaseListChanged'})
    else:
        form = PurchaseForm(instance=purchase)

    return render(request, 'partials/form.html', {
        'title': 'Edit Purchase',
        'form': form,
        'purchase': purchase,
    })


def purchase_remove(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)

    if request.method == 'POST':
        purchase.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'purchaseListChanged'})

    return render(request, 'purchase/partials/confirm_delete.html', {
        'title': 'Delete Purchase',
        'purchase': purchase,
    })


class PurchaseListView(ListView):
    model = Purchase
    extra_context = {
        'title': 'Purchase List',
        'active': 'purchases',
        'books':  list(Book.objects.all()),
        'users': list(User.objects.all())
    }
    context_object_name = 'purchases'
    template_name = 'purchase/purchase_list.html'


class PurchaseCreateView(CreateView):
    model = Purchase
    extra_context = {
        'title': 'Create Purchase',
        'active': 'purchases'
    }
    # fields = ('book', 'user')
    form_class = PurchaseForm
    template_name = 'purchase/purchase_create.html'
    success_url = reverse_lazy('purchases:purchase-index')


class PurchaseDetailView(DetailView):
    model = Purchase
    extra_context = {
        'title': 'Purchase Detail',
        'active': 'purchases'
    }
    context_object_name = 'purchase'
    template_name = 'purchase/purchase_detail.html'


class PurchaseUpdateView(UpdateView):
    model = Purchase
    extra_context = {
        'title': 'Update Purchase',
        'active': 'purchases'
    }
    # fields = ('book', 'user')
    form_class = PurchaseForm
    template_name = 'purchase/purchase_update.html'
    success_url = reverse_lazy('purchases:purchase-index')


class PurchaseDeleteView(DeleteView):
    model = Purchase
    extra_context = {
        'title': 'Delete Purchase',
        'active': 'purchases'
    }
    context_object_name = 'purchase'
    template_name = 'purchase/purchase_delete.html'
    success_url = reverse_lazy('purchases:purchase-index')
