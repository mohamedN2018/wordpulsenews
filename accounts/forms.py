from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Profile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': _('Username'),
            'email': _('Email Address'),
            'password1': _('Password'),
            'password2': _('Confirm Password'),
            'profile_picture': _('Profile Picture'),
        }
        help_texts = {
            'username': _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
            'email': _('Required. Enter a valid email address.'),
        }
        error_messages = {
            'username': {
                'max_length': _("This username is too long."),
                'unique': _("This username is already taken."),
            },
            'email': {
                'unique': _("This email address is already in use."),
            },
        }


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        # 'address', 'phone', 'date_of_birth', 'created_at', 'updated_at', 'images', 'links', 'media'
        fields = ('username', 'email', 'first_name', 'last_name',)
        labels = {
            'username': _('Username'),
            'email': _('Email Address'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'address': _('Address'),
            'phone': _('Phone Number'),
            'date_of_birth': _('Date of Birth'),
            'created_at': _('Created At'),
            'updated_at': _('Updated At'),
            'images': _('Images'),
            'links': _('Links'),
            'media': _('Media'),
            
        }
        help_texts = {
            'username': _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
            'email': _('Required. Enter a valid email address.'),
        }
        error_messages = {
            'username': {
                'max_length': _("This username is too long."),
                'unique': _("This username is already taken."),
            },
            'email': {
                'unique': _("This email address is already in use."),
            },
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'username': _('Username'),
            'email': _('Email Address'),
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
        }
        help_texts = {
            'username': _('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
            'email': _('Required. Enter a valid email address.'),
        }
        error_messages = {
            'username': {
                'max_length': _("This username is too long."),
                'unique': _("This username is already taken."),
            },
            'email': {
                'unique': _("This email address is already in use."),
            },
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'address', 'date_of_birth')
        labels = {
            'phone': _('Phone Number'),
            'address': _('Address'),
            'date_of_birth': _('Date of Birth'),
        }
        help_texts = {
            'phone': _('Enter a valid phone number.'),
            'address': _('Enter your address.'),
            'date_of_birth': _('Enter your date of birth.'),
        }
        error_messages = {
            'phone': {
                'invalid': _("Enter a valid phone number."),
            },
            'address': {
                'max_length': _("This address is too long."),
            },
        }        