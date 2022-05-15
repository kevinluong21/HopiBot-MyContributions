#the database file must be wiped before using and then created again in the terminal!

from flask import Flask, render_template, url_for, flash, redirect, request
from form import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = "b272d0b5e8ddc9e3ff92e6853766147c" #used to protect against modifying cookies! MUST HAVE!
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db" #creates a new file of site.db
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Patient table for database
class Patient(db.Model):
    id =  db.Column(db.Integer, primary_key = True, unique = True)
    healthcard = db.Column(db.String, unique=True) # health card number and version code will be concatenated
    first_name = db.Column(db.String(20), unique=False)
    last_name = db.Column(db.String(20), unique=False)
    dob = db.Column(db.DateTime)
    address = db.Column(db.String) #address will be concatenated
    home_phone = db.Column(db.Integer)
    mobile_phone = db.Column(db.Integer)
    symptoms = db.relationship('Symptom', backref="patient", lazy = True) #will be a list, links to Symptom class
    medical_conditions = db.relationship('MedCon', backref="patient", lazy = True)

    def __repr__(self):
        return f"Patient('{self.healthcard}', '{self.first_name}', '{self.last_name}', '{self.dob}', '{self.address}', '{self.home_phone}', '{self.mobile_phone}', '{self.symptoms}', '{self.medical_conditions}')"

#Symptom table for database
class Symptom(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique = True)
    symptom = db.Column(db.String(100), nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.healthcard"), nullable = False) #using health card as foreign key

    def __repr__(self):
        return f"Symptom('{self.symptom}', '{self.patient_id}')"

#Medical Conditions table for database
class MedCon(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique = True)
    medcon = db.Column(db.String(100), nullable = False)
    patient_id = db.Column(db.String, db.ForeignKey("patient.healthcard"), nullable = False) #using health card as foreign key

    def __repr__(self):
        return f"MedCon('{self.medcon}', '{self.patient_id}')"


@app.route("/", methods=['GET','POST']) #creates a new home page and functions underneath run on this page unless it encounters another route method (i think)
@app.route("/home", methods=['GET','POST'])
def home():
    form = RegistrationForm()

    if form.validate_on_submit():
        health_card = form.health_card.data.strip()
        health_card = health_card + form.version_code.data.strip().upper()

        first_name = form.first_name.data.strip().upper()
        last_name = form.last_name.data.strip().upper()

        dob = form.dob.data

        address = str(form.house_number.data) + " " + form.street.data.strip().upper() + ", " + form.city.data.strip().upper() + ", " + form.province.data.strip().upper() + ", " + form.country.data.strip().upper()

        home_phone = "1" + form.home_phone.data.strip()
        home_phone = int(home_phone)

        mobile_phone = "1" + form.mobile_phone.data.strip()
        mobile_phone = int(mobile_phone)


        patient = Patient(healthcard = health_card, first_name = first_name, last_name = last_name, dob = dob, address = address, home_phone = home_phone, mobile_phone = mobile_phone)
        db.session.add(patient)
        db.session.commit()

        for s in form.symptoms.data:
            symptom = Symptom(symptom = s, patient_id = patient.healthcard)
            db.session.add(symptom)
            db.session.commit()

        for m in form.medical_conditions.data:
            medcon = MedCon(medcon = m, patient_id = patient.healthcard)
            db.session.add(medcon)
            db.session.commit()

        return redirect(url_for("landing"))

    return render_template("home.html", form = form)

@app.route("/landing")
def landing():
    return render_template("landing.html")

@app.route("/display")
def display_all():
    patients = Patient.query.all()
    return render_template("display.html", patients=patients)

if __name__ == '__main__': #allows us to run the file using only "python filename.py"
    app.run(debug=True)
