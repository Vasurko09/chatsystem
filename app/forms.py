from django import forms
from .models import Message,User2

class MsgForm(forms.ModelForm):
    class Meta:
        model =Message
        fields = ["msg"]
class User2Form(forms.ModelForm):
    class Meta:
        model = User2
        fields = ["msg"]