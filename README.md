# LAB - Class 32

## project name : Permissions & Postgresql

## **Alaa Hmaidat**

---
## Project Setup
1. Create a virtual environment (venv):
```
python3 -m venv .venv
``` 
2. Activate the virtual environment:
- On macOS and Linux:
```
source .venv/bin/activate
``` 
- On Windows:
```
.venv\Scripts\activate
```
3. Install project requirements:
```
pip install -r requirements.txt
```
### Running the Project
1. Activate the virtual environment:

- On macOS and Linux:

```
source .venv/bin/activate
```

- On Windows:

```
.venv\Scripts\activate
```

2. Start the development server:


```
python manage.py runserver
```
The server will start running on http://127.0.0.1:8000/.

### Running the Project using docker
1. Build and start the Docker containers:

```
docker-compose up --build
```
This command will build the Docker image and start the Django development server inside a container.

2. Access the Django application:

The Django development server will be accessible at http://localhost:8000.

You can now develop and test your Django application within the Docker environment.

## Running Tests
To run tests for your project:

1. Activate the virtual environment (if not already activated):

- On macOS and Linux:

```
source .venv/bin/activate
```

- On Windows:


```
.venv\Scripts\activate
```
2. Run the tests using the following command:

```
python manage.py test
```
This will execute all the tests and display the test results.