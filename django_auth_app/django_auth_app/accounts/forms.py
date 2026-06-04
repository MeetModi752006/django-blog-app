from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class RegisterForm(UserCreationForm):
    """
    Registration form that extends Django's built-in UserCreationForm.
    Adds email, first name, and last name fields.
    """
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=150, required=False, help_text='Optional.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        """Override save to also create a UserProfile for the new user."""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            # Automatically create a UserProfile with 'regular' role
            UserProfile.objects.create(user=user, role='regular')
        return user


class ProfileUpdateForm(forms.ModelForm):
    """Form to update user profile details."""
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }


class UserUpdateForm(forms.ModelForm):
    """Form to update basic User fields."""
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
