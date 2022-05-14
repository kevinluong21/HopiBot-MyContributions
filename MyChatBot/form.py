from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class Emergency(FlaskForm):
    emergency = StringField("Is this a life-threatening emergency?", validators=[DataRequired(), Length(max = 3)])
    submit = SubmitField()

    # def validate_emergency(form, field):
    #     field.data = field.data.lower()
    #     if field.data != "y" or field.data != "yes" or field.data != "n" or field.data != "no":
    #         raise ValidationError('Invalid input')

class HealthCard(FlaskForm):
    healthcard = IntegerField("Please enter your health card number", validators=[DataRequired(), Length(min = 10, max = 10)])
    submit = SubmitField()

class VersionCode(FlaskForm):
    version_code = StringField("Version code", validators=[DataRequired(), Length(min = 2, max = 2)])
    submit = SubmitField()

class Names(FlaskForm):
    first_name = StringField("Please enter your first name", validators=[DataRequired(), Length(min = 2, max = 20)])
    last_name = StringField("Please enter your last", validators=[DataRequired(), Length(min = 2, max = 20)])
    submit = SubmitField()

class DOB(FlaskForm):
    dob = DateField("Please enter your date of birth (YY-MM-DD)", validators=[DataRequired(), Length(min = 2, max = 8)])
    submit = SubmitField()

class PhoneNumber(FlaskForm):
    mobile_phone = IntegerField("Please enter your mobile phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    home_phone = IntegerField("Please enter your home phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    submit = SubmitField()

class Symptoms(FlaskForm):
    symptoms = SelectMultipleField("Please describe your symptoms", choices=["chronic condition", "acute illness", "trauma/poisoning", "dental", "routine preventative health care",
    "pregnancy/birth-related", "other", "none of the above"])
    submit = SubmitField()

class MedicalConditions(FlaskForm):
    medical_conditions = SelectMultipleField("Please select your pre-existing medical conditions", choices=["autoimmune disorder", "cancer", 
    "diabetes", "heart conditions", "HIV", "neurological conditions", "tuberculosis", "other", "none of the above"])
    submit = SubmitField()

#class RegistrationForm(FlaskForm):
    # emergency = StringField("Is this a life-threatening emergency?", validators=[DataRequired(), Length(max = 3)])
    # health_card = IntegerField("Please enter your health card number", validators=[DataRequired(), Length(min = 10, max = 10)])
    # version_code = StringField("Version code", validators=[DataRequired(), Length(min = 2, max = 2)])
    # first_name = StringField("Please enter your first name", validators=[DataRequired(), Length(min = 2, max = 20)])
    # last_name = StringField("Please enter your last", validators=[DataRequired(), Length(min = 2, max = 20)])
    # dob = DateField("Please enter your date of birth (YY-MM-DD)", validators=[DataRequired(), Length(min = 2, max = 8)])
    # mobile_phone = IntegerField("Please enter your mobile phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    # home_phone = IntegerField("Please enter your home phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    # symptoms = SelectMultipleField("Please describe your symptoms", choices=["chronic condition", "acute illness", "trauma/poisoning", "dental", "routine preventative health care",
    # "pregnancy/birth-related", "other", "none of the above"])
    # medical_conditions = SelectMultipleField("Please select your pre-existing medical conditions", choices=["autoimmune disorder", "cancer", 
    # "diabetes", "heart conditions", "HIV", "neurological conditions", "tuberculosis", "other", "none of the above"])
    # submit = SubmitField()

    # def validate_emergency(form, field):
    #     field.data = field.data.lower()
    #     if field.data != "y" or field.data != "yes" or field.data != "n" or field.data != "no":
    #         raise ValidationError('Invalid input')


    
    

