from django.contrib import admin
from .models import Specialization, Disease, Patient, Doctor, Diagnosis

admin.site.register(Specialization)
admin.site.register(Disease)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Diagnosis)