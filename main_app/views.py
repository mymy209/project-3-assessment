from django.shortcuts import render
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'index.html', {
        'widget_form': widget_form, 
        'widgets': widgets,
    })
