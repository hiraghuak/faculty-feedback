from django.db import models
from django.conf import settings
import datetime
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

CLASS_CHOICES = (
    ('1 Icse ', '1 Icse '),
    ('1 Cbse', '1 Cbse'),
    ('2 Icse', '2 Icse'),
    ('2 Cbse', '2 Cbse'),
    ('3 Icse', '3 Icse'),
    ('3A Cbse', '3A Cbse'),
    ('3B Cbse', '3B Cbse'),
    ('4A Icse', '4A Icse'),
    ('4B Icse', '4B Icse'),
    ('4 Cbse', '4 Cbse'),
    ('5A Icse', '5A Icse'),
    ('5B Icse', '5B Icse'),
    ('5 Cbse', '5 Cbse'),
    ('6A Icse', '6A Icse'),
    ('6B Icse', '6B Icse'),
    ('6 Cbse', '6 Cbse'),
    ('7A Icse', '7A Icse'),
    ('7B Icse', '7B Icse'),
    ('7 Cbse', '7 Cbse'),
    ('8 Icse', '8 Icse'),
    ('8 Cbse', '8 Cbse'),
    ('9 Icse', '9 Icse'),
    ('9 Cbse', '9 Cbse'),
    ('10 Icse', '10 Icse'),
    ('10 Cbse', '10 Cbse')
)

