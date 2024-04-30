# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 17:29:11 2024

@author: abhib
"""
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('healthcarebill_random_forest_regression.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index_hcb.html')


standard_to = StandardScaler()
@app.route("/predictions", methods=['POST'])
def predict():
    if request.method == 'POST':
        Age = int(request.form['Age'])
        Gender = request.form['Gender']
        Gender_Male = 0
        if(Gender == 'Male'):
            Gender_Male = 1
        admited_days = int(request.form['admited_days'])
        Blood_Type = request.form['Blood_Type']
        Blood_Type_A_neg =0
        Blood_Type_AB_neg =0
        Blood_Type_AB_pos =0
        Blood_Type_B_neg =0
        Blood_Type_B_pos =0
        Blood_Type_O_neg =0
        Blood_Type_O_pos =0
        if (Blood_Type == "A-"):
            Blood_Type_A_neg =1
        elif (Blood_Type == "AB-"):           
            Blood_Type_AB_neg =1            
        elif (Blood_Type == "AB+"):
            Blood_Type_AB_pos =1
        elif (Blood_Type == "B-"):
            Blood_Type_B_neg =1
        elif (Blood_Type == "B+"):
            Blood_Type_B_pos =1
        elif (Blood_Type == "O+"):
            Blood_Type_O_pos =1
        elif (Blood_Type == "O+"):
            Blood_Type_O_neg =1

        Medical_Condition = request.form['Medical_Condition']
        Medical_Condition_Asthma = 0
        Medical_Condition_Cancer = 0
        Medical_Condition_Diabetes = 0
        Medical_Condition_Hypertension = 0
        Medical_Condition_Obesity = 0
        if (Medical_Condition == 'Asthma'):
            Medical_Condition_Asthma = 1
        elif(Medical_Condition == 'Cancer'):
            Medical_Condition_Cancer = 1
        elif(Medical_Condition == 'Diabetes'):
            Medical_Condition_Diabetes = 1
        elif(Medical_Condition_Cancer == 'Hypertesnion'):
            Medical_Condition_Hypertension = 1
        elif(Medical_Condition == 'Obesity'):
            Medical_Condition_Obesity = 1

        Insurance_Provider = request.form['Insurance_Provider']
        Insurance_Provider_Blue_Cross = 0
        Insurance_Provider_Cigna = 0
        Insurance_Provider_Medicare = 0
        Insurance_Provider_UnitedHealthcare= 0
        if(Insurance_Provider == 'Blue Cross'):
            Insurance_Provider_Blue_Cross=1
        elif(Insurance_Provider == 'Cigna'):
            Insurance_Provider_Cigna =1
        elif(Insurance_Provider == 'Medicare'):
            Insurance_Provider_Medicare =1
        elif(Insurance_Provider == 'United Health Care'):
            Insurance_Provider_UnitedHealthcare =1

        Admission_type = request.form['Admission_type']
        Admission_Type_Emergency= 0
        Admission_Type_Urgent= 0
        if(Admission_type == "Emergency"):
            Admission_Type_Emergency= 1
        elif(Admission_type == 'Urgent'):
            Admission_Type_Urgent= 1

        Medication = request.form['Medication_Type']
        Medication_Ibuprofen =0
        Medication_Lipitor = 0
        Medication_Paracetamol = 0
        Medication_Penicillin = 0
        if(Medication == 'Ibuprofen'):
            Medication_Ibuprofen =1
        elif(Medication == 'Lipitor'):
            Medication_Lipitor =1
        elif(Medication == 'Paracetamol'):
            Medication_Paracetamol =1
        elif(Medication == 'Penicillin'):
            Medication_Penicillin =1

        Test_Results = request.form['Test_Results']
        Test_Results_Inconclusive =0
        Test_Results_Normal = 0
        if(Test_Results == 'Inconclusive'):
            Test_Results_Inconclusive =1
        elif(Test_Results == 'Normal'):
            Test_Results_Normal=1

        prediction=model.predict([[Age,admited_days,Gender_Male, Blood_Type_A_neg, Blood_Type_AB_pos, Blood_Type_AB_neg,
                                   Blood_Type_B_pos, Blood_Type_B_neg, Blood_Type_O_pos,
                                   Blood_Type_O_neg, Medical_Condition_Asthma,
                                   Medical_Condition_Cancer, Medical_Condition_Diabetes,
                                   Medical_Condition_Hypertension, Medical_Condition_Obesity,
                                   Insurance_Provider_Blue_Cross, Insurance_Provider_Cigna,
                                   Insurance_Provider_Medicare, Insurance_Provider_UnitedHealthcare,
                                   Admission_Type_Emergency, Admission_Type_Urgent,
                                   Medication_Ibuprofen, Medication_Lipitor, Medication_Paracetamol,
                                   Medication_Penicillin, Test_Results_Inconclusive,
                                   Test_Results_Normal]])
        output=round(prediction[0],0)
        if output<0:
            return render_template('index_hcb.html',prediction_texts="Incorrect/Incomplete details. Please try again.")
        else:
            return render_template('index_hcb.html',prediction_text="Your expected Hostital bill under provided condition equals {} $".format(output))
    else:
        return render_template('index_hcb.html')

if __name__=="__main__":
    app.run(debug=True)



        

        


            
