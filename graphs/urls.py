from django.urls import path

from .views import GraphListView

urlpatterns = [
    path('', GraphListView.as_view())
]
