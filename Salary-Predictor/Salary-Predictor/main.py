from flask import Flask, render_template, request
import sklearn
import pandas as pd
import pickle
app = Flask(__name__)
data = pd.read_csv("cleandata.csv")
data.drop(columns=["Unnamed: 0"], inplace=True)
pipe = pickle.load(open("salary.pk1", "rb"))

@app.route('/')
def index():
    locations = sorted(data["Location"].unique())
    company = sorted(data["Company Name"].unique())
    job_title = sorted(data["Job Title"].unique())
    return render_template('index.html', locations=locations, company=company, job_title=job_title)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    company = request.form.get('company')
    job_title = request.form.get('job_title')

    input = pd.DataFrame([[job_title, company, location]],columns=["Job Title","Company Name","Location"])
    prediction = pipe.predict(input)[0]
    return str(prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5001)