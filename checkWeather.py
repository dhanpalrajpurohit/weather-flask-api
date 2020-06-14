from flask import Flask, render_template, request, flash
import json
import urllib.request
import requests
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['POST','GET'])
def weather():

    if request.method == 'POST':
        city = request.form['city']

        source = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ad06dc44bcfc93c5f3d1f48479679a37'
        list_of_data = requests.get(source).json()
        weather_data = []
        show=False
        if len(list_of_data)<4:
            show=True
            return  render_template('index.html',show=show)

        else:
            data = {
                'city': str(list_of_data['name']),
                'temp': str(list_of_data['main']['temp']),
                'min_temp':str(list_of_data['main']['temp_min']),
                'max_temp': str(list_of_data['main']['temp_max']),

                'desc': list_of_data['weather'][0]['description'],
                'icon':list_of_data['weather'][0]['icon']
            }
            weather_data.append(data)

            return render_template('index.html', weather_data=weather_data)
    elif request.method == 'GET' :
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
