# peasy
#Project Requirement 
Prototype the following project:

Build an application where the User’s data can be shared only if they approve it.

There are 3 types of users/roles:



1.Patient/User

2.Doctor

3.Pharmacist



The Patient has medical records and prescriptions. If a doctor asks for a patient’s prescription, the patient has to approve it. 
Same goes with the Pharmacist, if the pharmacist wants to view the patient’s prescription, the patient has to approve it.

#Solution
system requirements:
 create a virtual environment and then pip install -r requirements.txt (only django is required)

Start the server by running python manage.py runserver command

#Features:
create user via /signup endpoint
assign user-type to users from django (reason users should not be allowed to pick user_type , by default user_type is patient)


#Limitations:
1. Used simple HTML and no fancy css
2. there was no functionality of medical records so have not stored medical records of user
3. user prescrition has to be set from django admin






