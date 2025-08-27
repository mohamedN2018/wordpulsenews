from django.contrib import admin
from . models import InformationContact, ContactMessage, SocialMediaIcon 
# Register your models here.

admin.site.register(InformationContact)
admin.site.register(ContactMessage)
admin.site.register(SocialMediaIcon)
