from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    health_card = IntegerField("Please enter your health card number", validators=[DataRequired(), Length(min = 10, max = 10)])
    version_code = StringField("Version code", validators=[DataRequired(), Length(min = 2, max = 2)])
    first_name = StringField("Please enter your first name", validators=[DataRequired(), Length(min = 2, max = 20)])
    last_name = StringField("Please enter your last", validators=[DataRequired(), Length(min = 2, max = 20)])
    dob = DateField("Please enter your date of birth (YYYY-MM-DD)", validators=[DataRequired(), Length(min = 2, max = 8)])

    house_number = IntegerField("Please enter the house number of the address you are currently at", validators=[DataRequired(), Length(max = 4)])
    street = StringField("Please enter the street name of the address you are currently at", validators=[DataRequired()])
    city = StringField("Please enter the name of the city of the address you are currently at", validators=[DataRequired()])
    province = StringField("Please enter the name of the province of the address you are currently at", validators=[DataRequired(), Length(min = 2, max = 8)])
    country = StringField("Please enter the name of the country of the address you are currently at", validators=[DataRequired()])

    mobile_phone = IntegerField("Please enter your mobile phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    home_phone = IntegerField("Please enter your home phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
    symptoms = SelectMultipleField("Please describe your symptoms (Hold down CTRL to select multiple or SHIFT to select consecutive symptoms, then press ENTER to confirm)", choices=["chronic condition", "acute illness", "trauma/poisoning", "dental", "routine preventative health care",
    "pregnancy/birth-related", "other", "none of the above"])
    medical_conditions = SelectMultipleField("Please select your pre-existing medical conditions", choices=["autoimmune disorder", "cancer", 
    "diabetes", "heart conditions", "HIV", "neurological conditions", "tuberculosis", "other", "none of the above"])
    submit = SubmitField()

# class Emergency(FlaskForm):
#     emergency = StringField("Is this a life-threatening emergency?", validators=[DataRequired(), Length(max = 3)])
#     submit = SubmitField()

#     # def validate_emergency(form, field):
#     #     field.data = field.data.lower()
#     #     if field.data != "y" or field.data != "yes" or field.data != "n" or field.data != "no":
#     #         raise ValidationError('Invalid input')

# class HealthCard(FlaskForm):
#     healthcard = StringField("Please enter your health card number", validators=[DataRequired(), Length(min = 10, max = 10)])
#     # healthcard = StringField("Please enter your health card number")
#     submit = SubmitField()

# class VersionCode(FlaskForm):
#     version_code = StringField("Version code", validators=[DataRequired(), Length(min = 2, max = 2)])
#     submit = SubmitField()

# class Names(FlaskForm):
#     first_name = StringField("Please enter your first name", validators=[DataRequired(), Length(min = 2, max = 20)])
#     last_name = StringField("Please enter your last", validators=[DataRequired(), Length(min = 2, max = 20)])
#     submit = SubmitField()

# class DOB(FlaskForm):
#     dob = DateField("Please enter your date of birth (YY-MM-DD)", validators=[DataRequired(), Length(min = 2, max = 8)])
#     submit = SubmitField()

# class PhoneNumber(FlaskForm):
#     mobile_phone = IntegerField("Please enter your mobile phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
#     home_phone = IntegerField("Please enter your home phone number (no hypens, spaces, or parantheses)", validators=[DataRequired(), Length(min = 10, max = 10)])
#     submit = SubmitField()

# class Symptoms(FlaskForm):
#     symptoms = SelectMultipleField("Please describe your symptoms", choices=["chronic condition", "acute illness", "trauma/poisoning", "dental", "routine preventative health care",
#     "pregnancy/birth-related", "other", "none of the above"])
#     submit = SubmitField()

# class MedicalConditions(FlaskForm):
#     medical_conditions = SelectMultipleField("Please select your pre-existing medical conditions", choices=["autoimmune disorder", "cancer", 
#     "diabetes", "heart conditions", "HIV", "neurological conditions", "tuberculosis", "other", "none of the above"])
#     submit = SubmitField()


    
    

