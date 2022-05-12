from .models import Predictlabel, Temp
from django.shortcuts import redirect, render
import joblib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns



# Create your views here.
# def co_eyes(request):
#     class_object = Temp.objects.last()
#     return render(request, "main.html", {'class_object': class_object})

'''
def predict(request):
    object_name = Temp.objects.last()
    temp = object_name.temperature
    humid = object_name.humidity

    temp = float(temp)
    humid = float(humid)
    co2 = 1000

    estimator = joblib.load(r'C:\jupyter_home\Machine_Learning\ML_Project_5th\5th_ML_Project\Eyes detection-Django\team5_project_django\static\ml_model\temp_lightgbm.pkl')

    x_test = [[temp, humid, co2]]

    y_predict = estimator.predict(x_test)
    y_pred_proba = np.floor(estimator.predict_proba(x_test)[:, 1] * 100)

    df = pd.DataFrame(list(Predictlabel.objects.all().values()))
    df['register_date'] = df['register_date'].dt.day
    df = df.groupby('register_date').max()

    plt.plot(df.index, df['total_sleep_count'])
    plt.xticks(df.index)
    plt.xlabel('Date')
    plt.ylabel('Sleep_count')
    plt.legend()

    plt.savefig(
        'C:/jupyter_home/Machine_Learning/ML_Project_5th/5th_ML_Project/Eyes detection-Django/team5_project_django/static/img/graph.png')

    return render(request, 'main.html', {'y_predict': y_pred_proba})
'''

def predict(request):
    object_name = Temp.objects.last()
    temp = object_name.temperature
    humid = object_name.humidity

    temp = float(temp)
    humid = float(humid)
    co2 = 1000

    estimator = joblib.load(r'C:\jupyter_home\Machine_Learning\ML_Project_5th\5th_ML_Project\Eyes detection-Django\team5_project_django\static\ml_model\temp_lightgbm.pkl')

    x_test = [[temp, humid, co2]]

    y_predict = estimator.predict(x_test)
    y_pred_proba = np.floor(estimator.predict_proba(x_test)[:, 1] * 100)

    df = pd.DataFrame(list(Predictlabel.objects.all().values()))
    df['register_date'] = df['register_date'].dt.day
    df = df.groupby('register_date').max()

    #sns.lineplot(data=df)
    plt.plot(df.index, df['total_sleep_count'])
    plt.xticks(df.index)
    plt.xlabel('Date')
    plt.ylabel('Sleep_count')
    plt.legend()

    plt.savefig(
        'C:/jupyter_home/Machine_Learning/ML_Project_5th/5th_ML_Project/Eyes detection-Django/team5_project_django/static/img/graph.png')


    return render(request, 'main.html', {'y_predict': y_pred_proba})