from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '3b2c4e31cebeae605c609bf22714bcd1'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code != 200:
        return jsonify({'error': data.get('message', 'Error fetching weather data')}), response.status_code

    weather_data = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)