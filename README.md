# competition
Code for https://stackoverflow.com/questions/58524428/is-there-a-way-to-create-a-unique-id-over-2-fields

You'll need Django on your machine.

Clone the repository:  
<code>git clone https://github.com/cezar77/competition/</code>

Descend in the newly created directory.  
Create superuser:

```
python manage.py createsuperuser
```

You'll use the username and the password to login to the **admin**.

Load the fixtures (optional):

```
python manage.py loaddata competitor
python manage.py loaddata event
python manage.py loaddata participant
```

Now you can run:
```
python manage.py runserver
```

and visit *http://localhost:8000/admin* in your browser.
