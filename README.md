# Elevator
Elevator management system using Rest Apis

## Installation
1. Running locally
    - Clone the repository
    - Create a virtual environment
    - Activate the virtual environment and install the requirements
    - Run the makemigrations and migrate commands
    - Run the server
   ```bash
    - git clone
    - cd Elevator
    - virtualenv venv
    - source venv/bin/activate
    - pip install -r requirements.txt
    - python manage.py runserver
    ```
2. Prod ready app using docker
    - Clone the repository
    - Run the docker-compose file
    ```bash
    - git clone
    - cd Elevator
    - docker-compose up -d --build
    ```

## Project Structure
```
.
├── Dockerfile
├── README.md
├── docker-compose.yml
├── Elevator
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models
│   │   ├── __init__.py
│   │   ├── elevator.py
│   │   ├── elevator_request.py
│   │   └── elevator_system.py
│   ├── serializers
│   │   ├── __init__.py
│   │   ├── elevator_serializer.py
│   │   ├── elevator_request_serializer.py
│   │   └── elevator_system_serializer.py
│   ├── viewsets
│   │   ├── __init__.py
│   │   ├── elevator_request_viewset.py
│   │   ├── elevator_system_viewset.py
│   │   └── elevator_viewset.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
│   ├── docs
│   │   ├── apis.md
├── Elevator System.postman_collection.json

```

## Thought Process
- The elevator system has a name, number of elevators and number of floors
- An elevator system can have many elevators signifying one-to-many relationship
- An elevator has a number, current floor, direction, next stop, is door open, is operational
- An elevator has a one to many relationship with the requests. 

### Design thought
  - First, I tried to design with considering only one elevator systems where I will store N objects for elevators depincting an elevator system.
  - But I realised that the above approach might not be scalable as this app will only depict one elevator system and will have to destroy all elevators when creating a new one. 
  - Then I created seprate model for Elevator System and Elevator. This way I can create multiple elevator systems and each elevator system can have multiple elevators.

### Assumptions
- The elevator system is created with a name, number of elevators and number of floors
- The elevator system is created with all the elevators in the system in the ground floor
- The elevator system is created with all the elevators in the system in operational state
- Upon recieving request, system will assign the nearest elevator to the requested floor

### Other Points
- Current DB is sqlite which is default DB in a django project, we can use any other DB and provide its connection on settings file.
- I have not picked DB credentials from an env file, which is highly suggested while working on production servers.
- I have added postman collection which can be imported to check the APIs.
- All the APIs information can be checked in the file api.md which is present inside docs folder.