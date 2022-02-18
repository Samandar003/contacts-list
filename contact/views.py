from django.shortcuts import redirect, render
from .models import Contact

def index(request):
  contacts = Contact.objects.all()
  search_input = request.GET.get('search-area')
  if search_input:
    contacts = Contact.objects.filter(full_name__contains=search_input)
  else:
    contacts = Contact.objects.all()
    search_input = ''
  context = {'contacts':contacts, 'search_input':search_input}
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

def editContact(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone-number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {'contact': contact})
 
  