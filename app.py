from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_mysqldb import MySQL
import yaml
from flask_user import roles_required
import hashlib
import datetime
import json
import pickle
import numpy as np
import requests

app = Flask(__name__)
db = yaml.load(open('db.yaml'))
# Load the model
model = pickle.load(open('model.pkl','rb'))
app.secret_key = '3242353645646'





@app.route('/')
def login():
    return render_template('login.html')

model = pickle.load(open('model.pkl','rb'))

@app.route('/api',methods=['POST'])
def predict():
    #return request.json['name']
	# Get the data from the POST request.
    data = request.get_json(force=True)
    #return data
    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([[np.array(data['exp'])]])
    # Take the first value of prediction
    output = prediction[0]
    return jsonify(output)

@app.route('/request',methods=['POST'])
def hello_world():
   import requests
   rahul = request.form['Name']
   rahul1 = json.loads(rahul)

   url = 'http://localhost:5000/api'
   exp = 1
   r = requests.post(url,json={'exp':rahul1,})
   flash("Salary must be around "+str(r.json()))

   return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('modle.html', now=datetime.datetime.now())
    else:
        return redirect(url_for('login'))




@app.route('/login-check', methods = ['POST'])
def checkLogin():
    if request.method == 'POST':
        email = str(request.form['email'])
        password = str(request.form['password'])
        if request.method == 'POST':
            if request.form['email'] != 'rahul.pant@adaan.com' or request.form['password'] != 'rahul2336':
                flash("Invalid Credentials")
                return redirect(url_for('login'))
            else:
                data = ('Rahul',request.form['email'],request.form['password'],1)
                session['username'] = data
                return redirect(url_for('dashboard'))




@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")




if __name__ == "__main__":
    app.run(debug=True)
