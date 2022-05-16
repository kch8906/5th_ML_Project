from .models import Predictlabel, Temp
from django.shortcuts import render
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from time import localtime, strftime
from sklearn.preprocessing import StandardScaler




def predict(request):
    object_name = Temp.objects.last()
    temp = object_name.temperature
    humid = object_name.humidity
    co2 = object_name.co2

    temp = float(temp)
    humid = float(humid)
    co2 = float(co2)

    df = pd.read_csv(
        '/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/csv/temp.csv')
    x = df.drop('label', axis=1, inplace=False)

    estimator = joblib.load(
        r'/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/ml_model/Temp_LinearRegression.pkl')

    x_test = [[temp, humid, co2]]
    scaler = StandardScaler()
    test_scaled = scaler.fit(x).transform(x_test)
    test_pred2 = estimator.predict(test_scaled)
    y_pred_proba = np.floor(estimator.predict_proba(test_scaled)[:, 0] * 100)

    df = pd.DataFrame(list(Predictlabel.objects.all().values()))

    df['day'] = df['register_date'].dt.day
    df = df.groupby('day').max()
    df = df.reset_index()
    df['year'] = df['register_date'].dt.strftime('%Y-%m-%d')


    plt.figure(figsize=(10, 5), facecolor='white', edgecolor='white')
    plt.grid(True)

    sns.lineplot(df['year'], df['total_sleep_count'], color='white', marker='o')
    plt.fill_between(df['year'], df['total_sleep_count'], color='white', alpha=0.5)
    plt.xticks(df['year'], color='white')
    plt.yticks(df['total_sleep_count'], color='white')
    plt.xlabel('Date', color='white', loc='right', labelpad=10, fontsize=15)
    plt.ylabel('Sleep_count', color='white', loc='top', labelpad=10, fontsize=15)
    # plt.title('졸음 횟수', fontsize=16, color='white')

    plt.savefig('/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/img/graph.png', transparent=True, bbox_inches='tight')

    return render(request, 'main.html', {'y_predict': y_pred_proba, 'temp': temp, 'co2': co2, 'humid': humid})
