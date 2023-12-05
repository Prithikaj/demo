from django.shortcuts import render, get_object_or_404, redirect
from .models import Contactt
from .forms import ContacttForm

def contactt_list(request):
    contacts = Contactt.objects.all()
    return render(request, 'contacts/contactt_list.html', {'contacts': contacts})

def contactt_detail(request, pk):
    contact = get_object_or_404(Contactt, pk=pk)
    return render(request, 'contacts/contactt_detail.html', {'contact': contact})

def contactt_create(request):
    if request.method == 'POST':
        form = ContacttForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contactt_list')
    else:
        form = ContacttForm()
    return render(request, 'contacts/contactt_form.html', {'form': form})

def contactt_edit(request, pk):
    contact = get_object_or_404(Contactt, pk=pk)
    if request.method == 'POST':
        form = ContacttForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('contactt_list')
    else:
        form = ContacttForm(instance=contact)
    return render(request, 'contacts/contactt_form.html', {'form': form})

def contactt_delete(request, pk):
    contact = get_object_or_404(Contactt, pk=pk)
    contact.delete()
    return redirect('contactt_list')
