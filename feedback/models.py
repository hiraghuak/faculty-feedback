from django.db import models
import datetime
from multiselectfield import MultiSelectField

# Create your models here.

CLASS_CHOICES = (
    ('1_ICSE ', '1 ICSE '),
    ('1_CBSE', '1 CBSE'),
    ('2_ICSE', '2 ICSE'),
    ('2_CBSE', '2 CBSE'),
    ('3_ICSE', '3 ICSE'),
    ('3A_CBSE', '3A CBSE'),
    ('3B_CBSE', '3B CBSE'),
    ('4A_ICSE', '4A ICSE'),
    ('4B_ICSE', '4B ICSE'),
    ('4_CBSE', '4 CBSE'),
    ('5A_ICSE', '5A ICSE'),
    ('5B_ICSE', '5B ICSE'),
    ('5_CBSE', '5 CBSE'),
    ('6A_ICSE', '6A ICSE'),
    ('6B_ICSE', '6B ICSE'),
    ('6_CBSE', '6 CBSE'),
    ('7A_ICSE', '7A ICSE'),
    ('7B_ICSE', '7B ICSE'),
    ('7_CBSE', '7 CBSE'),
    ('8_ICSE', '8 ICSE'),
    ('8_CBSE', '8 CBSE'),
    ('9_ICSE', '9 ICSE'),
    ('9_CBSE', '9 CBSE'),
    ('10_ICSE', '10 ICSE'),
    ('10_CBSE', '10 CBSE')
)

SUBJECT_CHOICES = (

    ('Choose ', 'Choose'),
    ('ENGLISH_LANGUAGE', 'ENGLISH_LANGUAGE'),
    ('ENGLISH_LITERATURE', 'ENGLISH_LITERATURE'),
    ('KANNADA', 'KANNADA'),
    ('HINDI', 'HINDI'),
    ('MATHEMATICS', 'MATHEMATICS'),
    ('EVS', 'EVS'),
    ('SCIENCE', 'SCIENCE'),
    ('SOCIAL_STUDIES', 'SOCIAL_STUDIES'),
    ('PHYSICS', 'PHYSICS'),
    ('CHEMISTRY', 'CHEMISTRY'),
    ('BIOLOGY', 'BIOLOGY'),
    ('HISTORY_CIVICS', 'HISTORY_CIVICS'),
    ('GEOGRAPHY', 'GEOGRAPHY'),
    ('COMPUTER_APPLICATION', 'COMPUTER_APPLICATION'),

)

DOMAIN_CHOICES = (

    ('Choose', 'Choose'),
    ('KNOWLEDGE', 'KNOWLEDGE'),
    ('UNDERSTANDING', 'UNDERSTANDING'),
    ('APPLICATION', 'APPLICATION'),
    ('ANALYSIS', 'ANALYSIS'),
    ('EVALUATION', 'EVALUATION'),
    ('CREATIVE', 'CREATIVE'),

)

AREA_OF_INTEREST = (
    ('AGE', 'AGE'),
    ('GENDER', 'GENDER'),
    ('WIDELY_DISCUSSED', 'WIDELY_DISCUSSED'),
    ('CONTEMPORARY', 'CONTEMPORARY'),
    ('WITHIN_THE_COMPETENCY_OF_CHILDREN', 'WITHIN_THE_COMPETENCY_OF_CHILDREN'),
    ('SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY', 'SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY'),
    ('DOES NOT INDUCE INTEREST', 'DOES NOT INDUCE INTEREST'),
)

AREA_OF_INTEREST_2 = (
    ('AGE', 'AGE'),
    ('GENDER', 'GENDER'),
    ('WIDELY_DISCUSSED', 'WIDELY_DISCUSSED'),
    ('CONTEMPORARY', 'CONTEMPORARY'),
    ('WITHIN_THE_COMPETENCY_OF_CHILDREN', 'WITHIN_THE_COMPETENCY_OF_CHILDREN'),
    ('SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY', 'SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY'),
    ('DOES NOT INDUCE INTEREST', 'DOES NOT INDUCE INTEREST'),
)

