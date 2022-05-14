from flask import Flask, render_template, url_for, flash, redirect
from form import RegistrationForm
from flask_sqlalchemy import SQLAlchemy
#import the SQL database
from datetime import datetime

app = Flask(__name__) #do not touch!

app.config['SECRET_KEY'] = "b272d0b5e8ddc9e3ff92e6853766147c" #used to protect against modifying cookies! MUST HAVE!
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db" #creates a new file of site.db
db = SQLAlchemy(app)

class Patient(db.Model):
    healthcard = db.Column(db.Integer, primary_key=True, unique=True, nullable=False) # THIS IS THE HEALTH CARD NUMBER
    # version_code = db.Column(db.String(2), nullable=False)
    # first_name = db.Column(db.String(20), unique=False, nullable=False)
    # last_name = db.Column(db.String(20), unique=False, nullable=False)
    # dob = db.Column(db.DateTime, nullable=False)
    # home_phone = db.Column(db.Integer, nullable=False)
    # mobile_phone = db.Column(db.Integer, nullable=False)
    symptoms = db.relationship('Symptom', backref="patient", lazy = True) #will be a list, links to Symptom class
    medical_conditions = db.relationship('MedCon', backref="patient", lazy = True)

    def __repr__(self):
        return f"Patient('{self.healthcard}', '{self.symptoms}')"

class Symptom(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique = True)
    symptom = db.Column(db.String(100), nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.healthcard"), nullable = False)

    def __repr__(self):
        return f"Symptom('{self.symptom}', '{self.patient_id}')"

class MedCon(db.Model):
    id = db.Column(db.Integer(), primary_key = True, unique = True)
    medcon = db.Column(db.String(100), nullable = False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.healthcard"), nullable = False)

    def __repr__(self):
        return f"MedCon('{self.medcon}', '{self.patient_id}')"

@app.route("/", methods=['GET','POST']) #creates a new home page and functions underneath run on this page unless it encounters another route method (i think)
@app.route("/home", methods=['GET','POST'])
def home():
    form = RegistrationForm()
    return render_template("home.html", form = form)

if __name__ == '__main__': #allows us to run the file using only "python filename.py"
    app.run(debug=True)


#class Symptoms(db.Model):
    #chronic_cond = db.Column(db.Boolean, nullable = True)
    #acute_illness = db.Column(db.Boolean, nullable = True)
    #trauma_poisoning = db.Column(db.Boolean, nullable = True)
    #dental = db.Column(db.Boolean, nullable = True)
    #rphc = db.Column(db.Boolean, nullable = True)
    #preg = db.Column(db.Boolean, nullable = True)
    #other = db.Column(db.Boolean, nullable = True)
    #none = db.Column(db.Boolean, nullable = True)

#class MedCon(db.Model):
    #auto_immune = db.Column(db.Boolean, nullable = True)
    #cancer = db.Column(db.Boolean, nullable = True)
    #diabetes = db.Column(db.Boolean, nullable = True)
    #heart_cond = db.Column(db.Boolean, nullable = True)
    #hiv = db.Column(db.Boolean, nullable = True)
    #neur = db.Column(db.Boolean, nullable = True)
    #tuber = db.Column(db.Boolean, nullable = True)
    #other = db.Column(db.Boolean, nullable = True)
    #none = db.Column(db.Boolean, nullable = True)