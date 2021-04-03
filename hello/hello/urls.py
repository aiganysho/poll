"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from webapp.views import (
    IndexView,
    PollDetailView,
    PollCreate,
    PollUpdate,
    PollDelete,
    ChoiceView,
    ChoiceDetailView,
    ChoiceCreate,
    ChoiceUpdate,
    ChoiceDelete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='list-poll'),
    path('<int:pk>/', PollDetailView.as_view(), name='view-poll'),
    path('add/', PollCreate.as_view(), name='add-poll'),
    path('<int:pk>/update/', PollUpdate.as_view(), name='update-poll'),
    path('<int:pk>/delete/', PollDelete.as_view(), name='delete-poll'),
    path('choice/', ChoiceView.as_view(), name='list-choice'),
    path('<int:pk>/choice/view/', ChoiceDetailView.as_view(), name='view-choice'),
    path('<int:pk>/choice/add/', ChoiceCreate.as_view(), name='add-choice'),
    path('<int:pk>/choice/update/', ChoiceUpdate.as_view(), name='update-choice'),
    path('<int:pk>/choice/delete/', ChoiceDelete.as_view(), name='delete-choice'),
]
