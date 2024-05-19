from flask import Flask, render_template, request
import numpy as np
import pickle
from flask_navigation import Navigation
import subprocess as sp


model = pickle.load(open('model.pkl', 'rb'))
datasend =['', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'NO']



app = Flask(__name__)
nav = Navigation(app)

# initializing Navigations
nav.Bar('top', [
    # nav.Item('Home', 'home'),
    nav.Item('Service', 'predictPage'),
    nav.Item('Contact US', 'contactUs'),    #name,function
    nav.Item('About Us', 'aboutUs'),
])



@app.route('/reportDisplay', methods=["POST"])   # button nx page
def reportDisplay():
    data = datasend
    emt = ['', '', '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'NO']
    if(data == emt):
        return render_template('reportDisplay.html',name=data[0],email=data[1],phone=data[2],gender=data[3],age=data[4],
                                                smoking = data[5],yellowF = data[6],anxiety = data[7],peerP = data[8],
                                                chronicD = data[9],fatigue = data[10],allegy = data[11],wheezing = data[12],alcholC = data[13],
                                                coughing = data[14],shortnessBreath = data[15],SwllowingD = data[16],
                                                chestPain = data[17],result="Report For Lung Cancer: "+data[-1])
    else:
        print(data)
        return render_template('reportDisplay.html',name=data[0],email=data[1],phone=data[2],gender=data[3],age=data[4],
                                                smoking = data[5],yellowF = data[6],anxiety = data[7],peerP = data[8],
                                                chronicD = data[9],fatigue = data[10],allegy = data[11],wheezing = data[12],alcholC = data[13],
                                                coughing = data[14],shortnessBreath = data[15],SwllowingD = data[16],
                                                chestPain = data[17],result="Report For Lung Cancer: "+data[-1])



@app.route('/contactUs')
def contactUs():
    return render_template('contactUs.html')

@app.route('/aboutUs')
def aboutUs():
    return render_template('aboutUs.html')


@app.route("/", methods=['GET','POST'])
def predictPage():
    name = ""
    email=""
    phone=""
    temp=""
    gender=0
    age=0
    smoking=0
    yellowF=0
    anxiety=0
    peerP=0
    chronicD=0
    fatigue=0
    allegy=0
    wheezing=0
    alcholC=0
    coughing=0
    shortnessBreath=0
    SwllowingD=0
    chestPain = 0

    if request.method=='POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        gender = request.form['gender']
        age = request.form['age']
        yellowF = request.form['yellowF']
        smoking = request.form['smoking']
        anxiety = request.form['anxiety']
        peerP = request.form['peerP']
        chronicD = request.form['chronicD']
        fatigue = request.form['fatigue']
        allegy = request.form['allegy']
        wheezing = request.form['wheezing']
        alcholC = request.form['alcholC']
        coughing = request.form['coughing']
        shortnessBreath = request.form['shortnessBreath']
        SwllowingD = request.form['SwllowingD']
        chestPain = request.form['chestPain']
        

    # Changing categorical to numerical values 
        if gender == "male":
            gender= 0
        else :
            gender = 1

  
        if smoking == "yes":
            smoking= 0
        else :
            smoking = 1

        if yellowF == "yes":
            yellowF= 2
        else :
            yellowF = 1

        if anxiety == "yes":
            anxiety= 2
        else :
            anxiety = 1


        if peerP == "yes":
            peerP= 2
        else :
            peerP = 1

        if chronicD == "yes":
            chronicD= 2
        else :
            chronicD = 1

        if fatigue == "yes":
            fatigue= 2
        else :
            fatigue = 1
 
        if allegy == "yes":
            allegy= 2
        else :
            allegy = 1
    
        if wheezing == "yes":
            wheezing= 2
        else :
            wheezing = 1

        if alcholC == "yes":
            alcholC= 2
        else :
            alcholC = 1
    
        if coughing == "yes":
            coughing= 2
        else :
            coughing = 1
    
        if shortnessBreath == "yes":
            shortnessBreath= 2
        else :
            shortnessBreath = 1

        if SwllowingD == "yes":
            SwllowingD= 2
        else :
            SwllowingD = 1

        if chestPain == "yes":
            chestPain= 2
        else :
            chestPain = 1


    arr = np.array([[gender, age, smoking,yellowF, anxiety, peerP, chronicD, fatigue, allegy, 
                    wheezing, alcholC, coughing, shortnessBreath, SwllowingD, chestPain]])

    pred = model.predict(arr)
    

    # Changing numerical to categorical for showing result 
    if pred == 0:
        temp = "Negatve"
    else:
        temp = "Positive"

    if(name):
        name = "Name: "+name
    
    if(email):
        email = "Email address: "+email
    
    if(phone):
        phone = "Phone No. : "+phone

    if(age):
        age = "Age : "+age

        if gender == 0:
            gender= "Gender : Male"
        else :
            gender = "Gender : Female"

        if smoking == 1:
            smoking= "Smoking : Yes"
        else :
            smoking = "Smoking : No"

        if yellowF == 2:
            yellowF= "Yellow fingers: Yes"
        else :
            yellowF = "Yellow fingers: No"

        if anxiety == 2:
            anxiety= "Anxiety : Yes"
        else :
            anxiety = "Anxiety: No"

        if peerP == 2:
            peerP= "Peer Presure : Yes"
        else :
            peerP = "Peer Presure: No"

        if chronicD == 2:
            chronicD= "Chronic Disease : Yes"
        else :
            chronicD = "Chronic Disease: No"

        if fatigue == 2:
            fatigue= "Fatigue  Yes"
        else :
            fatigue = "Fatigue : No"
 
        if allegy == 2:
            allegy= "Allegy: Yes"
        else :
            allegy = "Allegy: No"
    
        if wheezing == 2:
            wheezing= "Wheezing: Yes"
        else :
            wheezing = "Wheezing: No"

        if alcholC == 2:
            alcholC= "AlcholC : Yes"
        else :
            alcholC = "AlcholC : No"
    

        if coughing == 2:
            coughing= "Coughing: Yes"
        else :
            coughing = "Coughing : No"

        if shortnessBreath == 2:
            shortnessBreath= "Shortness Of Breath : Yes"
        else :
            shortnessBreath = "Shortness Of Breath : No"

        if SwllowingD == 2:
            SwllowingD= "Swllowing Difficulty : Yes"
        else :
            SwllowingD = "Swllowing Difficulty : No"

        if chestPain == 2:
            chestPain= " Cheat Pain: Yes"
        else :
            chestPain = "Cheat Pain : No"
    
    global datasend 
    
    datasend = [name, email,phone,gender, age, smoking,yellowF, anxiety, peerP, chronicD, fatigue, allegy, 
                    wheezing, alcholC, coughing, shortnessBreath, SwllowingD, chestPain,temp]
    print("in predict: ",datasend)
    
    return render_template('predictPage.html',var=datasend)

if __name__ == "__main__":
    app.run(debug=True, port=8000)

