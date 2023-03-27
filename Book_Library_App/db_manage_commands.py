
import json
from pathlib import Path
import datetime

from Book_Library_App import app, db
from Book_Library_App.models import Author

from sqlalchemy.sql import text


@app.cli.group()
def db_manage():
    """Commands for database"""
    pass


@db_manage.command()
def add_data():
    """Add data to database"""
    try:
        authors_path = Path(__file__).parent / 'samples' / 'authors.json'
        with open(authors_path) as file:
            data_json = json.load(file)

            for item in data_json:
                item['birth_date'] = datetime.datetime.strptime(item['birth_date'], '%d-%m-%Y').date()
                author = Author(**item)
                db.session.add(author)
            db.session.commit()
            print('GOOD JOB! Data has been added to database')
    except Exception as exc:
        print('Unexpected error:{}'.format(exc))


@db_manage.command()
def remove_data():
    """Delete ALL data from database"""
    try:
        db.session.execute(text('DROP TABLE author'))
        db.session.commit()
        print('Data has been deleted to database')
    except Exception as exc:
        print('Unexpected error:{}'.format(exc))
