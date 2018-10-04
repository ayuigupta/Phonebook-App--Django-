from django.shortcuts import render
from .models import Contact, UserProfile, UserForm, UserProfileForm
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import ContactForm
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import ContactForm
# Create your views here.
@login_required
def contact_list(request):
	contacts = Contact.objects.filter(created_date__lte = timezone.now()).order_by('firstname')
	return render(request, 'phonebook/contact_list.html', {'contacts': contacts})

@login_required
def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.created_date = timezone.now()
            contact.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'phonebook/add_contact.html', {'form': form})

@login_required
def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'phonebook/contact_detail.html', {'contact': contact})

@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.created_date = timezone.now()
            contact.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'phonebook/contact_edit.html', {'form': form})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return redirect('contact_list') 

@login_required    
def logout_view(request):
    logout(request)
    # Redirect back to index page.
    return redirect('login')