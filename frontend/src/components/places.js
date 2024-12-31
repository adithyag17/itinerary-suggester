import React, { useEffect, useState } from "react";

const Places = () => {
  const [placesData, setPlacesData] = useState({});

  useEffect(() => {
    fetch("http://127.0.0.1:5000/places")
      .then((response) => response.json())
      .then((data) => setPlacesData(data))
      .catch((error) => console.error("Error fetching places data:", error));
  }, []);

  return (
    <section>
      <h2>Top Places to Visit</h2>
      <table>
        <thead>
          <tr>
            <th>City</th>
            <th>Place Name</th>
            <th>Rating</th>
            <th>Address</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(placesData).map(([city, places], index) =>
            places.map((place, idx) => (
              <tr key={`${index}-${idx}`}>
                <td>{city}</td>
                <td>{place.name}</td>
                <td>{place.rating}</td>
                <td>{place.address}</td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </section>
  );
};

export default Places;
