from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser



class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Conformation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

    
    def clean(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 is not None and password1 != password2:
            self.add_error("password_2", "Your passwords must match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class UserAdminChangeForm(forms.ModelForm):
    password1 = ReadOnlyPasswordHashField()
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'name','is_active', 'is_admin')

    def clean_password(self):
        return self.initial['password']







