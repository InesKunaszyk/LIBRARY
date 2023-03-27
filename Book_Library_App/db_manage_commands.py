from Book_Library_App import app, db

@app.cli.group()
def db_manage():
    """Commands for database"""
    pass

@db_manage.command()
def add_data():
    """Add data to database"""
    pass

@db_manage.command()
def remove_data():
    """Delete ALL data from database"""
    pass