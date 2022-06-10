from django.shortcuts import render

# Create your views here.
import joblib
import numpy as np
import pandas as pd


from plotly.offline import plot
import plotly.graph_objects as go

# import pyttsx3

prediction = 0

# engine = pyttsx3.init()  
# voices = engine.getProperty('voices')  # Get all the voices
# engine.setProperty('voice', voices[1].id)  # set it to second voice
# engine.say('Welcome! Predict the fuel prices of Bhutan. Fill the inputs fields and click on the predict button.')  # ask it to say the command
# engine.runAndWait()
# engine.stop()

model = joblib.load('model/model.pkl', "rb")


def home(request):
    
    return render(request,'index.html')

def predict(request):
    try:
        region = [request.POST.get('region')][0]
        product = [request.POST.get('product')][0]
        company = [request.POST.get('company')][0]
        dateinput = [request.POST.get('dateinput')][0]
        station = [request.POST.get('station')][0]
        nosrm = [request.POST.get('rminput')][0]
        
        # engine = pyttsx3.init()  
        # voices = engine.getProperty('voices')  # Get all the voices
        # engine.setProperty('voice', voices[1].id)  # set it to second voice
        # engine.say('Predicting the price on your input.')  # ask it to say the command
        # engine.runAndWait()
        # engine.stop()
        
        
        if region == "" or product == "" or company == "" or dateinput == "" or station == "":
            context = {'error': 'Please fill the input fields'}
            
            # print("Please fill the input fields")
            # engine = pyttsx3.init()  
            # voices = engine.getProperty('voices')  # Get all the voices
            # engine.setProperty('voice', voices[1].id)  # set it to second voice
            # engine.say('Please fill the input fields.')  # ask it to say the command
            # engine.runAndWait()
            # engine.stop()
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
            
           
            
            
            
            # return render(request,'result.html',context)
        
    except:
        # context = {'error': 'Something went wrong. Please try again by filling the input fields'}
        # engine = pyttsx3.init()  
        # voices = engine.getProperty('voices')  # Get all the voices
        # engine.setProperty('voice', voices[1].id)  # set it to second voice
        # engine.say('Something went wrong. Please try again by giving the correct inputs. ') # ask it to say the command
        # engine.runAndWait()
        # engine.stop()
        return render(request, 'index.html', context)

    # engine = pyttsx3.init()  
    # voices = engine.getProperty('voices')  # Get all the voices
    # engine.setProperty('voice', voices[1].id)  # set it to second voice
    # engine.say('Showing the predicted price... ') # ask it to say the command
    # engine.runAndWait()
    # engine.stop()
    
    return render(request,'index.html',context)


def dashboard(request):
    # def scatter():
    #     x1 = [1,2,3,4]
    #     y1 = [30, 35, 25, 45]

    #     trace = go.Scatter(
    #         x = x1,
    #         y = y1
    #     )
    #     layout = dict(
    #         title='Simple Graph',
    #         xaxis=dict(range=[min(x1), max(x1)]),
    #         yaxis = dict(range=[min(y1), max(y1)])
    #     )

    #     fig = go.Figure(data=[trace], layout=layout)
    #     plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    #     return plot_div

    # context ={
    #     'plot1': scatter()
    # }

    return render(request, 'core/welcome.html')


def bar(request):
    

    return render(request, 'core/barchart.html')

def pie(request):
    

    return render(request, 'core/piechart.html')


def line(request):    

    return render(request, 'core/linechart.html')


def box(request):    

    return render(request, 'core/boxplot.html')


