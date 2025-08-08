import React, { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [anomalies, setAnomalies] = useState([]);

  useEffect(() => {
    axios.get("/anomalies/")
      .then(response => {
        setAnomalies(response.data);
      })
      .catch(error => {
        console.error("There was an error fetching the anomalies!", error);
      });
  }, []);

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Sales Anomalies</h1>
      <table className="table-auto w-full mt-4">
        <thead>
          <tr>
            <th>Week</th>
            <th>Sales</th>
          </tr>
        </thead>
        <tbody>
          {anomalies.map((anomaly) => (
            <tr key={anomaly.id}>
              <td>{anomaly.sales_week}</td>
              <td>{anomaly.sales_data}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;