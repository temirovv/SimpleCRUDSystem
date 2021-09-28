from .models import NoteModel
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView, UpdateView, DeleteView)


class NoteListView(ListView):
    model = NoteModel
    template_name = 'home.html'


class NoteUpdateView(UpdateView):
	model = NoteModel
	template_name = 'update.html'
	fields = ['title', 'text']
	success_url = reverse_lazy('home')


class NoteDeleteView(DeleteView):
	model = NoteModel
	template_name = 'delete.html'
	success_url = reverse_lazy('home')


class NoteCreateView(CreateView):
	model = NoteModel
	template_name = 'create.html'
	fields = ['author', 'title', 'text']
	success_url = reverse_lazy('home')
