# WMGSIS
This is a Django project that provides statistical information for WMG.



## Running the project 
You should already have python installed on your computer. I'd advise you create a virtual enviroment to store the project dependencies seperately, you can install virtualenv with 

```
pip install virtualenv
```

Clone or download this repository and open it in your editor, then create the virtual env

```
virtualenv env
```

Next activate it with 

```
source venv/bin/activate
```

Now install the project dependencies with 

```
pip install -r requirements.txt
```


Then create the tables for the database

```
makemigrations app
```

Then run this command to migrate

```
manage.py migrate
```

Run the development server

```
python manage.py runserver
```

Go to web-browser and open
```
http://127.0.0.1:8000
```


## Guides

- https://www.djangoproject.com/start/
