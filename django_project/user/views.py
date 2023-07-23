from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from user.forms import UserForm
from user.models import User


def user_list(request):
    return render(request, 'user/partials/list.html', {
        'users': User.objects.all(),
    })


def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'userListChanged'})
    else:
        form = UserForm()

    return render(request, 'partials/form.html', {
        'title': 'Add User',
        'form': form,
    })


def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'userListChanged'})
    else:
        form = UserForm(instance=user)

    return render(request, 'partials/form.html', {
        'title': 'Edit User',
        'form': form,
        'user': user,
    })


def user_remove(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == 'POST':
        user.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'userListChanged'})

    return render(request, 'user/partials/confirm_delete.html', {
        'title': 'Delete User',
        'user': user,
    })


class UserListView(ListView):
    model = User
    extra_context = {
        'title': 'User List',
        'active': 'users'
    }
    context_object_name = 'users'
    template_name = 'user/user_list.html'


class UserCreateView(CreateView):
    model = User
    extra_context = {
        'title': 'Create User',
        'active': 'users'
    }
    # fields = ('username', 'email', 'password', 'first_name', 'last_name', 'age', 'is_superuser', 'is_staff', 'is_active')
    form_class = UserForm
    template_name = 'user/user_create.html'
    success_url = reverse_lazy('users:user-index')


class UserDetailView(DetailView):
    model = User
    extra_context = {
        'title': 'User Detail',
        'active': 'users'
    }
    context_object_name = 'user'
    template_name = 'user/user_detail.html'


class UserUpdateView(UpdateView):
    model = User
    extra_context = {
        'title': 'Update User',
        'active': 'users'
    }
    # fields = ('username', 'email', 'password', 'age', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active')
    form_class = UserForm
    template_name = 'user/user_update.html'
    success_url = reverse_lazy('users:user-index')


class UserDeleteView(DeleteView):
    model = User
    extra_context = {
        'title': 'Delete User',
        'active': 'users'
    }
    context_object_name = 'user'
    template_name = 'user/user_delete.html'
    success_url = reverse_lazy('users:user-index')
