# library IoT security system

  
  

## Deploy application in Heroku

### Login to Heroku account.
```sh
heroku login
```

  

### Login to Heroku registry container.

```sh
heroku container:login
```
  

### Create a new app

```sh
heroku create
```  

### Build and upload to heroku registry the image of our Django application

```sh
heroku container:push web --app <app_name>
```
  

### Release our Django application
```sh
heroku container:release web --app <app_name>
```
  
## Deploy production at heroku

- In settings.py - ```DEBUG = False```

- Run: ```python manage.py collectstatic```

- Install whitenoise: ```pip install whitenoise```

- Add configuration to serve statics with whitenoise in settings.py

- Run: ```heroku container: push web --app <app_name>```

- Run: ```heroku container:release web --app <app_name>```