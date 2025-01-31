from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import pandas as pd
import statsmodels

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin_page():
    if request.method == 'POST':
        time_frame = request.form.get('time_frame')
        start_date = request.form.get('start')
        end_date = request.form.get('end')
        if time_frame == 'daily':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='d')
            pickle_in = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/bitcoin_daily.pkl", 'rb')
            daily_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = daily_model.predict(start=start_date, end=end_date)
        elif time_frame == 'monthly':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='m')
            pickle_in = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/bitcoin_monthly.pkl", 'rb')
            monthly_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = monthly_model.predict(start=start_date, end=end_date)
            
        return render_template('bitcoin.html', check=True ,start_date=start_date, end_date=end_date, labels=dates, predictions=pred)
    
    return render_template('bitcoin.html')

@app.route('/ethereum', methods=['GET', 'POST'])    
def ethereum_page():
    if request.method == 'POST':
        time_frame = request.form.get('time_frame')
        start_date = request.form.get('start')
        end_date = request.form.get('end')
        if time_frame == 'daily':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='d')
            pickle_in = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/ethereum_daily.pkl", 'rb')
            daily_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = daily_model.predict(start=start_date, end=end_date)
        elif time_frame == 'monthly':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='m')
            pickle_in = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/ethereum_monthly.pkl", 'rb')
            monthly_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = monthly_model.predict(start=start_date, end=end_date)
            
        return render_template('ethereum.html', check=True ,start_date=start_date, end_date=end_date, labels=dates, predictions=pred)
    
    return render_template('ethereum.html')

@app.route('/DOGE', methods=['GET', 'POST'])
def DOGE_page():
    if request.method == 'POST':
        time_frame = request.form.get('time_frame')
        start_date = request.form.get('start')
        end_date = request.form.get('end')
        if time_frame == 'daily':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='d')
            pickle_in = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/DOGE_daily.pkl", 'rb')
            daily_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = daily_model.predict(start=start_date, end=end_date)
        elif time_frame == 'monthly':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='m')
            pickle_in = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/DOGE_monthly.pkl", 'rb')
            monthly_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = monthly_model.predict(start=start_date, end=end_date)

        return render_template('DOGE.html', check=True ,start_date=start_date, end_date=end_date, labels=dates, predictions=pred)

    return render_template('DOGE.html')

@app.route('/prediction', methods=['GET', 'POST'])
def prediction_page():
    if request.method == 'POST':

        time_frame = request.form.get('time_frame')
        start_date = request.form.get('start')
        end_date = request.form.get('end')

        if time_frame == 'daily':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='d')
            pickle_in =  open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/ethereum_daily.pkl", 'rb')
            daily_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = daily_model.predict(start=start_date, end=end_date)
            
            
            #bitcoin
            pickle_in1 = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/bitcoin_daily.pkl", 'rb')
            daily_model1 = pickle.load(pickle_in1)
            pickle_in1.close()
            pred1 = daily_model1.predict(start=start_date, end=end_date)

        elif time_frame == 'monthly':
            dates = pd.date_range(pd.to_datetime(start_date), pd.to_datetime(end_date), freq='m')
            pickle_in =   open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/ethereum_monthly.pkl", 'rb')
            monthly_model = pickle.load(pickle_in)
            pickle_in.close()
            pred = monthly_model.predict(start=start_date, end=end_date)

            #bitcoin
            pickle_in1 = open("C:/Users/amalb/Downloads/Cryptocurrency-Prediction-With-Sentiment-Analysis-main/models/bitcoin_monthly.pkl", 'rb')
            monthly_model1 = pickle.load(pickle_in1)
            pickle_in1.close()
            pred1 = monthly_model1.predict(start=start_date, end=end_date)
           
    
        return render_template('prediction.html',check=True ,start_date=start_date, end_date=end_date, labels=dates, predictions=pred,labels1=dates, predictions1=pred1)

    return render_template('prediction.html')

if __name__ == "__main__":
    app.run(debug=True)