SUBJECT_CHOICES = (

    ('English Language', 'English Language'),
    ('English Literature', 'English Literature'),
    ('Kannada', 'Kannada'),
    ('Hindi', 'Hindi'),
    ('Mathematics', 'Mathematics'),
    ('Evs', 'Evs'),
    ('Science', 'Science'),
    ('Social Studies', 'Social Studies'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('History Civics', 'History Civics'),
    ('Geography', 'Geography'),
    ('Computer Application', 'Computer Application'),

)

DOMAIN_CHOICES = (

    ('Knowledge', 'Knowledge'),
    ('Understanding', 'Understanding'),
    ('Application', 'Application'),
    ('Analysis', 'Analysis'),
    ('Evaluation', 'Evaluation'),
    ('Creative', 'Creative'),

)

AREA_OF_INTEREST = (
    ('Age', 'Age'),
    ('Gender', 'Gender'),
    ('Widely Discussed', 'Widely Discussed'),
    ('Contemporary', 'Contemporary'),
    ('Within the Competency of Children', 'Within the Competency of Children'),
    ('Social Religious Linguistic National Identity', 'Social Religious Linguistic National Identity'),
    ('Does Not Induce Interest', 'Does Not Induce Interest'),
)

AREA_OF_INTEREST_2 = (
    ('Age', 'Age'),
    ('Gender', 'Gender'),
    ('Widely Discussed', 'Widely Discussed'),
    ('Contemporary', 'Contemporary'),
    ('Within the Competency of Children', 'Within the Competency of Children'),
    ('Social Religious Linguistic National Identity', 'Social Religious Linguistic National Identity'),
    ('Does Not Induce Interest', 'Does Not Induce Interest'),
)

TYPE_OF_LEARNING_ACTIVITY_1_CHOICES = (

    ('Demo with Visual_aid', 'Demo with Visual_aid'),
    ('Demo with Teaching Aid', 'Demo with Teaching Aid'),
    ('Demo with Learning Aid', 'Demo with Learning Aid'),
    ('Demo with white Board', 'Demo with white Board'),
    ('Discussion', 'Discussion'),
    ('Oral', 'Oral'),
    ('Rhymes_recitation', 'Rhymes_recitation'),
    ('People_play', 'People_play'),

)

STUDENTS_EXPERIENCE_VISUAL_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

AUDITORY_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

FINE_MOTOR_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

GROSS_MOTOR_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

INTELLIGENCE_USED_CHOICES = (
    ('Verbal Linguistic	', 'Verbal Linguistic'),
    ('Mathematical', 'Mathematical'),
    ('Musical', 'Musical'),
    ('Visual Spacial', 'Visual Spacial'),
    ('Bodily Kinesthetic', 'Bodily Kinesthetic'),
    ('Intrapersonal', 'Intrapersonal'),
    ('Naturalist', 'Naturalist'),
    ('Existential', 'Existential'),
)

LEARNING_MATERIAL_USED_CHOICES = (
    ('Whiteboard', 'Whiteboard'),
    ('Laptop with Projector', 'Laptop with Projector'),
    ('Model From Lab', 'Model From Lab'),
    ('Live Model', 'Live Model'),
    ('Magnets', 'Magnets'),
    ('Electrical Circuits', 'Electrical Circuits'),
    ('Charts', 'Charts'),
)

STATUS_CHOICES = (
    ('Approved', 'Approved'),
    ('Edit and Resend', 'Edit and Resend'),
)


class Post(models.Model):
    # title = models.TextField()  # text Area
    # name = models.CharField(max_length=500, default='')  # input
    # cover = models.ImageField(upload_to='images/')  # file upload
    # class_select = models.CharField(max_length=150, choices=CLASS_CHOICES, default='1_ICSE')  # Drop Down
    # my_field = MultiSelectField(choices=SUBJECT_CHOICES, default='item_key1')  # multiple Choices
    # display = models.CharField(max_length=1, choices=FAVORITE_COLORS_CHOICES, blank=True, =True)  # Drop Down

    # MAIN INPUT START

    CLASS_NAME = models.CharField(
        max_length=150, choices=CLASS_CHOICES, default='', blank=True)

    SUBJECT = models.CharField(max_length=150, choices=SUBJECT_CHOICES, default='', blank=True)
    NAME_OF_THE_LESSON = models.CharField(max_length=500, default='', blank=True)
    # FROM_DATE = models.DateField(default=datetime.date.today)
    # TO_DATE = models.DateField(default=datetime.date.today)
    INSTRUCTIONAL_OBJECTIVE_1 = models.CharField(max_length=500, default='', blank=True)
    INSTRUCTIONAL_OBJECTIVE_2 = models.CharField(max_length=500, default='', blank=True)
    INSTRUCTIONAL_OBJECTIVE_3 = models.CharField(max_length=500, default='', blank=True)
    INSTRUCTIONAL_OBJECTIVE_4 = models.CharField(max_length=500, default='', blank=True)
    INSTRUCTIONAL_OBJECTIVE_5 = models.CharField(max_length=500, default='', blank=True)

    # TEACHING_POINT_1
    TEACHING_POINT_1 = models.CharField(max_length=500, default='', blank=True)
    DOMAIN = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='', blank=True)
    AREA_OF_INTEREST = MultiSelectField(choices=AREA_OF_INTEREST, default='AGE', blank=False)
    TYPE_OF_LEARNING_ACTIVITY_1 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='Choose',
                                                   blank=True)
    LEARNING_ACTIVITY = models.CharField(max_length=500, default='', blank=True)
    STUDENTS_EXPERIENCE_VISUAL = models.CharField(max_length=150,
                                                  choices=STUDENTS_EXPERIENCE_VISUAL_CHOICES, default='1', blank=False)
    AUDITORY = models.CharField(max_length=150, choices=AUDITORY_CHOICES, default='', blank=True)
    FINE_MOTOR = models.CharField(max_length=150, choices=FINE_MOTOR_CHOICES, default='', blank=True)
    GROSS_MOTOR = models.CharField(max_length=150, choices=GROSS_MOTOR_CHOICES, default='', blank=True)
    INTELLIGENCE_USED = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='', blank=True)
    IMAGE_IF_ANY = models.ImageField(upload_to='images/', default='', blank=True)
    VIDEO_LINK_IF_ANY = models.CharField(max_length=1500, default='', blank=True)
    LEARNING_MATERIAL_USED = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='', blank=True)
    ASSESSMENT_OF_LEARNING_ACTIVITY = models.CharField(max_length=500, default='', blank=True)

    # TEACHING_POINT_2
    TEACHING_POINT_2 = models.CharField(max_length=500, default='', blank=True)
    DOMAIN_2 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='', blank=True)
    AREA_OF_INTEREST_2 = MultiSelectField(choices=AREA_OF_INTEREST_2, default='', blank=False)
    TYPE_OF_LEARNING_ACTIVITY_2 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='Choose',
                                                   blank=True)
    LEARNING_ACTIVITY_2 = models.CharField(max_length=500, default='')
    STUDENTS_EXPERIENCE_VISUAL_2 = models.CharField(max_length=150,
                                                    choices=STUDENTS_EXPERIENCE_VISUAL_CHOICES, default='',
                                                    blank=False)
    AUDITORY_2 = models.CharField(max_length=150, choices=AUDITORY_CHOICES, default='', blank=True)
    FINE_MOTOR_2 = models.CharField(max_length=150, choices=FINE_MOTOR_CHOICES, default='', blank=True)
    GROSS_MOTOR_2 = models.CharField(max_length=150, choices=GROSS_MOTOR_CHOICES, default='')
    INTELLIGENCE_USED_2 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='', blank=True)
    IMAGE_IF_ANY_2 = models.ImageField(upload_to='images/', default='', blank=True)
    VIDEO_LINK_IF_ANY_2 = models.CharField(max_length=1500, default='', blank=True)
    LEARNING_MATERIAL_USED_2 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='', blank=True)
    ASSESSMENT_OF_LEARNING_ACTIVITY_2 = models.CharField(max_length=500, default='', blank=True)

    HOMEWORK = models.TextField(blank=True)

    COMMENTS = models.TextField(blank=True)
    STATUS = models.CharField(max_length=150, choices=STATUS_CHOICES, default='', blank=True)

    author = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='',
    )

    def __str__(self):
        return self.CLASS_NAME


class Contact(models.Model):
    name = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name
