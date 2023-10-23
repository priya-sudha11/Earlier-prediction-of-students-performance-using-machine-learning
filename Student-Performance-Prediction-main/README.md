# Student Performance Prediction using Django, Twilio and MongoDB

This project aims to predict the performance of students using machine learning techniques, with a web-based interface built using the Django framework. The project also utilizes Twilio for sending SMS notifications to parents or guardians about their child's performance.
***
**Technologies Used**
***
The project uses the following technologies:

Python 

Django

Djongo (for MongoDB integration)

Scikit-learn (for machine learning)

Twilio API (for SMS notifications)


**Installation**
***

To run this project, you need to have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/


Once you have Python installed, follow these steps to set up the project:

Clone the repository to your local machine.


git clone https://github.com/SivasuriyanM/Student-Performance-Prediction.git

Change to the project directory.


cd Student-Performance-Prediction

Install the project dependencies using pip.


pip install -r requirements.txt

Create a file named .env in the project directory with the following contents:

makefile

Copy code

TWILIO_ACCOUNT_SID=<your-twilio-account-sid>

TWILIO_AUTH_TOKEN=<your-twilio-auth-token>

TWILIO_PHONE_NUMBER=<your-twilio-phone-number>


Replace the placeholders with your actual Twilio account SID, auth token and phone number.


**Start the Django development server.**
***

Copy code

python manage.py runserver

Open your web browser and navigate to http://localhost:8000 to access the project.

**Usage**
***
To use the project, follow these steps:

Enter the student's information in the input fields provided.

Click on the "Predict" button to generate a performance prediction based on the provided information.

If the student's performance is below a certain threshold, an SMS notification will be sent to the phone number specified in the .env file.


**License**
***

This project is licensed under the MIT License. You can view the license file here.



