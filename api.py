from flask import Flask, escape, make_response, request, jsonify
import numpy as np
import pickle
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return 'Hello'
	
@app.route('/predict',methods=['GET', 'POST'])
def predict():
    
     if request.method == 'GET':
            return make_response('failure')
     if request.method == 'POST':
        criticiteCID = request.json['criticiteCID']
        criticiteBUSINESS = request.json['criticiteBUSINESS']
	    
        prediction =model.predict(np.array([criticiteCID,criticiteBUSINESS]).reshape(-1, 1) )
        return str (prediction[0]) 

if __name__ == "__main__":
    app.run(debug=True)		