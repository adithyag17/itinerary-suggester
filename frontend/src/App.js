import React, { useState, useEffect } from "react";
import "./styles/App.css";

function App() {
  const [cities, setCities] = useState([]); // List of cities
  const [selectedCity, setSelectedCity] = useState(""); // Selected city
  const [cityData, setCityData] = useState(null); // Data for the selected city

  // Fetch all available cities from the backend
  useEffect(() => {
    fetch("http://localhost:5000/api/cities") // Backend endpoint for available cities
      .then((response) => response.json())
      .then((data) => {
        const cityNames = data.map((city) => city.name);
        setCities(cityNames);
      })
      .catch((error) => console.error("Error fetching cities:", error));
  }, []);

  // Fetch details of the selected city
  const handleCityChange = (event) => {
    const city = event.target.value;
    setSelectedCity(city);

    if (city) {
      fetch(`http://localhost:5000/api/cities/${city}`) // Backend endpoint for city data
        .then((response) => response.json())
        .then((data) => setCityData(data))
        .catch((error) => console.error("Error fetching city data:", error));
    } else {
      setCityData(null);
    }
  };

  return (
    <div className="App">
      <div className="header">
        <h1>Explore Tourist Destinations</h1>
      </div>

      {/* Dropdown for city selection */}
      <div className="dropdown">
        <label htmlFor="city-select">Select a city:</label>
        <select
          id="city-select"
          value={selectedCity}
          onChange={handleCityChange}
        >
          <option value="">--Select a city--</option>
          {cities.map((city) => (
            <option key={city} value={city}>
              {city}
            </option>
          ))}
        </select>
      </div>

      {/* Display data for the selected city */}
      {cityData && (
        <div className="city-details">
          <h2>{selectedCity}</h2>

          <h3>Weather:</h3>
          <p>
            Temperature: {cityData.weather?.temperature || "N/A"}, Condition:{" "}
            {cityData.weather?.condition || "N/A"}
          </p>

          <h3>Top Hotels:</h3>
          <ul>
            {cityData.hotels.length > 0 ? (
              cityData.hotels.map((hotel, index) => (
                <li key={index}>
                  <strong>{hotel.name}</strong> <br />
                  Rating: {hotel.rating || "N/A"} <br />
                  Address: {hotel.address || "N/A"}
                </li>
              ))
            ) : (
              <p>No hotels available</p>
            )}
          </ul>

          <h3>Best Places to Visit:</h3>
          <ul>
            {cityData.places.length > 0 ? (
              cityData.places.map((place, index) => (
                <li key={index}>
                  <strong>{place.name}</strong> <br />
                  Rating: {place.rating || "N/A"} <br />
                  Address: {place.address || "N/A"}
                </li>
              ))
            ) : (
              <p>No places available</p>
            )}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
