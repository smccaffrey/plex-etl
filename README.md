# plex-etl [![Python 3.7.3](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

An ETL tool for extracting, transforming, and loading media into your Plex Server.

# Why use plex-etl?
Are you the type of person who doesn't use automated RSS feeds to gather media for your Media Server? Are you tired of having no standard directory structure for your Media Server's libraries? Well, if so, then this is the tool for you!

# Features
plex-etl currently has the following capabilities:
* Extract all media files from an infinitely nested directory structure. Just point plex-etl at the most top level directory where you dump media files and it will take care of the rest.
* A specific queue built for ingesting ~~movies~~ media files into a target library directory.
# Installation
```shell script
$ git clone https://github.com/smccaffrey/plex-etl.git
```
plex-etl will create a directory under you user's home directory, i.e. `~/.plex-etl`, which is where all data/databases will be stored.
# Usage
```shell script
~/plex-etl $ pipenv install
```

Run in `dev` mode
```shell script
~/plex-etl $ pipenv run python manage.py dev
```

Run in `prod` mode
```shell script
~/plex-etl $ pipenv run python manage.py prod
```

# Stack
![python-logo](https://user-images.githubusercontent.com/11462398/76695212-b7bce380-6639-11ea-9fbc-abf17e40511c.png)
![flask-powered](https://user-images.githubusercontent.com/11462398/76695149-074edf80-6639-11ea-94b5-7076fe17c723.png)
![sqla_logo](https://user-images.githubusercontent.com/11462398/76695166-3f562280-6639-11ea-84a5-c6e72a1026ee.png)

## Sample Usage
### Config Screen
![config_example](https://user-images.githubusercontent.com/11462398/76706998-fc339800-66a8-11ea-951f-2f66abdc6c5d.gif)

### Movie Queue
![screen_recording](https://user-images.githubusercontent.com/11462398/76693060-6baf7600-661c-11ea-8e4d-1692a4bd1d5d.gif)

### Versions

#### 1.0.0