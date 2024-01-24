from django.shortcuts import render
from .forms import ContactForm
from django.contrib.auth.decorators import login_required


@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        user = request.user
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = user
            contact.save()
            return render(request, 'contact/done.html', {'contact': contact})
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})
