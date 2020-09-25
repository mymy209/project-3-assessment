from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    widgets = Widget.objects.all()
    total = 0
    for widget in widgets:
        total += widget.quantity
    widget_form = WidgetForm()
    return render(request, 'index.html', {
        'widget_form': widget_form, 
        'widgets': widgets,
        'total': total
    })

def delete_widget(request, widget_id):
    Widget.objects.filter(id=widget_id).delete()
    return redirect('index')

def add_widget(request):
  form = WidgetForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('index')