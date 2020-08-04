from django import forms
from .models import Trainee, Trainer, Financial
from django.core.validators import RegexValidator

alpha = RegexValidator(r'^[a-zA-Z]*$', 'Only alphabets are allowed')
new = RegexValidator(r'^\(\d{3}\)*\d{3}[-]??\d{4}$', 'Invalid Contact')


class TraneeForm(forms.ModelForm):
    des = (('Lead','LEAD'),('Prospect','PROSPECT'),('In Training','IN TRAINING'),('Completed','COMPLETED'),
           ('Rejected','REJECTED'),('Invalid','INVALID'))
    fname = forms.CharField(label="First Name",validators=[alpha])
    lname = forms.CharField(label="Last Name",validators=[alpha])
    addressl1 = forms.CharField(label="Address Lane 1")
    addressl2 = forms.CharField(label="Address Lane 2")
    city = forms.CharField(label="City",validators=[alpha])
    state = forms.CharField(label="State",validators=[alpha])
    zipcode = forms.CharField(label="Zip Code")
    country = forms.CharField(label="Country",validators=[alpha])
    jobtitle = forms.CharField(label="Job Title",validators=[alpha])
    technology = forms.CharField(label="Technology",validators=[alpha])
    rate = forms.FloatField(label="Rate")
    phone = forms.CharField(label="Consultant Phone",validators=[new])
    email = forms.EmailField(label="Consultant Email")
    startdate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':"YYYY-MM-DD"}),label="Training Start Date")
    enddate = forms.DateField(widget=forms.DateInput(attrs={'placeholder':"YYYY-MM-DD"}),label="Training End Date")
    trainer = forms.CharField(label="Trainer")
    status = forms.ChoiceField(label="Status",choices=des)

    class Meta:
        model = Trainee
        fields = "__all__"


class TrainerForm(forms.ModelForm):
    fname = forms.CharField(label="First Name", validators=[alpha])
    lname = forms.CharField(label="Last Name", validators=[alpha])
    addressl1 = forms.CharField(label="Address Lane 1")
    addressl2 = forms.CharField(label="Address Lane 2")
    city = forms.CharField(label="City", validators=[alpha])
    state = forms.CharField(label="State", validators=[alpha])
    zipcode = forms.CharField(label="Zip Code")
    country = forms.CharField(label="Country", validators=[alpha])
    jobtitle = forms.CharField(label="Job Title", validators=[alpha])
    technology = forms.CharField(label="Technology", validators=[alpha])
    rate = forms.FloatField(label="Rate")
    phone = forms.CharField(label="Consultant Phone", validators=[new])
    email = forms.EmailField(label="Consultant Email")

    class Meta:
        model = Trainer
        fields = "__all__"


class FinancialForm(forms.ModelForm):
    class Meta:
        model = Financial
        fields = "__all__"