AREA_OF_INTEREST_3 = (
    ('AGE', 'AGE'),
    ('GENDER', 'GENDER'),
    ('WIDELY_DISCUSSED', 'WIDELY_DISCUSSED'),
    ('CONTEMPORARY', 'CONTEMPORARY'),
    ('WITHIN_THE_COMPETENCY_OF_CHILDREN', 'WITHIN_THE_COMPETENCY_OF_CHILDREN'),
    ('SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY', 'SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY'),
    ('DOES NOT INDUCE INTEREST', 'DOES NOT INDUCE INTEREST'),
)

AREA_OF_INTEREST_4 = (
    ('AGE', 'AGE'),
    ('GENDER', 'GENDER'),
    ('WIDELY_DISCUSSED', 'WIDELY_DISCUSSED'),
    ('CONTEMPORARY', 'CONTEMPORARY'),
    ('WITHIN_THE_COMPETENCY_OF_CHILDREN', 'WITHIN_THE_COMPETENCY_OF_CHILDREN'),
    ('SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY', 'SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY'),
    ('DOES NOT INDUCE INTEREST', 'DOES NOT INDUCE INTEREST'),
)

AREA_OF_INTEREST_5 = (
    ('AGE', 'AGE'),
    ('GENDER', 'GENDER'),
    ('WIDELY_DISCUSSED', 'WIDELY_DISCUSSED'),
    ('CONTEMPORARY', 'CONTEMPORARY'),
    ('WITHIN_THE_COMPETENCY_OF_CHILDREN', 'WITHIN_THE_COMPETENCY_OF_CHILDREN'),
    ('SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY', 'SOCIAL-RELIGIOUS-LINGUISTIC-NATIONAL-IDENTITY'),
    ('DOES NOT INDUCE INTEREST', 'DOES NOT INDUCE INTEREST'),
)

TYPE_OF_LEARNING_ACTIVITY_1_CHOICES = (

    ('Choose', 'Choose'),
    ('DEMO_WITH_VISUAL_AID', 'DEMO_WITH_VISUAL_AID'),
    ('DEMO_WITH_TEACHING_AID', 'DEMO_WITH_TEACHING_AID'),
    ('DEMO_WITH_LEARNING_AID', 'DEMO_WITH_LEARNING_AID'),
    ('DEMO_WITH_WHITE_BOARD', 'DEMO_WITH_WHITE_BOARD'),
    ('DISCUSSION', 'DISCUSSION'),
    ('ORAL', 'ORAL'),
    ('RHYMES_RECITATION', 'RHYMES_RECITATION'),
    ('PEOPLE_PLAY', 'PEOPLE_PLAY'),

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
    ('VERBAL LINGUISTIC	', 'VERBAL LINGUISTIC'),
    ('MATHEMATICAL', 'MATHEMATICAL'),
    ('MUSICAL', 'MUSICAL'),
    ('VISUAL - SPACIAL', 'VISUAL - SPACIAL'),
    ('BODILY KINESTHETIC', 'BODILY KINESTHETIC'),
    ('INTRAPERSONAL', 'INTRAPERSONAL'),
    ('NATURALIST', 'NATURALIST'),
    ('EXISTENTIAL', 'EXISTENTIAL'),
)

LEARNING_MATERIAL_USED_CHOICES = (
    ('WHITEBOARD', 'WHITEBOARD'),
    ('LAPTOP WITH PROJECTOR', 'LAPTOP WITH PROJECTOR'),
    ('MODEL FROM LAB', 'MODEL FROM LAB'),
    ('LIVE MODEL', 'LIVE MODEL'),
    ('MAGNETS', 'MAGNETS'),
    ('ELECTRICAL CIRCUITS', 'ELECTRICAL CIRCUITS'),
    ('CHARTS', 'CHARTS'),
)

STATUS_CHOICES = (
    ('Choose', 'Choose'),
    ('APPROVED', 'APPROVED'),
    ('EDIT_AND_RESEND', 'EDIT_AND_RESEND'),
)


