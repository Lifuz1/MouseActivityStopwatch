"""
This is the main module of the application.

Classes:
    ProStopWatch: A stopwatch class defined in Stopwatch_project.py

"""

import tkinter as tk
from tkinter import ttk, Frame
import time
from Stopwatch import ProStopWatch


def main():
    """
    The main function of the application. It sets up the GUI and starts the Tkinter event loop.

    The GUI consists of a main window with a notebook widget.
    In the future, the notebook will have two tabs: 'ProStopwatch' and 'RNG'.
    RNG will be a random number generator that is useful for people who utilize GTO (Game Theory Optimal) in their game.
    """
    # Create the main GUI window
    root = tk.Tk()
    root.title("Stopwatch_project")
    root.geometry("440x200")
    root.minsize(440, 200)
    root.maxsize(440, 200)

    my_notebook = ttk.Notebook(root)
    my_notebook.pack(pady=0)

    my_frame1 = Frame(my_notebook, width=440, height=200)
    my_frame1.pack(fill="both", expand=1)

    my_notebook.add(my_frame1, text="ProStopwatch")

    pro_stopwatch = ProStopWatch(my_frame1)

    def on_closing():
        """
        This function is called when the main window is closed. It stops the mouse tracking thread
        in the ProStopWatch instance and then destroys the main window.
        """
        pro_stopwatch.is_mouse_tracking = False  # Stop mouse tracking thread
        time.sleep(0.1)  # Allow time for threads to finish
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


if __name__ == "__main__":
    main()
