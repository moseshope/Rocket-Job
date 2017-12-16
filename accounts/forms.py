from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import (
    authenticate,
#    get_user_model,
#    login,
#    logout,
)

class SignUpFormF(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid Email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')



class SignUpFormE(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid Email address.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class login_form(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        #if username and password:
        #    user = authenticate(username=username, password=password)
        #    if not user:
        #        raise forms.ValidationError("Not exist")

    class Meta:
        model = User
        fields = ('username', 'password')


#User = get_user_model()

#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
#    confirmpassword = forms.CharField(widget=forms.PasswordInput)
#
#    class Meta:
#        model = User
#        fields = ['email', 'username', 'password', 'confirmpassword']


#class UserLoginForm(forms.ModelForm):
#    username = forms.CharField()
#    password = forms.CharField(widget=forms.PasswordInput)

#    def clean(self, *args, **kwargs):
#        username = self.cleand_data.get("username")
#        password = self.cleand_data.get("password")

#        if username and password:
#            user = authenticate(username=username, password=password)
#            if not user:
#                raise forms.ValidationError("This user does not exist!")

#            if not user.check_password(password):
#                raise forms.ValidationError("Incorrect password!")

#            if not user.is_active:
#                raise forms.ValidationError("This user is no longer active.")

#        class Meta:
#            model = User
#            fields = ['username', 'password']
        #return super(UserLoginForm, self).clean(*args, **kwargs)
