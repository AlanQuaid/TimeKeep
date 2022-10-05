from django.urls import path
from .views import teams, add, team, edit, activate_team, invite, plans, promote, demote, kick

app_name = 'team'

urlpatterns = [
    path('', teams, name='teams'),
    path('add/', add, name='add'),
    path('<int:team_id>/', team, name='team'),
    path('edit/', edit, name='edit'),
    path('invite/', invite, name='invite'),
    path('plans/', plans, name='plans'),
    path('activate_team/<int:team_id>/', activate_team, name='activate_team'),
    path('promote/<int:user_id>/', promote, name='promote'),
    path('demote/<int:user_id>/', demote, name='demote'),
    path('kick/<int:user_id>/', kick, name='kick')
]