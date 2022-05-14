from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    is_emergency = StringField("Is this a life-threatening emergency?", validators=[DataRequired(), Length(min = 1, max = 3)])
    submitEmergency = SubmitField();
    health_card = IntegerField("Please enter your health card number", validators=[DataRequired(), Length(min = 10, max = 10)])
    version_code = StringField("Version code", validators=[DataRequired(), Length(min = 2, max = 2)])
    first_name = StringField("Please enter your first name", validators=[DataRequired(), Length(min = 2, max = 20)])
    last_name = StringField("Please enter your last", validators=[DataRequired(), Length(min = 2, max = 20)])
    dob = DateField("Please enter your date of birth (YY-MM-DD)", validators=[DataRequired(), Length(min = 2, max = 8)])
    mobile_phone = IntegerField("Please enter your mobile phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    home_phone = IntegerField("Please enter your home phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    symptoms = SelectMultipleField("Please describe your symptoms", choices=["chronic condition", "acute illness", "trauma/poisoning", "dental", "routine preventative health care",
    "pregnancy/birth-related", "other", "none of the above"])
    medical_conditions = SelectMultipleField("Please select your pre-existing medical conditions", choices=["autoimmune disorder", "cancer", 
    "diabetes", "heart conditions", "HIV", "neurological conditions", "tuberculosis", "other", "none of the above"])

    def validate_is_emergency(form, field):
        field = field.lower()
        if field == "y" or field == "yes":
            print("no")
        elif field == "n" or field == "no":
            print("hi")
        else:
            raise ValidationError('Invalid input')

    


    
    

