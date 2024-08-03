from database.db_setup import init_db
import tkinter as tk
from interface import EstudoApp

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = EstudoApp(root)
    root.mainloop()
