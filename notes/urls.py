from django.urls import path
from .views import NoteListView, NoteUpdateView, NoteDeleteView, NoteCreateView


urlpatterns = [
    path('', NoteListView.as_view(), name='home'),
    path('update/<int:pk>/', NoteUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', NoteDeleteView.as_view(), name='delete'),
    path('create/', NoteCreateView.as_view(), name='create'),
]
