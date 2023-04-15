import argparse
from note_model import NoteModel
from peewee_notes_model import create_tables, seed_data

reate_tables()
seed_data()

def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note = NoteModel.create(title=title, content=content)
    print(f'Note "{note.title}" created successfully!')