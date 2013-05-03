from django.views.generic import TemplateView, ListView, DetailView
from .models import *

class IndexView(ListView):
    queryset = Pattern.objects.live().order_by('order')

class PatternCategoryView(ListView):
    def get_queryset(self):
        return Pattern.objects.filter(category__slug=self.kwargs['category'],
          category__visible=True).order_by('order')


class PatternDetailView(DetailView):
    model = Pattern
