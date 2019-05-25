from django import forms
from .models import Post


# class PostFormM(forms.Form):
#     # content = forms.CharField(widget=forms.Textarea)
#
#     user = forms.CharField()
#     CLASS_NAME = forms.CharField()
#     SUBJECT = forms.CharField()
#     NAME_OF_THE_LESSON = forms.CharField()
#     AREA_OF_INTEREST = forms.CharField()
#     STUDENTS_EXPERIENCE_VISUAL = forms.CharField()
#     AUDITORY = forms.CharField()
#     FINE_MOTOR = forms.CharField()
#     GROSS_MOTOR = forms.CharField()
#     TEACHING_POINT_1 = forms.CharField()
#     DOMAIN = forms.CharField()
#     TYPE_OF_LEARNING_ACTIVITY_1 = forms.CharField()
#     LEARNING_ACTIVITY = forms.CharField()
#     INTELLIGENCE_USED = forms.CharField()
#     IMAGE_IF_ANY = forms.CharField()
#     VIDEO_LINK_IF_ANY = forms.CharField()
#     LEARNING_MATERIAL_USED = forms.CharField()
#     ASSESSMENT_OF_LEARNING_ACTIVITY = forms.CharField()
#     HOMEWORK = forms.CharField()
#     COMMENTS = forms.CharField()
#     STATUS = forms.CharField()
#     publish_date = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        # NAME_OF_THE_LESSON = forms.CharField(widget=forms.Textarea)
        fields = [
            'CLASS_NAME',
            'SUBJECT',

            'NAME_OF_THE_LESSON',
            'AREA_OF_INTEREST',
            'STUDENTS_EXPERIENCE_VISUAL',
            'AUDITORY',
            'FINE_MOTOR',
            'GROSS_MOTOR',
            'TEACHING_POINT_1',
            'DOMAIN',
            'TYPE_OF_LEARNING_ACTIVITY_1',
            'LEARNING_ACTIVITY',
            'INTELLIGENCE_USED',
            'IMAGE_IF_ANY',
            'VIDEO_LINK_IF_ANY',
            'LEARNING_MATERIAL_USED',
            'ASSESSMENT_OF_LEARNING_ACTIVITY',
            'HOMEWORK',
            'COMMENTS',
            'STATUS',
        ]

        # exclude = [
        #     'user',
        # ]