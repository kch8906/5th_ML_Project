from .models import Predictlabel, Temp
from django.shortcuts import redirect, render
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def predict(request):
    object_name = Temp.objects.last()
    temp = object_name.temperature
    humid = object_name.humidity
    co2 = object_name.co2

    temp = float(temp)
    humid = float(humid)
    co2 = float(co2)

    df = pd.read_csv('/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/csv/temp.csv')
    x = df.drop('label', axis=1, inplace=False)


    estimator = joblib.load(r'/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/ml_model/Temp_LinearRegression.pkl')

    x_test = [[temp, humid, co2]]
    scaler = StandardScaler()
    test_scaled = scaler.fit(x).transform(x_test)
    test_pred2 = estimator.predict(test_scaled)
    y_pred_proba = np.floor(estimator.predict_proba(test_scaled)[:, 0] * 100)



    df = pd.DataFrame(list(Predictlabel.objects.all().values()))
    df['register_date'] = df['register_date'].dt.day
    df = df.groupby('register_date').max()

    plt.grid(True)
    sns.lineplot(df.index,df['total_sleep_count'],color='slateblue', marker='o')
    plt.fill_between(df.index,df['total_sleep_count'],color='lightpink', alpha=0.4)
    plt.xticks(df.index)
    plt.yticks(df['total_sleep_count'])
    plt.xlabel('Date')
    plt.ylabel('Sleep_count')
    plt.title('Number of drowsy driving',fontsize=16)

    plt.savefig('/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/img')

    return render(request, 'main.html', {'y_predict': y_pred_proba, 'temp': temp, 'co2': co2, 'humid':  humid})