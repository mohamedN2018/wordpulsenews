from django.db import models

# Create your models here.

class InformationContact(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'information_contact'
        managed = True
        verbose_name = 'Information Contact'
        verbose_name_plural = 'Information Contacts'

    def __str__(self):
        return f"Contact from {self.name} - {self.created_at}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contact_message'
        managed = True
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"Message from {self.name} - {self.created_at}"
    


class SocialMediaIcon(models.Model):
    icon_name = models.CharField(max_length=255, blank=True, null=True)
    link = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("social media icons")
        verbose_name_plural = ("social media icons")

    def __str__(self):
        return self.icon_name
    
    