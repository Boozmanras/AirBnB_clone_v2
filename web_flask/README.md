# AirBnB_clone_v2

## Description

This repository contains the second version of the AirBnB clone project, a full-stack web application developed as part of the ALX SE curriculum. The goal of the project is to build a clone of the AirBnB website, complete with dynamic content and interactions between the backend and frontend. The project is divided into several phases, with this version focusing on deploying a dynamic web application using Flask, SQLAlchemy, and other tools.

## Project Structure

The project is organized into several directories:

- `models/`: Contains the classes for the ORM (Object-Relational Mapping) using SQLAlchemy. Models include `User`, `State`, `City`, `Amenity`, `Place`, and `Review`.
- `tests/`: Contains the test cases for the application.
- `console.py`: A command-line interpreter to interact with the storage engine.
- `web_flask/`: Contains the Flask web application files.
- `web_static/`: Contains the static assets (HTML, CSS, images) for the web application.

## Features

- **Command Interpreter**: A console application to create, read, update, and delete objects in the storage engine.
- **Storage Engines**: Supports both file storage (`FileStorage`) and database storage (`DBStorage`) using SQLAlchemy.
- **Web Framework**: Uses Flask to create dynamic web pages.
- **Database**: MySQL is used for the database storage.
- **Templating**: Jinja2 is used for rendering dynamic content in HTML templates.

## HBNB is alive!

This specific task sets up a Flask web application to display a dynamic HTML page with states, cities, amenities, and places, using data fetched from the storage engine.

### Features

- The application listens on `0.0.0.0`, port `5000`.
- Routes:
  - `/hbnb`: Displays an HTML page similar to `8-index.html`.
- Uses the storage engine to fetch data from the database.
- Handles app context teardown to remove the current SQLAlchemy session.
- Static files and templates are organized under `web_flask/static` and `web_flask/templates` respectively.
- Imported a SQL dump file (`100-dump.sql`) to have some data for the application.

### Setup

1. Ensure you have a valid `setup_mysql_dev.sql` in your repository.
2. Run the following commands to set up your database and load initial data:
   ```bash
   $ echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py
   $ curl -o 100-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/100-hbnb.sql"
   $ cat 100-dump.sql | mysql -uroot -p
