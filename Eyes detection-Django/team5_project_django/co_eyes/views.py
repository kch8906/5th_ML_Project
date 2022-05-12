
from .models import Predictlabel, Temp
from django.shortcuts import redirect, render
import joblib
from django.db.models import Sum, Count,Max
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def predict(request):
    object_name = Temp.objects.last()
    temp = object_name.temperature
    humid = object_name.humidity
    co2 = object_name.co2

    temp = float(temp)
    humid = float(humid)
    co2 = float(co2)

    day_list = Predictlabel.objects.values(
        'register_date__day'
    ).annotate(daily_total=Sum('total_sleep_count'))

    estimator = joblib.load(r'C:\jupyter_home\Machine_Learning\ML_Project_5th\5th_ML_Project\Eyes detection-Django\team5_project_django\static\ml_model\temp_lightgbm.pkl')

    x_test = [[temp, humid, co2]]

    y_predict = estimator.predict(x_test)
    y_pred_proba = np.floor(estimator.predict_proba(x_test)[:, 1] * 100)

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

    plt.savefig('C:/jupyter_home/Machine_Learning/ML_Project_5th/5th_ML_Project/Eyes detection-Django/team5_project_django/static/img/graph.png')

    return render(request, 'main.html', {'y_predict': y_pred_proba, 'temp': temp, 'co2' : co2, 'humid' : humid})