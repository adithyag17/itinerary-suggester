import requests
from bs4 import BeautifulSoup
import json

def scrape_weather():
    cities = ["New York", "London", "Tokyo", "Rome", "Paris", "Madrid", "Singapore", "Barcelona", "Berlin", "Sydney", "Goa", "Chennai","Bangalore"]
    weather_data = []
    
    for city in cities:
        url = f"https://wttr.in/{city}?format=j1"
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = response.json()
                weather_data.append({
                    "city": city,
                    "temperature": f"{data['current_condition'][0]['temp_C']}°C",
                    "condition": data['current_condition'][0]['weatherDesc'][0]['value']
                })
            except json.JSONDecodeError:
                print(f"Failed to decode JSON for {city}")
        else:
            print(f"Failed to fetch weather for {city}: {response.status_code}")
    
    # Save data to JSON
    with open("data/weather.json", "w") as file:
        json.dump(weather_data, file, indent=4)
    print("Weather data saved.")

if __name__ == "__main__":
    scrape_weather()