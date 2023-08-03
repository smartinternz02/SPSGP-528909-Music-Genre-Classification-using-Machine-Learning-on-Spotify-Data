from flask import Flask,request,render_template
import numpy as np
import joblib

app = Flask(__name__)
model=joblib.load('bagging.model')
sc = joblib.load('transform.save')

@app.route('/')
def home():
    return render_template('home.hmtl')

@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('indexnew.html')

@app.route('/Home',methods=['POST','GET'])
def my_home():
    return render_template('home.html')

@app.route('predict',methods=['POST','GET'])
def predict():
    input_feature=[float(x) for x in request.form.values()]
    x = [np.array(input_feature)]
    x = sc.transform(x)
    print(x)

    prediction=model.predict(x)
    labels = ["Dark Trap","Emo","Hiphop","Pop",'Rap',"Rnb","Trap Metal","Underground Rap","dnb","hardstyle","psytrance","techhouse","techhouse","techno","trance","trap"]

    print("Prediction is:",labels[prediction[0]])

    return render_template("resultnew.html",prediction=labels[prediciton[0]])

if __name__== "__main__":

    app.run(host="0.0.0.0", port=8000,debug=True)

