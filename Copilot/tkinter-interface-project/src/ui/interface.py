class MainInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Tkinter Interface Project")
        self.master.geometry("400x300")

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.master, text="Welcome to the Tkinter Interface Project", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = ttk.Entry(self.master, width=30)
        self.entry.pack(pady=5)

        self.button = ttk.Button(self.master, text="Submit", command=self.on_submit)
        self.button.pack(pady=10)

    def on_submit(self):
        user_input = self.entry.get()
        print(f"User input: {user_input}")  # Replace with desired functionality