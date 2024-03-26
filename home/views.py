from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import Http404

def home(request):
    return render(request, 'home/welcome.html', {})

@login_required
def authorized(request):
    return render(request, 'home/authorized.hmtl', {})

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesnt exist")
    return render(request, 'notes/notes_detail.html', {'note': note})