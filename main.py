from flask import Flask
from flask import render_template
from flask import request
import requests

api_key = '85cc0a8a8a7e6695de777691cf451349'

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


    


@app.route("/result",methods=['POST'])
def result():
    city = request.form['city']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        hum = data['main']['humidity']
        fl_temp = data['main']['feels_like']
        temp = int(temp-273.15)
        fl_temp = int(fl_temp-273.15)
        wt_data = {'city':city,
                   'temp':temp,
                   'fl_temp':fl_temp,
                   'hum':hum,
                   'desc':desc}
        return render_template("result.html",weather=wt_data)
    else:
        return "Error fetching weather data. Please try again later."

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)