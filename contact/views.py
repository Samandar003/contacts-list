from django.shortcuts import redirect, render
from .models import Contact

def index(request):
  contacts = Contact.objects.all()
  context = {'contacts':contacts}
  return render(request, 'index.html', context)

def addContact(request):
  if request.method == 'POST':
    data = request.POST
    new_contact = Contact(
    full_name = data['fullname'],
    relationship = data['relationship'],
    phone_number = data['phone-number'],
    email = data['email'],
    address = data['address'] )
    new_contact.save()
    return redirect('/')
  context = {}
  return render(request, 'new.html')

def contactProfile(request, pk):
  contact = Contact.objects.get(id=pk)
  context = {'contact':contact}  
  return render(request, 'contact-profile.html', context)

# def editContact(request):
#   if request.
#   context = {}
#   return render(request, 'edit.html', context)
