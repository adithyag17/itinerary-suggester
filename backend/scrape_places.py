import requests
import json

def scrape_places():
    url = "https://travel-advisor.p.rapidapi.com/attractions/list-by-latlng"
    api_key = "76769c82f0msh8314d65c5780e02p10aea2jsndc535f0fe63c"  # Replace with your RapidAPI key

    # Example city coordinates (replace these with actual coordinates)
    cities = {
        "New York": {"lat": 40.7128, "lng": -74.0060},
        "London": {"lat": 51.5074, "lng": -0.1278},
        "Tokyo": {"lat": 35.6895, "lng": 139.6917},
        "Rome": {"lat": 41.9028, "lng": 12.4964},
        "Paris": {"lat": 48.8566, "lng": 2.3522},
        "Madrid": {"lat": 40.4168, "lng": -3.7038},
        "Singapore": {"lat": 1.3521, "lng": 103.8198},
        "Barcelona": {"lat": 41.3851, "lng": 2.1734},
        "Berlin": {"lat": 52.5200, "lng": 13.4050},
        "Sydney": {"lat": -33.8688, "lng": 151.2093},
        "Goa": {"lat": 15.2993, "lng": 74.1240},
        "Bangalore": {"lat": 12.9716, "lng": 77.5946},
        "Chennai": {"lat": 13.0827, "lng": 80.2707}

    }

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "travel-advisor.p.rapidapi.com"
    }

    places_data = {}

    for city, coords in cities.items():
        print(f"Scraping top destinations for {city}...")
        query_params = {
            "latitude": coords["lat"],
            "longitude": coords["lng"],
            "limit": 3,  # Limit results to top 5 attractions
            "currency": "USD",
            "lang": "en_US"
        }

        try:
            response = requests.get(url, headers=headers, params=query_params)
            if response.status_code == 200:
                attractions = response.json().get("data", [])
                places_data[city] = [
                    {
                        "name": attraction.get("name", "N/A"),
                        "rating": attraction.get("rating", "N/A"),
                        "address": attraction.get("address", "N/A")
                    }
                    for attraction in attractions if "name" in attraction
                ]
            else:
                print(f"Failed to fetch data for {city}. Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error occurred for {city}: {e}")

    # Save data to places.json
    with open("data/places.json", "w") as file:
        json.dump(places_data, file, indent=4)

    print("Top destinations data successfully saved to places.json.")

if __name__ == "__main__":
    scrape_places()
