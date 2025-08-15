

from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib


filename = 'nlp_crime_model_test.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('new 1.html')

@app.route('/predict',methods=['POST'])
def predict():
   if request.method == 'POST':
       message = request.form['message']
       data = [message]
       vect = cv.transform(data).toarray()
       my_prediction = clf.predict(vect)
   return render_template('predict.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)