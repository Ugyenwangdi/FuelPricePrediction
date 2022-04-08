from django.shortcuts import render

# Create your views here.
import joblib
import numpy as np


model_from_joblib = joblib.load('model/houseprice.pkl')


def index(request):
    return render(request,'index.html')

def predict(request):
    try:
        nosrm = [request.POST.get('rminput')]
        # print(nosrm)
        # print(type(nosrm))                  #get the sentence 
        x = np.array([nosrm], dtype=float).reshape(-1,1)  #convert the number of rooms to float

        # Use the loaded model to make predictions
        prediction = model_from_joblib.predict(x)
        prediction = format(prediction[0], '.3f')  # format to 3 decimals

        context = {'result': prediction, 'rooms': x}
    except:
        context = {'error': 'Please enter the number of rooms'}
        return render(request, 'index.html', context)

    return render(request,'result.html',context)