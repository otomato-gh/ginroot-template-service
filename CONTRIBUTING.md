# Developing

Python version: 3.10+

## Create a virtual environment. 

If you decide to use [pyenv](https://github.com/pyenv/pyenv) with virtualenvwrapper (this is what I'm using):

```bash
pyenv install 3.10.7
pyenv virtualenvwrapper
mkvirtualenv -p ${PYENV_ROOT}/versions/3.10.6/bin/python3 ginroot
workon ginroot
```

Or use any other way of activating a virtualenv with python 3.10.6 installed

## Install dependencies

The project is managed using [poetry](https://python-poetry.org/)

- Install poetry:
`pip install poetry`

- Install project dependencies:
`poetry install`

** Note about psycopg2-binary **

On MacOS you will probably get an error installing the package named *psycopg2-binary*

My way of resolving this was:

`brew install postgresql`

and then:

`pip install psycopg2-binary`

But [@Samofimp](https://github.com/Samofimp) says she managed without installing the whole thing. Instead she installed some libs...
Ask her if interested.

## DB management

The DB for testing is executed in a Docker container (see [README.md](README.md)).

If you want a nice UI to manage the data - give [OmniDB](https://github.com/OmniDB/OmniDB) a try.

## Start developing:
Follow the instructions in [README.md](README.md)


