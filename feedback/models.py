from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User

# Create your models here.

CLASS_CHOICES = (
    ('1 ICSE ', '1 ICSE '),
    ('1 CBSE', '1 CBSE'),
    ('2 ICSE', '2 ICSE'),
    ('2 CBSE', '2 CBSE'),
    ('3 ICSE', '3 ICSE'),
    ('3A CBSE', '3A CBSE'),
    ('3B CBSE', '3B CBSE'),
    ('4A ICSE', '4A ICSE'),
    ('4B ICSE', '4B ICSE'),
    ('4 CBSE', '4 CBSE'),
    ('5A ICSE', '5A ICSE'),
    ('5B ICSE', '5B ICSE'),
    ('5 CBSE', '5 CBSE'),
    ('6A ICSE', '6A ICSE'),
    ('6B ICSE', '6B ICSE'),
    ('6 CBSE', '6 CBSE'),
    ('7A ICSE', '7A ICSE'),
    ('7B ICSE', '7B ICSE'),
    ('7 CBSE', '7 CBSE'),
    ('8 ICSE', '8 ICSE'),
    ('8 CBSE', '8 CBSE'),
    ('9 ICSE', '9 ICSE'),
    ('9 CBSE', '9 CBSE'),
    ('10 ICSE', '10 ICSE'),
    ('10 CBSE', '10 CBSE')
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
    ('Laptop With Projector', 'Laptop With Projector'),
    ('Model From Lab', 'Model From Lab'),
    ('Live Model', 'Live Model'),
    ('Magnets', 'Magnets'),
    ('Electrical Circuits', 'Electrical Circuits'),
    ('Charts', 'Charts'),
    ('Glass Slab', 'Glass Slab'),
    ('Prism', 'Prism'),
    ('Materials Around Them', 'Materials Around Them'),
    ('Flash Cards', 'lash Cards'),
    ('Dictionary', 'Dictionary'),
    ('Textbook/sm/hm', 'Textbook/sm/hm'),
    ('Beads/abacus', 'Beads/abacus'),
    ('Lens / Mirrors', 'ens / Mirrors'),
    ('Weighing Machines', 'Weighing Machines'),
    ('Spirit Lamp', 'Spirit Lamp'),
    ('Lab Glass Materials And Chemicals', 'Lab Glass Materials And Chemicals'),
    ('Newspapaer Clip', 'Newspapaer Clip'),
    ('Globe', 'Globe'),
    ('Maps', 'Maps'),
    ('Measurement Tapes', 'Measurement Tapes'),
    ('Clock', 'Clock'),
    ('Number Blocks', 'Number Blocks'),
    ('Seeds', 'Seeds'),
    ('Audio Players', 'Audio Players'),
    ('Others', 'Others'),
    ('Atlas', 'Atlas'),
)

STATUS_CHOICES = (
    ('Approved', 'Approved'),
    ('Review', 'Review'),
    ('Pending', 'Pending'),
)

AUDITORY_CHOICES = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

User = settings.AUTH_USER_MODEL


class BlogPostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)


