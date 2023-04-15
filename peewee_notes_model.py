# Import the datetime module and peewee ORM
import datetime 
from peewee import *

# Create the database connection to notes.db file
db = SqliteDatabase('notes.db')