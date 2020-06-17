from django.views.generic.list import ListView

from .models import Graph


class GraphListView(ListView):
    model = Graph
