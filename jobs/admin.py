from django.contrib import admin

# Register your models here.
from .models import Job
from .models import Profile 
from .models import About
from .models import Summary
from .models import Education
from .models import Experience
from .models import Portfolio
from .models import Contact

admin.site.register(Job)
admin.site.register(Profile)
admin.site.register(About)
admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Portfolio)
admin.site.register(Contact)