class Post(models.Model):
    # title = models.TextField()  # text Area
    # name = models.CharField(max_length=500, default='null')  # input
    # cover = models.ImageField(upload_to='images/')  # file upload
    # class_select = models.CharField(max_length=150, choices=CLASS_CHOICES, default='1_ICSE')  # Drop Down
    # my_field = MultiSelectField(choices=SUBJECT_CHOICES, default='item_key1')  # multiple Choices
    # display = models.CharField(max_length=1, choices=FAVORITE_COLORS_CHOICES, blank=True, null=True)  # Drop Down

    # MAIN INPUT START

    CLASS_NAME = models.CharField(max_length=150, choices=CLASS_CHOICES, default='null' )
    SUBJECT = models.CharField(max_length=150, choices=SUBJECT_CHOICES, default='null')
    NAME_OF_THE_LESSON = models.CharField(max_length=500, default='null')
    # FROM_DATE = models.DateField(default=datetime.date.today)
    # TO_DATE = models.DateField(default=datetime.date.today)
    INSTRUCTIONAL_OBJECTIVE_1 = models.CharField(max_length=500, default='null')
    INSTRUCTIONAL_OBJECTIVE_2 = models.CharField(max_length=500, default='null')
    INSTRUCTIONAL_OBJECTIVE_3 = models.CharField(max_length=500, default='null')
    INSTRUCTIONAL_OBJECTIVE_4 = models.CharField(max_length=500, default='null')
    INSTRUCTIONAL_OBJECTIVE_5 = models.CharField(max_length=500, default='null')

    # TEACHING_POINT_1
    TEACHING_POINT_1 = models.CharField(max_length=500, default='null')
    DOMAIN = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='null')
    AREA_OF_INTEREST = MultiSelectField(choices=AREA_OF_INTEREST, default='AGE', blank=False)
    TYPE_OF_LEARNING_ACTIVITY_1 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='Choose')
    LEARNING_ACTIVITY = models.CharField(max_length=500, default='null')
    STUDENTS_EXPERIENCE_VISUAL = models.CharField(max_length=150,
                                                  choices=STUDENTS_EXPERIENCE_VISUAL_CHOICES, default='1', blank=False)
    AUDITORY = models.CharField(max_length=150, choices=AUDITORY_CHOICES, default='1')
    FINE_MOTOR = models.CharField(max_length=150, choices=FINE_MOTOR_CHOICES, default='1')
    GROSS_MOTOR = models.CharField(max_length=150, choices=GROSS_MOTOR_CHOICES, default='1')
    INTELLIGENCE_USED = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='NULL')
    IMAGE_IF_ANY = models.ImageField(upload_to='images/')
    VIDEO_LINK_IF_ANY = models.CharField(max_length=1500, default='null')
    LEARNING_MATERIAL_USED = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='NULL')
    ASSESSMENT_OF_LEARNING_ACTIVITY = models.CharField(max_length=500, default='null')

    # TEACHING_POINT_2
    TEACHING_POINT_2 = models.CharField(max_length=500, default='null')
    DOMAIN_2 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='null')
    AREA_OF_INTEREST_2 = MultiSelectField(choices=AREA_OF_INTEREST_2, default='AGE')
    TYPE_OF_LEARNING_ACTIVITY_2 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='Choose')
    LEARNING_ACTIVITY_2 = models.CharField(max_length=500, default='null')
    STUDENTS_EXPERIENCE_VISUAL_2 = models.CharField(max_length=150,
                                                    choices=STUDENTS_EXPERIENCE_VISUAL_CHOICES, default='1',
                                                    blank=False)
    AUDITORY_2 = models.CharField(max_length=150, choices=AUDITORY_CHOICES, default='1')
    FINE_MOTOR_2 = models.CharField(max_length=150, choices=FINE_MOTOR_CHOICES, default='1')
    GROSS_MOTOR_2 = models.CharField(max_length=150, choices=GROSS_MOTOR_CHOICES, default='1')
    INTELLIGENCE_USED_2 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='NULL')
    IMAGE_IF_ANY_2 = models.ImageField(upload_to='images/')
    VIDEO_LINK_IF_ANY_2 = models.CharField(max_length=1500, default='null')
    LEARNING_MATERIAL_USED_2 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='NULL')
    ASSESSMENT_OF_LEARNING_ACTIVITY_2 = models.CharField(max_length=500, default='null')

    # TEACHING_POINT_3
    TEACHING_POINT_3 = models.CharField(max_length=500, default='null')
    DOMAIN_3 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='null')
    AREA_OF_INTEREST_3 = MultiSelectField(choices=AREA_OF_INTEREST_3, default='AGE')
    TYPE_OF_LEARNING_ACTIVITY_3 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='Choose')
    LEARNING_ACTIVITY_3 = models.CharField(max_length=500, default='null')
    STUDENTS_EXPERIENCE_VISUAL_3 = models.CharField(max_length=150,
                                                    choices=STUDENTS_EXPERIENCE_VISUAL_CHOICES, default='1',
                                                    blank=False)
    AUDITORY_3 = models.CharField(max_length=150, choices=AUDITORY_CHOICES, default='1')
    FINE_MOTOR_3 = models.CharField(max_length=150, choices=FINE_MOTOR_CHOICES, default='1')
    GROSS_MOTOR_3 = models.CharField(max_length=150, choices=GROSS_MOTOR_CHOICES, default='1')
    INTELLIGENCE_USED_3 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='NULL')
    IMAGE_IF_ANY_3 = models.ImageField(upload_to='images/')
    VIDEO_LINK_IF_ANY_3 = models.CharField(max_length=1500, default='null')
    LEARNING_MATERIAL_USED_3 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='NULL')
    ASSESSMENT_OF_LEARNING_ACTIVITY_3 = models.CharField(max_length=500, default='null')

    # TEACHING_POINT_4
    TEACHING_POINT_4 = models.CharField(max_length=500, default='null')
    DOMAIN_4 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='null')
    AREA_OF_INTEREST_4 = MultiSelectField(choices=AREA_OF_INTEREST_4, default='AGE', blank=False)
    TYPE_OF_LEARNING_ACTIVITY_4 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='Choose')
    LEARNING_ACTIVITY_4 = models.CharField(max_length=500, default='null')
    STUDENTS_EXPERIENCE_VISUAL_4 = models.CharField(max_length=150,
                                                    choices=STUDENTS_EXPERIENCE_VISUAL_CHOICES, default='1',
                                                    blank=False)
    AUDITORY_4 = models.CharField(max_length=150, choices=AUDITORY_CHOICES, default='1')
    FINE_MOTOR_4 = models.CharField(max_length=150, choices=FINE_MOTOR_CHOICES, default='1')
    GROSS_MOTOR_4 = models.CharField(max_length=150, choices=GROSS_MOTOR_CHOICES, default='1')
    INTELLIGENCE_USED_4 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='NULL')
    IMAGE_IF_ANY_4 = models.ImageField(upload_to='images/')
    VIDEO_LINK_IF_ANY_4 = models.CharField(max_length=1500, default='null')
    LEARNING_MATERIAL_USED_4 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='NULL')
    ASSESSMENT_OF_LEARNING_ACTIVITY_4 = models.CharField(max_length=500, default='null')

    # TEACHING_POINT_5
    TEACHING_POINT_5 = models.CharField(max_length=500, default='null')
    DOMAIN_5 = models.CharField(max_length=150, choices=DOMAIN_CHOICES, default='null')
    AREA_OF_INTEREST_5 = MultiSelectField(choices=AREA_OF_INTEREST_5, default='AGE', blank=False)
    TYPE_OF_LEARNING_ACTIVITY_5 = models.CharField(max_length=150,
                                                   choices=TYPE_OF_LEARNING_ACTIVITY_1_CHOICES, default='Choose')
    LEARNING_ACTIVITY_5 = models.CharField(max_length=500, default='null')
    STUDENTS_EXPERIENCE_VISUAL_5 = models.CharField(max_length=150,
                                                    choices=STUDENTS_EXPERIENCE_VISUAL_CHOICES, default='1',
                                                    blank=False)
    AUDITORY_5 = models.CharField(max_length=150, choices=AUDITORY_CHOICES, default='1')
    FINE_MOTOR_5 = models.CharField(max_length=150, choices=FINE_MOTOR_CHOICES, default='1')
    GROSS_MOTOR_5 = models.CharField(max_length=150, choices=GROSS_MOTOR_CHOICES, default='1')
    INTELLIGENCE_USED_5 = MultiSelectField(choices=INTELLIGENCE_USED_CHOICES, default='NULL')
    IMAGE_IF_ANY_5 = models.ImageField(upload_to='images/')
    VIDEO_LINK_IF_ANY_5 = models.CharField(max_length=1500, default='null')
    LEARNING_MATERIAL_USED_5 = MultiSelectField(choices=LEARNING_MATERIAL_USED_CHOICES, default='NULL')
    ASSESSMENT_OF_LEARNING_ACTIVITY_5 = models.CharField(max_length=500, default='null')

    HOMEWORK = models.TextField()

    COMMENTS = models.TextField()
    STATUS = models.CharField(max_length=150, choices=STATUS_CHOICES, default='null')

    def __str__(self):
        return self.CLASS_NAME
