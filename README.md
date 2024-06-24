# Dental Scraper Readme Documentation

# Installation

## Installation of Required dependencies 

### 1. python3
- `brew install python@3.12`
> Check your installation via command: 
> - `python3 --version`
> - Output should be python `3.12.*`. 

## Installation of Repo

Make a virtual environment to keep all the repo packages separate from the global packages
- `python3.12 -m venv venv`
- `source venv/bin/activate`


Install all the packages required for proper functioning:
- `pip install -r requirements.txt`

We are done, you can now run the server and check if everything is setup properly

`python run.py`

You can also checkout this to check swagger documentation provided by fastapi
`{{host}}/docs`

If you are running on local it will be `http://127.0.0.1:8000/docs`