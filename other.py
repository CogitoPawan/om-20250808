project-root
│   README.md
│   requirements.txt
│   docker-compose.yml
└───anomaly_detection
│   │   main.py
│   │   config.py
│   │
│   ├───api
│   │   ├── endpoints.py
│   │   └── models.py
│   │
│   ├───services
│   │   ├── anomaly_service.py
│   │   └── alert_service.py
│   │
│   ├───utils
│   │   ├── logging.py
│   │   └── exceptions.py
│   │
│   └───tests
│       ├── test_anomaly_service.py
│       └── test_alert_service.py
└───frontend
    ├───public
    │   └── index.html
    └───src
        └── App.js

# Anomaly Detection from Weekly Sales Data

## Overview

This project implements a system to detect anomalies in weekly sales data. It leverages a microservices architecture and real-time data streaming to provide quick and accurate anomaly detection, real-time alerts, and comprehensive reporting.

## Prerequisites

- Python 3.8+
- Docker
- Docker Compose
- Node.js

## Setup Instructions

1. Clone the repository

2. Create a virtual environment and install dependencies

3. Set up environment variables in a `.env` file

4. Run the application using Docker Compose

5. Navigate to `http://localhost:3000` to access the frontend.

## Running Tests

To run unit tests:

1. Activate the virtual environment

2. Run the tests

## Technologies Used

- Backend: Flask, SQLAlchemy, FastAPI
- Frontend: React.js, Tailwind CSS
- Database: PostgreSQL, Redis
- Real-time processing: Apache Kafka
- Monitoring: Application Insights

fastapi
uvicorn
SQLAlchemy
psycopg2-binary
redis
pydantic
requests
pytest
pytest-cov

version: '3.8'

services:
  postgres:
    image: postgres:13
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: anomalydb
    ports:
      - "5432:5432"

  redis:
    image: redis:6-alpine
    ports:
      - "6379:6379"

  backend:
    build: .
    command: uvicorn anomaly_detection.main:app --host 0.0.0.0 --port 8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - postgres
      - redis

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend

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

DATABASE_URL=postgresql://user:password@localhost/anomalydb
SECRET_KEY=your_secret_key
ALERT_URL=http://alert-service/alert