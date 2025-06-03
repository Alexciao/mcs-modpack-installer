import threading
import tkinter as tk
from tkinter import ttk
import logging

# GLOBAL references
log_text_widget = None


# Custom logging handler
class TextHandler(logging.Handler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text_widget.insert(tk.END, msg + "\n")
            self.text_widget.see(tk.END)

        self.text_widget.after(0, append)


# Example function to simulate work
def start_task():
    import main

    def task():
        main.install_prism_launcher()

    threading.Thread(target=task, daemon=False).start()


# Logger setup
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# GUI Setup
def create_main_window():
    global progress_var, log_text_widget

    root = tk.Tk()
    root.title("Minecraft Steam Modpack Installer")

    # Start button
    start_button = ttk.Button(root, text="Start Installation", command=start_task)
    start_button.pack(padx=10, pady=2, expand=True, fill=tk.X)

    # TODO: actual install logic + add profile

    # Log window setup
    log_text_widget = tk.Text(
        root, height=15, width=60, wrap="none", state="normal", font=("Arial", 10)
    )
    log_text_widget.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Attach logging handler to text widget
    text_handler = TextHandler(log_text_widget)
    formatter = logging.Formatter("%(message)s")
    text_handler.setFormatter(formatter)
    logger.addHandler(text_handler)

    return root


if __name__ == "__main__":
    window = create_main_window()
    window.mainloop()
    exit(0)
