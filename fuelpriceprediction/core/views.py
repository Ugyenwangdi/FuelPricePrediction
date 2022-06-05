from django.shortcuts import render

# Create your views here.
import joblib
import numpy as np
import pandas as pd


model = joblib.load('model/model.pkl', "rb")


def index(request):
    return render(request,'index.html')

def predict(request):
    try:
        region = [request.POST.get('region')][0]
        product = [request.POST.get('product')][0]
        company = [request.POST.get('company')][0]
        dateinput = [request.POST.get('dateinput')][0]
        station = [request.POST.get('station')][0]
        nosrm = [request.POST.get('rminput')][0]
        
        
        if region == "" or product == "" or company == "" or dateinput == "" or station == "":
            context = {'error': 'Please fill the input fields'}
            
            print("Please fill the input fields")
            return render(request, 'index.html', context)
        
        else:
        
        # dateinput = [request.POST.get('dateinput')][0].split("-")
        
        # month = dateinput[0]
        # day = dateinput[1]
        # year = dateinput[2]
        
        
        # print(month)
        # print(day)
        # print(year)
        
    #     stations = ['Phuentsholing', 'Rinchending', 'Pasakha', 'Samtse Town', 'Sipsoo',
    #    'Gomtu', 'Gedu', 'Phuentsholing Main gate',
    #    'Gelephu Forest Checkpost', 'Sarpang', 'Gelephu Gate',
    #    'Gelephu Town', 'Dagapela', 'Tsirang', 'Zhemgang', 'Trongsa',
    #    'Bumthang', 'Dagana', 'Lhamoizingkha', 'Dangdung', 'Panbang',
    #    'Tingtibi', 'Samdrup Jongkhar', 'Wamrong', 'Trashigang',
    #    'Trashiyangtse', 'Mongar', 'Gyelposing', 'Kanglung', 'Pemagatshel',
    #    'Lhuntse', 'Jomotsangkha', 'Autsho', 'Doksum', 'Bhangtar',
    #    'Rangjung', 'Nganglam', 'Samdrup Jongkhar Gate',
    #    'Nganglam Potonala', 'Samdrup Jongkhar Upper Town', 'Chimakothi',
    #    'Lungtenzampa', 'Paro Town', 'Haa', 'Bajo Town', 'Beychu',
    #    'Khuruthang', 'Gasa', 'Motithang', 'Olakha', 'Paro NIE Bridge',
    #    'Langlitsawa', 'Wangdue Zero Point', 'Lobesa', 'Chubachu',
    #    'Paro Shaba', 'Samtse Checkpost', 'Pagli', 'Mitsina', 'Dorokha',
    #    'Langdru (Khasadrapchu)', 'Chanzamtok', 'Gomtu Phuentshopelri',
    #    'Phuentsholing Truck Parking', 'Phuentsholing Dungkhag Office',
    #    'Phuentsholing Near MDP', 'Ramtokto', 'Chamkuna LAP,Phuntsholing']
    #     print(len(stations)) # 68
        
        
        # columns = ['Region', 'Product', 'Company', 'Approved_Date', 'Station']
        # sample = [['Western Region', 'Diesel', 'Indian Oil Corporation Limited', '2021-08-16', 'Samtse Checkpost']]
        

            x = [[region, product, company, dateinput, station]]
            print(x)
            
            
            x = pd.DataFrame(x, columns=['Region', 'Product', 'Company', 'Approved_Date', 'Station'])
            
            # print(x)
            # Use the loaded model to make predictions
            prediction = model.predict(x)
            prediction = format(prediction[0], '.3f')  # format to 3 decimals

            context = {'result': prediction, 'input': x}
            return render(request,'result.html',context)
        
    except:
        context = {'error': 'Something went wrong. Please try again by filling the input fields'}
        return render(request, 'index.html', context)

    # return render(request,'result.html',context)