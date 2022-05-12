from .models import Predictlabel, Temp
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import F, Func, Value, CharField
from datetime import datetime
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Create your views here.
# def co_eyes(request):
#     class_object = Temp.objects.last()
#     return render(request, "main.html", {'class_object': class_object})

def predict(request):
    object_name = Temp.objects.last()
    temp = object_name.temperature
    humid = object_name.humidity

    temp = float(temp)
    humid = float(humid)
    co2 = 1000

    estimator = joblib.load(r'/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/ml_model/temp_lightgbm.pkl')

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

    plt.savefig('/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/imgs/graph.png')

    return render(request, 'main.html', {'y_predict': y_pred_proba})


# def graph(request):
#     df = pd.DataFrame(list(Predictlabel.objects.all().values()))
#     df['register_date'] = df['register_date'].dt.day
#     df = df.groupby('register_date').max()
#
#     plt.plot(df.index, df['total_sleep_count'])
#     plt.xticks(df.index)
#     plt.xlabel('Date')
#     plt.ylabel('Sleep_count')
#     plt.legend()
#
#     plt.savefig('/home/crysis/Workspace/5th_ML_Project/Eyes detection-Django/team5_project_django/static/imgs/graph.png')
#
#
#     return render(request, 'main.html')







