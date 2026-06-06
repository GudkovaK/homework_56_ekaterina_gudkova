from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import GuestEntry
from webapp.forms import GuestEntryForm, SearchForm

def entry_list(request):
    form = GuestEntryForm()
    search_form = SearchForm(request.GET)
    entries = GuestEntry.objects.filter(status='active').order_by('-created_at')
    if search_form.is_valid() and search_form.cleaned_data['name']:
        entries = entries.filter(name=search_form.cleaned_data['name'])
    return render(request, 'webapp/entry_list.html', {'entries': entries, 'form': form, 'search_form': search_form})

def entry_add(request):
    if request.method == 'POST':
        form = GuestEntryForm(request.POST)
        if form.is_valid():
            GuestEntry.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('entry_list')
        entries = GuestEntry.objects.filter(status='active').order_by('-created_at')
        return render(request, 'webapp/entry_list.html', {'entries': entries, 'form': form})
    return redirect('entry_list')

def entry_edit(request, pk):
    entry = get_object_or_404(GuestEntry, pk=pk)
    if request.method == 'POST':
        form = GuestEntryForm(request.POST)
        if form.is_valid():
            entry.name = form.cleaned_data['name']
            entry.email = form.cleaned_data['email']
            entry.text = form.cleaned_data['text']
            entry.save()
            return redirect('entry_list')
    else:
        form = GuestEntryForm(initial={
            'name': entry.name,
            'email': entry.email,
            'text': entry.text
        })
    return render(request, 'webapp/entry_edit.html', {'form': form, 'entry': entry})

def entry_delete(request, pk):
    entry = get_object_or_404(GuestEntry, pk=pk)
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        if email == entry.email:
            entry.delete()
            return redirect('entry_list')
        else:
            error = 'Email введён неверно!'
    return render(request, 'webapp/entry_delete.html', {'entry': entry, 'error': error})