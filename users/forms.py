
from .models import Profile, Message
from django.forms import ModelForm, fields

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'bio', 'dp', 'facebook', 'twitter', 'dribbble', 'website']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'body']

    # def __init__(self, *args, **kwargs):
    #     super(MessageForm, self).__init__(*args, **kwargs)

    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'input'})
