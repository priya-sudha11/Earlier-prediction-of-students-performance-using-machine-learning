from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pymongo import MongoClient
from django.contrib import messages
from twilio.rest import Client
import pandas as pd

client = MongoClient('mongodb+srv://admin:pswd11@cluster0.anhuqsv.mongodb.net/?retryWrites=true&w=majority')

db = client["students_db"]
mycol = db["student_records"]
dab = client["staff"]
col = dab["login"]
def home(request):
    return render(request,'home.html')

def login_view(request):
    return render(request, 'login.html')
def logredir(request):
    val1 = request.GET['email']
    val2 = request.GET['password']
    res = col.find_one({'email': val1})
    email = res['email']
    rest = col.find_one({'password': val2})
    password = rest['password']
    if (email==val1 and password==val2):
        data = list(mycol.find())
        return render(request, 'predict.html', {'data': data})
    else:
        return render(request, 'login.html')
def main(request):
    return render(request,'main.html')

def registration(request):

    val1 = request.GET['n1']
    val2 = request.GET['n2']
    val3 = request.GET['n3']
    val4 = request.GET['n4']
    rec = dab.login
    new_rec = {
        'name': val1,
        'email':val2,
        'password': val3,
        'department':val4,
    }
    rec.insert_one(new_rec)
    return render(request, 'login.html')

def predict(request):
    data = list(mycol.find())
    return render(request, 'predict.html', {'data': data})
def reg(request):
    return render(request,'reg_sec.html')
def result(request):
    return render(request,'reg_sec.html')
def send_sms(request):
    account_sid = 'AC4fd315edc67283bc123c346e1f22c26e'
    auth_token = '0e93de010772128c5529b67eafb8c9ea'
    client = Client(account_sid, auth_token)

    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        message = client.messages.create(
            body=message,
            from_='+15855751224',
            to=phone_number
        )
        data = list(mycol.find())
        return render(request, 'predict.html', {'data': data})

    return render(request, 'send_sms.html')
def predict2(request):
    return render(request,'predict2.html')

def result_2(request):

    stud_data = pd.read_csv(r'C:\Users\msiva\spp\SPP\resource\data.csv')

    a = stud_data.drop("y", axis=1)
    b = stud_data['y']

    a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.2, stratify=b, random_state=2)

    model = LogisticRegression()
    model.fit(a_train, b_train)


    val1 = request.GET['n1']
    val2 = request.GET['n2']
    val3 = request.GET['n3']
    val4 = request.GET['n4']
    val5 = request.GET['n5']
    val6 = request.GET['n6']
    val7 = request.GET['n7']
    val8 = request.GET['n8']
    val9 = request.GET['n9']
    val10 = request.GET['n10']
    val11 = request.GET['n11']
    # val12 = request.GET['n12']
    # val13 = request.GET['n13']
    # val13 = request.GET['n13'])
    new_data = pd.DataFrame([[1,val4,val5,val6,val7,val8,val9,val10,val11]], columns=stud_data.columns[:-1])
    prediction = model.predict(new_data)
    result4 = ''
    if prediction == [1]:
        result4 = "pass"
    else:
        result4 = "fail"

    rec = db.student_records
    new_rec = {
        'name': val1,
        'reg_no':val2,
        'dept': val3,
        'gpa':val4,
        'dca1':val5,
        'dca2':val6,
        'model':val7,
        'unittest1':val8,
        'unittest2':val9,
        'unittest3':val10,
        'unittest4':val11,
        'result':result4,
    }

    rec.insert_one(new_rec)
    data = list(mycol.find())
    val = mycol.find({'name': val1})
    
    return render(request,'predict.html', {'data': data})
