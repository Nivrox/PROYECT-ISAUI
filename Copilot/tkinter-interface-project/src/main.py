import tkinter as tk
from ui.interface import MainInterface

def main():
    root = tk.Tk()
    root.title("Tkinter Interface Project")
    root.geometry("400x300")

    app = MainInterface(root)
    app.setup_ui()

    root.mainloop()

if __name__ == "__main__":
    main()