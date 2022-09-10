from django.urls import path

from .views import projects, add, project, edit, edit_entry, add_entry, delete_entry, delete_untracked_entry, modal

app_name = 'project'

urlpatterns = [
    path('', projects, name='projects'),
    path('<int:project_id>/', project, name='project'),
    path('add/', add, name='add'),
    path('modal', modal, name='modal'),
    path('<int:project_id>/edit/', edit, name='edit'),
    path('<int:project_id>/<int:entry_id>/edit/', edit_entry, name='edit_entry'),
    path('<int:project_id>/<int:entry_id>/delete/', delete_entry, name='delete_entry'),
    path('add_entry/<int:entry_id>/', add_entry, name='add_entry'),
    path('delete_untracked_entry/<int:entry_id>/', delete_untracked_entry, name='delete_untracked_entry'),


]