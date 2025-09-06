from flask import Flask,render_template,redirect,url_for,request
from sklearn.ensemble import StackingClassifier
import numpy as np
import joblib
app = Flask(__name__)
import joblib
import numpy as np

import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    port=3306,          
    user='root',        
    passwd='',          
    database='Anxiety'  
)

mycur = mydb.cursor()




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/registration',methods=['POST','GET'])
def registration():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        
        
        if password == confirmpassword:
            # Check if user already exists
            sql = 'SELECT * FROM users WHERE email = %s'
            val = (email,)
            mycur.execute(sql, val)
            data = mycur.fetchone()  # Use fetchone to check if user exists
            
            if data is not None:
                msg = 'User already registered!'
                return render_template('registration.html', msg=msg)
            else:
                # Insert new user
                sql = 'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)'
                val = (name, email, password)
                mycur.execute(sql, val)
                mydb.commit()
                msg = 'User registered successfully!'
                return render_template('login.html', msg=msg)
        else:
            msg = 'Passwords do not match!'
            return render_template('registration.html', msg=msg)
    
    return render_template('registration.html')


@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        sql = 'SELECT * FROM users WHERE email=%s'
        val = (email,)
        mycur.execute(sql, val)
        data = mycur.fetchall()
        
        if data:
            if password == data[0][2]:
                return render_template('prediction.html')
            else:
                msg = 'Password does not match!'
                return render_template('login.html', msg=msg)
        else:
            msg = 'User with this email does not exist. Please register.'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')
    


@app.route('/prediction',methods=['POST','GET'])
def prediction():
    if request.method == 'POST':								
        GAD1 = int(request.form['GAD1'])
        GAD2 = int(request.form['GAD2'])
        GAD3 = int(request.form['GAD3'])
        GAD4 = int(request.form['GAD4'])
        GAD5 = int(request.form['GAD5'])
        GAD6 = int(request.form['GAD6'])
        GAD7 = int(request.form['GAD7'])
        SWL1 = int(request.form['SWL1'])
        SWL2 = int(request.form['SWL2'])
        SWL3 = int(request.form['SWL3'])
        SWL4 = int(request.form['SWL4'])
        SWL5 = int(request.form['SWL5'])
        Game = int(request.form['Game'])
        Hours = float(request.form['Hours'])
        Gender = int(request.form['Gender'])
        Age = int(request.form['Age'])
        Work = int(request.form['Work'])
        Degree = int(request.form['Degree'])
        GAD_T = int(request.form['GAD_T'])
        SWL_T = int(request.form['SWL_T'])
        abc = [[GAD1,GAD2,GAD3,GAD4,GAD5,GAD6,GAD7,SWL1,SWL2,SWL3,SWL4,SWL5,Game,Hours,Gender,Age,Work,Degree,GAD_T,SWL_T]]
        # Convert abc to numpy array for model prediction
        abc_array = np.array(abc)
            # Load the model
        loaded_model = joblib.load('stacking_model.pkl')
        # Predict the output using the loaded model
        result = loaded_model.predict(abc_array)
        if result == 0:
            msg= "Extremely difficult"
        elif result == 1:
            msg= "Not difficult at all"
        elif result == 2:
            msg= "Somewhat difficult"
        elif result == 3:
            msg= "Very difficult"
        else:
            msg= result  
        return render_template('prediction.html',msg = msg)
    return render_template('prediction.html')

@app.route('/logout')
def logout():
    return render_template('index.html')
    






if __name__ == '__main__':
    app.run(debug = True)