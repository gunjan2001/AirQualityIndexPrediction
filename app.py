
from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

# load the model from disk
model = pickle.load(open('random_forest_model.pkl' ,'rb'))

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	return render_template('home.html')

standard_to = StandardScaler()
@app.route('/predict',methods=['POST'])
def predict():
    
    if request.method == 'POST':

        T = float(request.form['temp'])

        TM = float(request.form['Maxtemp'])

        Tm = float(request.form['Mintemp'])

        SLP = float(request.form['Sea'])

        H = float(request.form['Humidity'])

        VV = float(request.form['Visibility'])

        V = float(request.form['Wind'])

        VM = float(request.form['Maxwind'])

        prediction=model.predict([[T,TM,Tm,SLP,H,VV,V,VM]])

        output=round(prediction[0],2)

        return render_template('result.html',prediction_text="Air Quality Index (PM 2.5) is : {}".format(output) )
    
    else:
        return render_template('home.html')
 
    # df=pd.read_csv('real_2016.csv')
    # my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    # my_prediction=my_prediction.tolist()
    # return render_template('result.html',prediction = my_prediction)

if __name__ == '__main__':
	app.run(debug=True)