class Post(models.Model):
    # MAIN INPUT START

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    CLASS_NAME = models.CharField(max_length=150, choices=CLASS_CHOICES, default='', blank=True)
    SUBJECT = models.CharField(max_length=150, choices=SUBJECT_CHOICES, default='', blank=True)
    NAME_OF_THE_LESSON = models.CharField(max_length=500, default='', blank=False)

    FROM_DATE = models.DateField(default=datetime.date.today)
    TO_DATE = models.DateField(default=datetime.date.today)

    AREA_OF_INTEREST = MultiSelectField(choices=AREA_OF_INTEREST, default='', blank=True)

    INSTRUCTIONAL_OBJECTIVE_1 = models.CharField(max_length=500,  blank=True, null=True)
    INSTRUCTIONAL_OBJECTIVE_2 = models.CharField(max_length=500, blank=True, null=True)
    INSTRUCTIONAL_OBJECTIVE_3 = models.CharField(max_length=500,  blank=True, null=True)
    INSTRUCTIONAL_OBJECTIVE_4 = models.CharField(max_length=500,  blank=True, null=True)
    INSTRUCTIONAL_OBJECTIVE_5 = models.CharField(max_length=500,  blank=True, null=True)

    STUDENTS_EXPERIENCE_VISUAL = models.CharField(max_length=150, default='', blank=True)
    AUDITORY = models.CharField(max_length=150, default='', blank=True)
    FINE_MOTOR = models.CharField(max_length=150, default='', blank=True)
    GROSS_MOTOR = models.CharField(max_length=150, default='', blank=True)

    # TEACHING_POINT_1
    TEACHING_POINT_1 = models.CharField(max_length=500, default='', blank=True)
    DOMAIN = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='', blank=True)
    TYPE_OF_LEARNING_ACTIVITY_1 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='',
                                                   blank=True)
    LEARNING_ACTIVITY = models.CharField(max_length=500, default='', blank=True)
    INTELLIGENCE_USED = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='', blank=True)
    IMAGE_IF_ANY = models.ImageField(upload_to='images/', default='', blank=True)
    VIDEO_LINK_IF_ANY = models.CharField(max_length=1500, default='', blank=True)
    LEARNING_MATERIAL_USED = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='', blank=True)
    ASSESSMENT_OF_LEARNING_ACTIVITY = models.CharField(max_length=500, default='', blank=True)

    # TEACHING_POINT_2
    TEACHING_POINT_2 = models.CharField(max_length=500, default='', blank=True)
    DOMAIN_2 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='', blank=True)
    TYPE_OF_LEARNING_ACTIVITY_2 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='',
                                                   blank=True)
    LEARNING_ACTIVITY_2 = models.CharField(max_length=500, default='', blank=True)
    INTELLIGENCE_USED_2 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='', blank=True)
    IMAGE_IF_ANY_2 = models.ImageField(upload_to='images/', default='', blank=True)
    VIDEO_LINK_IF_ANY_2 = models.CharField(max_length=1500, default='', blank=True)
    LEARNING_MATERIAL_USED_2 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='', blank=True)
    ASSESSMENT_OF_LEARNING_ACTIVITY_2 = models.CharField(max_length=500, default='', blank=True)

    # TEACHING_POINT_3
    TEACHING_POINT_3 = models.CharField(max_length=500, default='', blank=True)
    DOMAIN_3 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='', blank=True)
    TYPE_OF_LEARNING_ACTIVITY_3 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='',
                                                   blank=True)
    LEARNING_ACTIVITY_3 = models.CharField(max_length=500, default='', blank=True)
    INTELLIGENCE_USED_3 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='', blank=True)
    IMAGE_IF_ANY_3 = models.ImageField(upload_to='images/', default='', blank=True)
    VIDEO_LINK_IF_ANY_3 = models.CharField(max_length=1500, default='', blank=True)
    LEARNING_MATERIAL_USED_3 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='', blank=True)
    ASSESSMENT_OF_LEARNING_ACTIVITY_3 = models.CharField(max_length=500, default='', blank=True)

    # TEACHING_POINT_4
    TEACHING_POINT_4 = models.CharField(max_length=500, default='', blank=True)
    DOMAIN_4 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='', blank=True)
    TYPE_OF_LEARNING_ACTIVITY_4 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='',
                                                   blank=True)
    LEARNING_ACTIVITY_4 = models.CharField(max_length=500, default='', blank=True)
    INTELLIGENCE_USED_4 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='', blank=True)
    IMAGE_IF_ANY_4 = models.ImageField(upload_to='images/', default='', blank=True)
    VIDEO_LINK_IF_ANY_4 = models.CharField(max_length=1500, default='', blank=True)
    LEARNING_MATERIAL_USED_4 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='', blank=True)
    ASSESSMENT_OF_LEARNING_ACTIVITY_4 = models.CharField(max_length=500, default='', blank=True)

    # TEACHING_POINT_4
    TEACHING_POINT_5 = models.CharField(max_length=500, default='', blank=True)
    DOMAIN_5 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='', blank=True)
    TYPE_OF_LEARNING_ACTIVITY_5 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='',
                                                   blank=True)
    LEARNING_ACTIVITY_5 = models.CharField(max_length=500, default='', blank=True)
    INTELLIGENCE_USED_5 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='', blank=True)
    IMAGE_IF_ANY_5 = models.ImageField(upload_to='images/', default='', blank=True)
    VIDEO_LINK_IF_ANY_5 = models.CharField(max_length=1500, default='', blank=True)
    LEARNING_MATERIAL_USED_5 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='', blank=True)
    ASSESSMENT_OF_LEARNING_ACTIVITY_5 = models.CharField(max_length=500, default='', blank=True)

    # FINAL FORM
    HOMEWORK = models.TextField(blank=True)
    COMMENTS = models.TextField(blank=True)
    STATUS = models.CharField(max_length=150, choices=STATUS_CHOICES, default='Pending', blank=True)

    # Updateded Date&time
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date', '-updated', '-timestamp']

    def __str__(self):
        return str(self.user)
