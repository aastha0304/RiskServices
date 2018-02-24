```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres
docker exec -it <container_name> bash
psql -U postgres
CREATE DATABASE data;

```
On another shell, in root of service project, update db details in settings.py

```
python manage.py makemigrations
python manage.py migrate

```
Back to postgres db, check for models in data store

```
\c data;

```

Back to service root, create some models

```
from risk_apis.models import *
Risk.objects.create(label='prize', description='prize insurance',
             value={
                 'coverage_limit': '10000',
                 'event': 'golf tournament'
         })
Risk.objects.create(label='accident',
             value={
                 'coverage_limit': '10000',
                 'vehicle_type': '4_wheeler'
         })
Risk.objects.create(label='accident', description='accident insurance',
             value={
                 'coverage_limit': '10000',
                 'vehicle': '4 wheeler'
         })
Risk.objects.create(label='houses',
             value={
                 'coverage_limit': '10000',
                 'age_of_house_limit': '2'
         })

```

Start the server

```
python manage.py runserver

```

Test things work

```
http://localhost:8000/risks  # rendered page displayed
http://localhost:8000/api/risk/ # rest call results
http://localhost:8000/api/risks/ # rendered page displayed

```