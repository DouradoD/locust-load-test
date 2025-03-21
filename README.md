# locust-load-test

Archtecture - Data-Driven Testing

### Structure
```tests/
├── api/
│   ├── services/
│   │   ├── post_service.py
│   │   ├── user_service.py
│   ├── endpoints/
│   │   ├── post_endpoint.py
│   │   ├── user_endpoint.py
├── data/
│   ├── test_data.py
├── utils/
│   ├── helpers.py
├── locustfile.py
├── README.md
├── requirements.txt

```
- api package - Service Objects - Encapsulate the APIs responsibility
- data package - Static data store responsibility
- utils package - Utils functions and common actions
- locustfile.py -  
