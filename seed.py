# import the necessary libraries
from peewee import *
from note_model import NoteModel

# Create the database connection to notes.db file
db = SqliteDatabase('notes.db')
