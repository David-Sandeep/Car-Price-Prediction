from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)

url ='https://drive.google.com/file/d/1adq9EUFi-kUqg-KYa5hT7ZgrpLK6paWn/view?usp=drivesdk'





def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)



file_id = '1adq9EUFi-kUqg-KYa5hT7ZgrpLK6paWn'
destination = 'random_forest_regression_model.pkl'
download_file_from_google_drive(file_id, destination)














model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Kilometers_Driven = int(request.form['Kilometers_Driven'])
        Mileage = int(request.form['Mileage'])
        Engine=int(request.form['Engine'])
        Power=int(request.form['Power'])
        Seats=int(request.form['Seats'])
        how_old=int(request.form['how_old'])


        
       
        Fuel_Type=request.form['Fuel_Type']
        if(Fuel_Type=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        elif(Fuel_Type=='Diesel'):
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=0
            
        	
        Transmission_type=request.form['Transmission_type']
        if(Transmission_type=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
            
        Owner_type=request.form['Owner_type']
        
        if(Owner_type=='Second'):
                Owner_Type_Second=1
                Owner_Type_Third=0
        elif(Owner_type=='Third'):
            Owner_Type_Second=0
            Owner_Type_Third=1
        else:
            Owner_Type_Second=0
            Owner_Type_Third=0
            
        fs=[Kilometers_Driven, Mileage, Engine,Power, Seats, how_old,
       Fuel_Type_Petrol, Transmission_Manual, Owner_Type_Second,
       Owner_Type_Third, Fuel_Type_Diesel]
	
        print(fs)
        prediction=model.predict([fs])
        output=np.round(prediction[0],2)
        print(str(output)+" predicted ")
        if output<0:
            return render_template('index.html',prediction="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

