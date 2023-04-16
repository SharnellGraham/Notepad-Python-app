import tkinter as tk
import tkinter.scrolledtext as tkst
from datetime import datetime
from tkinter.messagebox import showinfo

class NotepadGUI:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")

        # create scrolled text widget
        self.text = tkst.ScrolledText(master, wrap=tk.WORD)
        self.text.pack(expand=True, fill=tk.BOTH)

        # create menu bar
        menu_bar = tk.Menu(master)
        master.config(menu=menu_bar)

        # create file menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_note)
        file_menu.add_command(label="Save", command=self.save_note)
        file_menu.add_command(label="Exit", command=self.exit_notepad)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # create help menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menu_bar.add_cascade(label="Help", menu=help_menu)

    def new_note(self):
        self.text.delete("1.0", tk.END)

    def save_note(self):
        note = self.text.get("1.0", tk.END)
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.txt")
        with open(filename, "w") as f:
            f.write(note)
        showinfo("Note saved", f"The note was saved to {filename}.")

    def exit_notepad(self):
        self.master.destroy()

    def show_about(self):
        about_text = "Notepad v0.1\n\nA simple text editor."
        showinfo("About Notepad", about_text)

root = tk.Tk()
notepad = NotepadGUI(root)
root.mainloop()
