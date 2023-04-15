# import the necessary libraries
from peewee import *
from note_model import NoteModel

# Create the database connection to notes.db file
db = SqliteDatabase('notes.db')

def create_tables():
    # create the tables in the database
    with db:
        db.create_tables([NoteModel])


def seed_data():
    # seed the database with some data 
    NoteModel.create(title='First note', content='This is my first note')
    NoteModel.create(title='Second note', content='This is my second note')

if __name__ == '__main__':
    # create the tables and seed the data into the database
    create_tables()
    seed_data()