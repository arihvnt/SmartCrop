from flask import Blueprint, render_template, request
import requests

weather_bp = Blueprint('weather', __name__)

API_KEY = "565dde455a00dbb4ab7513773330f3d3"

@weather_bp.route('/weather', methods=['GET', 'POST'])
def weather():
    data = None
    if request.method == 'POST':
        city = request.form['city']
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        print(response)  # 🔹 Add this to debug in terminal

        if response.get("main"):
            data = {
                "city": city,
                "temperature": response["main"]["temp"],
                "humidity": response["main"]["humidity"],
                "condition": response["weather"][0]["description"]
            }
    return render_template("weather.html", data=data)



