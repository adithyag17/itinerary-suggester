import React, { useEffect, useState } from "react";

const Hotels = () => {
  const [hotelsData, setHotelsData] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:5000/hotels")
      .then((response) => response.json())
      .then((data) => setHotelsData(data))
      .catch((error) => console.error("Error fetching hotels data:", error));
  }, []);

  return (
    <section>
      <h2>Top Hotels</h2>
      <table>
        <thead>
          <tr>
            <th>City</th>
            <th>Hotel Name</th>
            <th>Rating</th>
            <th>Address</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(hotelsData).map(([city, hotels], index) =>
            hotels.map((hotel, idx) => (
              <tr key={`${index}-${idx}`}>
                <td>{city}</td>
                <td>{hotel.name}</td>
                <td>{hotel.rating}</td>
                <td>{hotel.address}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </section>
  );
};

export default Hotels;
