# Flask scaffold example

Simple stub of a Flask application that can be used to bootstrap a flask project

Requires Python 3

Check Flask documentation here: https://flask.palletsprojects.com/en/1.1.x/ 

## Virtual environment

Recommend using Python virtual env, can be created as such: 

`python3 -m venv env`

Loading virtual env: `source env/bin/activate` or on Windows run `env\scripts\activate.bat`


## Install requirements:

Read above section and load venv as necessary. 
Install using 

```bash
pip3 install -r requirements.txt
```

## Running:

Run as follows:

`python server/server.py` 

Output should look as follows: 

```
2020-06-03 17:16:12,470 INFO: Running server at 127.0.0.1 8080
 * Serving Flask app "scaffold-app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
 * Restarting with stat
2020-06-03 17:16:12,692 INFO: Running server at 127.0.0.1 8080
 * Debugger is active!
 * Debugger PIN: 539-222-217
```

Note that when running in debug mode the app launches twice and some logging is duplicated.
Saving working code results in an auto-reload. Broken code might require a server restart. 
