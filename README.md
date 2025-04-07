# locust-load-test

Archtecture - Data-Driven Testing

#### Before start the load test

Check the tips at the end of this documentation

### Structure
```tests/
├── tests/
│   ├── api/
│   │   ├── tests/
│   │   │   ├── test_user.py
│   │   ├── user.py
│   ├── utils/
│   │   ├── helpers.py
│   ├── locustfile.py
├── .gitignore
├── README.md
├── requirements.txt

```
### Key Components

- **`api/`** - API interaction layer
  - `user.py`: CRUD operations for user API endpoints
  - `tests/test_user.py`: Unit tests for API functionality
- **`utils/`** - Shared utilities
  - `helpers.py`: Common functions for test data generation and validation
- **`locustfile.py`**: Main configuration for load tests

## Getting Started

### Prerequisites
- Python 3.8+
- Locust 2.0+

### Installation
```bash
    pip install -r requirements.txt
```


### Running Unit Tests
```bash
    pytest tests/api/tests/
```

### Load Tests

Before run the load test, start the API. 
- Run the following command:
```bash
     python tests/api/user.py
```

- Now run the Locust file
```bash
     locust -f locustfile.py --host http://localhost:5000    
```

The host was defined inside the tests/api/user.py API.

 - Then access the web interface at http://localhost:8089