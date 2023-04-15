# Import the datetime module and peewee ORM
import datetime 
from peewee import *

# Create the database connection to notes.db file
db = SqliteDatabase('notes.db')

# Define the NoteModel class that uses db connection as Meta class
class NoteModel(Model):
    title = CharField() # Charfield for storing titles
    content = TextField() # Textfield for storing content
    date = DateTimeField(default=datetime.datetime.now) # DateTimeField with current time as default value

    class Meta:
        database = db
 # create the NoteModel table in the notes.db database
db.create_tables([NoteModel])