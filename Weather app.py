import requests
def get_weather(city):
    api_key = "f6be5906359d00480b0462d14341e197"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}&units=metric"

    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            humidity = main["humidity"]
            pressure = main["pressure"]
            weather_description = weather["description"]

            weather_report = (
                f"Weather in {city}:\n"
                f"Temperature: {temperature}°C\n"
                f"Humidity: {humidity}%\n"
                f"Pressure: {pressure} hPa\n"
                f"Description: {weather_description.capitalize()}"
            )
        else:
            weather_report = f"City {city} not found."

    except requests.exceptions.RequestException as e:
        weather_report = f"Error fetching weather data: {e}"

    return weather_report

def weather_app():
    print("Welcome to the Weather App!")
    city = input("Enter city name: ")
    weather_report = get_weather(city)
    print(weather_report)


if __name__ == "__main__":
    weather_app()
