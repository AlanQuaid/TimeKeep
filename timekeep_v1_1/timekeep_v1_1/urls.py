"""timekeep_v1_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from timetracking.timer import start_timer, stop_timer, discard_timer, get_tasks
from timetracking.views import (
    home,
    shop,
    acc,
    logout_request,
    accept_invitation,


)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', include('summary.urls')),
    path('shop', shop, name='shop'),
    path('', include('subscriptions.urls')),
    path('logout/', logout_request, name='logout'),
    path('account/', acc, name='account'),
    path('accept_invitation/', accept_invitation, name='accept_invitation'),
    path('teams/', include('team.urls')),
    path('projects/', include('project.urls')),
    path("timetracking/timer/start_timer/", start_timer, name='start_timer'),
    path("timetracking/timer/stop_timer/", stop_timer, name='stop_timer'),
    path("timetracking/timer/discard_timer/", discard_timer, name='discard_timer'),
    path('timetracking/timer/get_tasks/', get_tasks, name='get_tasks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
