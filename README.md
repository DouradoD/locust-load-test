# locust-load-test

Archtecture - Data-Driven Testing

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
- api package - Responsible for store the Database/API and those API tests
  - tests - Unit tests to cover the API
- utils package - Utils functions and common actions
- locustfile.py -  Responsible for run the load test using the API user


