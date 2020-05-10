from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms



class Edit(UserChangeForm):
    password = forms.CharField(label='',widget=forms.TextInput(attrs={'type':'hidden'}))
    class Meta:
        model = User
        fields = ("username", 'first_name',"last_name",'email','password')





class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='',  widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter yout email'}))
    first_name = forms.CharField(help_text='enter your first name', label='', max_length=100,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter first name'}))
    last_name = forms.CharField(label='', max_length=100,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Enter last name'}))

    class Meta:
        model = User
        fields = ("username", 'first_name',"last_name",'email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = 'form-control'
        self.fields["username"].widget.attrs["placeholder"] = 'enter username'
        self.fields["username"].label= ''
        self.fields["username"].help_text = '<small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small>'
        self.fields["password1"].widget.attrs["class"] = 'form-control'
        self.fields["password2"].widget.attrs["class"] = 'form-control'
        self.fields["password1"].widget.attrs["placeholder"] = 'password'
        self.fields["password2"].widget.attrs["placeholder"] = 'password'
        self.fields["password1"].label= ''
        self.fields["password2"].label= ''


