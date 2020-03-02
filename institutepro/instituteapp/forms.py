from django import forms
from multiselectfield import MultiSelectFormField

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="enter the name",
        widget=forms.TextInput(
            attrs={
                'class':'forms-control',
                'placeholder':'your name'
            }
        )
    )

    rating=forms.IntegerField(
        label="enter your rating",
        widget=forms.NumberInput(
            attrs={
                'class':'forms-control',
                'placeholder':'your rating'
            }
        )
    )
    feedback=forms.CharField(
        label="enter your feedback ",
        widget=forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'your feedback'
            }
        )
    )
class ContactForm(forms.Form):
    name=forms.CharField(
        label="enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    mobile=forms.IntegerField(
        label="enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile number'
            }
        )
    )
    email=forms.EmailField(
        label="enter your email id",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email id'
            }
        )
    )
    COURSES_CHOICES=(
        ('python','python'),
        ('django','django'),
        ('UI','UI'),
        ('Rest API','Rest API'),
        ('Flask','Flask'),
        ('Mysql','Mysql')
    )
    courses=MultiSelectFormField(choices=COURSES_CHOICES,label="select your required courses")
    TRAINERS_CHOICES=(
        ('Narayana','Narayana'),
        ('Mahesh','Mahesh'),
        ('Mohan Reddy','Mohan Reddy'),
        ('srinivas','srinivas'),
        ('wilson','wilson')
    )
    trainers=MultiSelectFormField (choices=TRAINERS_CHOICES,label='select your Trainer')
    LOCATIONS_CHOICES=(
        ('Hyd','Hyd'),
        ('Bang','Bang'),
        ('pune','pune'),
        ('Delhi','Delhi'),
        ('chennai','chennai')
    )
    locations=MultiSelectFormField(
        choices=LOCATIONS_CHOICES,
        label="select your required Locations"
    )
    SHIFTS_CHOICES=(
        ('Morning','Morning'),
        ('Afternoon','Afternoon'),
        ('Evening','Evening'),
        ('Night','Night')
    )
    shifts=MultiSelectFormField(
        choices=SHIFTS_CHOICES,
        label="select your comfortable shifts"
    )
    GENDER_CHOICES=(
        ('Male','MALE'),
        ('Female','FEMALE')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=GENDER_CHOICES,
        label="select your gender:"
    )
    start_date=forms.DateField(
        widget=forms.SelectDateWidget(

        )
    )






























