from django.shortcuts import render, get_object_or_404

from .models import Job
from .models import Profile
from .models import About
from .models import Summary
from .models import Education
from .models import Experience
from .models import Portfolio
from .models import Contact
# Create your views here.

def home(request):
    jobs = Job.objects
    profiles=Profile.objects.all()
    abouts=About.objects.all()
    summarys=Summary.objects.all()
    educations=Education.objects
    experiences=Experience.objects
    portfolios=Portfolio.objects
    contacts=Contact.objects.all()
    return render(request, 'jobs/home.html',{'jobs':jobs,'profiles':profiles,'abouts':abouts,'summarys':summarys,'educations':educations,'experiences':experiences,'portfolios':portfolios,'contacts':contacts})

