from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, DateField, SelectField, SelectMultipleField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    health_card = StringField("Please enter your 10-digit health card number")
    version_code = StringField("Please enter your health card version code")
    first_name = StringField("Please enter your first name")
    last_name = StringField("Please enter your last")
    dob = DateField("Please enter your date of birth (YYYY-MM-DD)")

    house_number = IntegerField("Please enter the house number of the address you are currently at")
    street = StringField("Please enter the street name of the address you are currently at")
    city = StringField("Please enter the name of the city of the address you are currently at")
    province = StringField("Please enter the name of the province of the address you are currently at")
    country = StringField("Please enter the name of the country of the address you are currently at")

    mobile_phone = StringField("Please enter your mobile phone number (no hypens, spaces, or parantheses)")
    home_phone = StringField("Please enter your home phone number (no hypens, spaces, or parantheses)")
    symptoms = SelectMultipleField("Please describe your symptoms (Hold down CTRL to select multiple or SHIFT to select consecutive symptoms, then press ENTER to confirm)", choices=["chronic condition", "acute illness", "trauma/poisoning", "dental", "routine preventative health care",
    "pregnancy/birth-related", "other", "none of the above"])
    medical_conditions = SelectMultipleField("Please select your pre-existing medical conditions", choices=["autoimmune disorder", "cancer", 
    "diabetes", "heart conditions", "HIV", "neurological conditions", "tuberculosis", "other", "none of the above"])
    submit = SubmitField()




    
    

