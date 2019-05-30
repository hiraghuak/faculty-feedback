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

AUDITORY_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        fields = [
            'CLASS_NAME',
            'SUBJECT',
            'NAME_OF_THE_LESSON',

            'INSTRUCTIONAL_OBJECTIVE_1',
            'INSTRUCTIONAL_OBJECTIVE_2',
            'INSTRUCTIONAL_OBJECTIVE_3',
            'INSTRUCTIONAL_OBJECTIVE_4',
            'INSTRUCTIONAL_OBJECTIVE_5',

            'AREA_OF_INTEREST',
            'STUDENTS_EXPERIENCE_VISUAL',
            'AUDITORY',
            'FINE_MOTOR',
            'GROSS_MOTOR',


            # TEACHING_POINT_1
            'TEACHING_POINT_1',
            'DOMAIN',
            'TYPE_OF_LEARNING_ACTIVITY_1',
            'LEARNING_ACTIVITY',
            'INTELLIGENCE_USED',
            'IMAGE_IF_ANY',
            'VIDEO_LINK_IF_ANY',
            'LEARNING_MATERIAL_USED',
            'ASSESSMENT_OF_LEARNING_ACTIVITY',


            # TEACHING_POINT_2
            'TEACHING_POINT_2',
            'DOMAIN_2',
            'TYPE_OF_LEARNING_ACTIVITY_2',
            'LEARNING_ACTIVITY_2',
            'INTELLIGENCE_USED_2',
            'IMAGE_IF_ANY_2',
            'VIDEO_LINK_IF_ANY_2',
            'LEARNING_MATERIAL_USED_2',
            'ASSESSMENT_OF_LEARNING_ACTIVITY_2',

            # TEACHING_POINT_3
            'TEACHING_POINT_3',
            'DOMAIN_3',
            'TYPE_OF_LEARNING_ACTIVITY_3',
            'LEARNING_ACTIVITY_3',
            'INTELLIGENCE_USED_3',
            'IMAGE_IF_ANY_3',
            'VIDEO_LINK_IF_ANY_3',
            'LEARNING_MATERIAL_USED_3',
            'ASSESSMENT_OF_LEARNING_ACTIVITY_3',

            # TEACHING_POINT_4
            'TEACHING_POINT_4',
            'DOMAIN_4',
            'TYPE_OF_LEARNING_ACTIVITY_4',
            'LEARNING_ACTIVITY_4',
            'INTELLIGENCE_USED_4',
            'IMAGE_IF_ANY_4',
            'VIDEO_LINK_IF_ANY_4',
            'LEARNING_MATERIAL_USED_4',
            'ASSESSMENT_OF_LEARNING_ACTIVITY_4',

            # TEACHING_POINT_5
            'TEACHING_POINT_5',
            'DOMAIN_5',
            'TYPE_OF_LEARNING_ACTIVITY_5',
            'LEARNING_ACTIVITY_5',
            'INTELLIGENCE_USED_5',
            'IMAGE_IF_ANY_5',
            'VIDEO_LINK_IF_ANY_5',
            'LEARNING_MATERIAL_USED_5',
            'ASSESSMENT_OF_LEARNING_ACTIVITY_5',


            # LAST FORM
            'HOMEWORK',
            'COMMENTS',
            'STATUS',
            'publish_date',
        ]

        # NAME_OF_THE_LESSON = forms.CharField(widget=forms.Textarea)
        # widgets = {
        #     'AUDITORY': forms.ChoiceField(attrs={
        #   'type' : 'radio',
        #   'class' : 'your_class'
        #     },widget=forms.RadioSelect(),choices=AUDITORY_CHOICES)
        # }

        # exclude = [
        #     'user',
        # ]