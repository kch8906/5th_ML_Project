from .models import Predictlabel, Temp
from django.shortcuts import redirect, render
import joblib
from django.db.models import Sum, Count,Max
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create your views here.
# def co_eyes(request):
#     class_object = Temp.objects.last()
#     return render(request, "main.html", {'class_object': class_object})


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

    estimator = joblib.load(r'C:\jupyter_home\Machine_Learning\5th_ML_Project\Eyes detection-Django\team5_project_django\static\ml_model\temp_lightgbm.pkl')

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

    plt.savefig('C:/jupyter_home/Machine_Learning/5th_ML_Project/Eyes detection-Django/team5_project_django/static/img/graph.png')

    # if y_pred_proba >= 70 :
    #     comment = '졸릴 확률이 높습니다. 환기를 시켜주세요'
    # else:
    #     comment = '안전한 운전 하십시요'

    return render(request, 'main.html', {'y_predict': y_pred_proba, 'temp': temp, 'co2' : co2, 'humid' : humid})


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
#     plt.savefig('C:/jupyter_home/Machine_Learning/5th_ML_Project/Eyes detection-Django/team5_project_django/static/img/graph.png')
#
#     return render(request, 'main.html')


# def count_sleep(request):
#     day_list = Predictlabel.values(
#         'label'
#     ).annotate(daily_total=Sum('register_date'))


# def predict(request):
#     class_all = Predictlabel.objects.all()
#     return render(request, 'main.html', {'y_predict': class_all})
