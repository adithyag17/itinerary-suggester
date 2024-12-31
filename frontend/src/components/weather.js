import React, { useEffect, useState } from "react";

const Weather = () => {
  const [weatherData, setWeatherData] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/weather")
      .then((response) => response.json())
      .then((data) => setWeatherData(data))
      .catch((error) => console.error("Error fetching weather data:", error));
  }, []);

  return (
    <section>
      <h2>Weather Data</h2>
      <table>
        <thead>
          <tr>
            <th>City</th>
            <th>Temperature</th>
            <th>Condition</th>
          </tr>
        </thead>
        <tbody>
          {weatherData.map((item, index) => (
            <tr key={index}>
              <td>{item.city}</td>
              <td>{item.temperature}</td>
              <td>{item.condition}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
};

export default Weather;
