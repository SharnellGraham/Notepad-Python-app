
import argparse
from peewee_notes_model import NoteModel




# Create note
def create_note():
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    note = NoteModel.create(title=title, content=content)
    print(f'Note "{note.title}" created successfully!')

# List notes
def list_notes():
    notes = NoteModel.select()
    for note in notes:
     print(f'{note.title} - {note.content}')

# Get note by title
def get_note():
    title = input("Enter note title: ")
    try:
        note = NoteModel.get(NoteModel.title == title)
        print(f'{note.title} - {note.content}')
    except NoteModel.DoesNotExist:
        print(f'Note with title "{title}" does not exist.')

# Update notes title
def update_title():
    old_title = input("Enter current note title: ")
    new_title = input("Enter new note title: ")
    note = NoteModel.get(NoteModel.title == old_title)
    note.title = new_title
    note.save()
    print(f'Note title updated to "{new_title}"')

# Update notes content 
def update_content():
    title = input("Enter note title: ")
    content = input("Enter new note content: ")
    note = NoteModel.get(NoteModel.title == title)
    note.content = content
    note.save()
    print(f'Note content updated')

# Delete note by title 
def delete_note():
    title = input("Enter note title: ")
    note = NoteModel.get(NoteModel.title == title)
    note.delete_instance()
    print(f'Note "{title}" deleted successfully')
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Notepad application')
    parser.add_argument('command', choices=['create', 'list', 'get', 'update_title', 'update_content', 'delete'])
    args = parser.parse_args()



if args.command == 'create':
        create_note()
    
elif args.command == 'list':
        list_notes()

elif args.command == 'get':
        get_note()

elif args.command == 'update_title':
        update_title()

elif args.command == 'update_content':
        update_content()        

elif args.command == 'delete':
        delete_note()