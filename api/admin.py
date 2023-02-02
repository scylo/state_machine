from django.contrib import admin
from .models import State, Machine, Transition

admin.site.register(State)
admin.site.register(Machine)
admin.site.register(Transition)
