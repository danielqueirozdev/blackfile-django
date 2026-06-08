from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def home(request):
    notes_list = Note.objects.all()

    return render(request, 'notes/pages/home.html', {
        'notes_list': notes_list
    })

def note(request, id):
    note = get_object_or_404(Note, pk=id)

    return render(request, 'notes/pages/home.html', {
        'note': note
    })

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('notes:home')

    else:
        form = NoteForm()

    return render(request, 'notes/pages/create.html', {
        'form': form
    })

def delete(request, id):
    note = get_object_or_404(Note, pk=id)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:home')
    
    return render(request, 'notes/pages/create.html', {
        'note': note
    })

def edit(request, id):
    ...