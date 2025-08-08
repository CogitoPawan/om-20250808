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