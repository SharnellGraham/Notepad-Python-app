# Notepad Application

This is a simple notepad application built with Python and Peewee.

## Setup

1. Clone this repository.
2. Install the required packages with `pip install -r requirements.txt`.
3. Create the database with `python3 peewee_notes_model.py`.
4. Run the application with `python3 note_pad_app.py`.

## Usage

The application has the following commands:

- `create`: create a new note.
- `list`: list all notes.
- `get`: get a specific note by title.
- `update_title`: update a note's title.
- `update_content`: update a note's content.
- `delete`: delete a note by title.

To run a command, type the command name when prompted after running `python3 note_pad_app.py`.

## User Interface

A user interface for this notepad application has been built with PySimpleGUI. To use it, run `python3 gui.py` instead of `python3 note_pad_app.py`.
