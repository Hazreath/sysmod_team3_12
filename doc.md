# Documentation
Please read this document very carefully. You will find every important information about this system.
If you have any question that is not answered here feel free to ask me: Maxime Moreau.

## Dependencies
Python >= 3.8 (and maybe >=3.7 could also works but I'm not sure).

Install them, for example via pip:
```
pip install --requirement ./requirements.txt
```

Or any virtualenv, pipenv... Anything you want.

## Run the software
```
uvicorn main:app --reload
```

## OpenAPI
The system has an OpenAPI documentation (following all of the guidelines).

To find the documentation, open your web browser and go on [http://localhost:8000/docs](http://localhost:8000/docs).

You will find **everything** about the API, all of the available endpoints are documented:
which HTTP method to use, HTTP arguments, what the endpoint does, you can every try it because the documentation is interactive.
