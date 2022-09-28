from django.shortcuts import render, redirect

from .models import Location, Person
from .forms import RegistrationForm

# Create your views here.

def index(request):
    list = Location.objects.all()
    return render(request, 'locations/index.html', {
        'A_value': 1,
        'A': list
    })

def details(request, location_slug):
    try:
        selected_location_list = Location.objects.get(slug=location_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                person_email = registration_form.cleaned_data['email']
                person, _  = Person.objects.get_or_create(email=person_email)
                selected_location_list.persons.add(person)
                return redirect('confirm-registration', location_slug=location_slug)


        return render(request, 'locations/details.html', {
                'location_found': True,
                'location': selected_location_list,
                'form': registration_form
            })
    except Exception as exc:
        print(exc)
        return render(request, 'locations/details.html',{
        'location_found': False 
        })

def confirm_registration(request, location_slug):
    location = Location.objects.get(slug=location_slug)
    return render(request, 'locations/registration-success.html', {
        'organizer_email': location.organizer_email
    })

