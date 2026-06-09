from .models import Note
from .forms import NoteForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='accounts:login')
def home(request):
    notes_list = Note.objects.all()

    return render(request, 'notes/pages/home.html', {
        'notes_list': notes_list
    })

@login_required(login_url='accounts:login')
def note(request, id):
    note = get_object_or_404(Note, pk=id)
    note_title = note.title

    return render(request, 'notes/pages/note.html', {
        'note': note,
        'note_title': note_title,
    })

@login_required(login_url='accounts:login')
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

@login_required(login_url='accounts:login')
def delete(request, id):
    note = get_object_or_404(Note, pk=id)

    if request.method == 'POST':
        note.delete()
        return redirect('notes:home')
    
    return render(request, 'notes/pages/delete.html', {
        'note': note
    })

@login_required(login_url='accounts:login')
def edit(request, id):
    note = get_object_or_404(Note, pk=id)

    if request.method == 'POST':
        form = NoteForm(
            request.POST,
            instance=note
        )

        if form.is_valid():
            form.save()
            return redirect('notes:home')
        
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/pages/edit.html', {
        'form': form,
    })