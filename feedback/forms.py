from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post

        AUDITORY_CHOICES = (
            ('11', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        )

        AUDITORY = forms.ChoiceField(widget=forms.RadioSelect, choices=AUDITORY_CHOICES)

        fields = "__all__"
