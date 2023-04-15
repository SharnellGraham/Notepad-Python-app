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

def list_notes():
    notes = NoteModel.select()
    for note in notes:
     print(f'{note.title} - {note.content}')

def get_note():
    title = input("Enter note title: ")
    try:
        note = NoteModel.get(NoteModel.title == title)
        print(f'{note.title} - {note.content}')
    except NoteModel.DoesNotExist:
        print(f'Note with title "{title}" does not exist.')

