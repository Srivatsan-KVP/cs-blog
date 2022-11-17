from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    nickname = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class BlogForm(forms.Form):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea())

class ReplyForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea())