# from flask import Flask, jsonify
# import json

# app = Flask(__name__)

# @app.route('/weather', methods=['GET'])
# def get_weather():
#     with open('data/weather.json') as file:
#         data = json.load(file)
#     return jsonify(data)

# @app.route('/hotels', methods=['GET'])
# def get_hotels():
#     with open('data/hotels.json') as file:
#         data = json.load(file)
#     return jsonify(data)

# @app.route('/places', methods=['GET'])
# def get_places():
#     with open('data/places.json') as file:
#         data = json.load(file)
#     return jsonify(data)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, jsonify, request
import json

from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Load data once at startup
with open("data/weather.json") as weather_file:
    weather_data = json.load(weather_file)

with open("data/hotels.json") as hotels_file:
    hotels_data = json.load(hotels_file)

with open("data/places.json") as places_file:
    places_data = json.load(places_file)


# Get a list of cities
@app.route("/api/cities", methods=["GET"])
def get_cities():
    cities = [{"name": entry["city"]} for entry in weather_data]
    return jsonify(cities)


# Get details for a specific city
@app.route("/api/cities/<city>", methods=["GET"])
def get_city_details(city):
    # Fetch weather data for the specified city
    city_weather = next((entry for entry in weather_data if entry["city"].lower() == city.lower()), None)
    
    # Fetch hotels and places from the object format
    city_hotels = hotels_data.get(city, [])
    city_places = places_data.get(city, [])

    if not city_weather and not city_hotels and not city_places:
        return jsonify({"error": "City not found"}), 404

    return jsonify({
        "weather": {
            "temperature": city_weather.get("temperature", "N/A") if city_weather else "N/A",
            "condition": city_weather.get("condition", "N/A") if city_weather else "N/A"
        },
        "hotels": [
            {
                "name": hotel.get("name", "N/A"),
                "rating": hotel.get("rating", "N/A"),
                "address": hotel.get("address", "N/A")
            }
            for hotel in city_hotels
        ],
        "places": [
            {
                "name": place.get("name", "N/A"),
                "rating": place.get("rating", "N/A"),
                "address": place.get("address", "N/A")
            }
            for place in city_places
        ]
    })

if __name__ == "__main__":
    app.run(debug=True)
