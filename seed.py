# import the necessary libraries
from peewee import *
from note_model import NoteModel

# Create the database connection to notes.db file
db = SqliteDatabase('notes.db')

def create_tables():
    # create the tables in the database
    with db:
        db.create_tables([NoteModel])
