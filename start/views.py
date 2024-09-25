from django.shortcuts import render

from django.views.generic import ListView
from start.models import Start


class StartListView(ListView):
    model = Start
