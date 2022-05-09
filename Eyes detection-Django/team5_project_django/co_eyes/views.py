from .models import Predictlabel, Temp
from django.shortcuts import redirect, render
import joblib
import numpy as np



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
    return render(request, 'main.html', {'y_predict': y_pred_proba})