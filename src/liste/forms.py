from django import forms
from .models import Student, Item


class UpdateStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['student_ID']

    def __init__(self, *args, **kwargs):
        super(UpdateStudent, self).__init__(*args, **kwargs)
        self.fields['nickname'].required = False
        self.fields['card_ID'].required = False


class CreateItem(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['item_ID']


class UpdateName(forms.Form):
    # Wie in models.py festgelegt sind 100 Zeichen maximale Namenlänge
    nickname = forms.CharField(label="Name eingeben:", max_length=100)
