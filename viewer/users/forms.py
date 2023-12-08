from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for item in self.fields:
        #     self.fields[str(item)].widget.attrs.update({
        #     'class': 'input',
        #     'type': 'text',
        # })
        self.fields["username"].widget.attrs.update({
            'class': 'input',
            'type': 'text',
        })
        
        self.fields["password1"].widget.attrs.update({
            'class': 'input',
            'type': 'text',
        })
        
        self.fields["password2"].widget.attrs.update({
            'class': 'input',
            'type': 'text',
        })
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
