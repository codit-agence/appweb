from django.contrib import admin
from .models import Contact, ContactInscription


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','ville']


class ContactInscriptionAdmin(admin.ModelAdmin):
    list_display = ['name','ville']


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactInscription, ContactInscriptionAdmin)