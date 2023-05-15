Project: Django Permissions and Postgresql

Author: Sheldon Pierce

How to initialize/run your application (where applicable)

```
  - python3.11 venv .venv
  - pip install -r requirements.txt
  - pip freeze > requirements.txt
  - docker compose up --build -d
  - docker compose run web python manage.py makemigrations
  - docker compose run web python manage.py migrate
  - docker compose run web python manage.py createsuperuser
  - docker compose run web python manage.py collectstatic
  - change site to localhost:8000
  - To see JSON data go to https://cookie-stand-api-sheldon-2qrah5q0o-sheldon-pierce.vercel.app/api/v1/cookie_stands/
  - To shut down properly docker compose down

```

Vercel App 

```
    - To see JSON data go to https://cookie-stand-api-sheldon-2qrah5q0o-sheldon-pierce.vercel.app/api/v1/cookie_stands/

```



Tests
- How do you run tests?
```
    Using httpie in the terminal
    - Getting auth token
        - http :8000/api/token
    - Refreshing auto token
        - http :8000/api/refresh
    - Checking data
        - http :8000/api/v1/cookie_stands/ username=*yourusername* password=*yourpassword*
```