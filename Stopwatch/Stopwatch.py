import tkinter as tk
from tkinter import simpledialog, filedialog
from datetime import date
import time
import openpyxl
import pyautogui
import threading


class ProStopWatch:
    """
       A stopwatch that starts and stops based on mouse movement.

       Attributes:
           threshold_time (int): The time in seconds the mouse has to be still for the stopwatch to stop.
           is_running (bool): Whether or not the stopwatch is currently running.
           is_mouse_tracking (bool): Whether or not mouse movement is currently being tracked.
           start_time (float): The time the stopwatch was last started.
           elapsed_time (float): The total time the stopwatch has been running.
           time_label (tk.Label): The label displaying the current time on the stopwatch.
           threshold_label (tk.Label): The label displaying the current threshold time.
           change_threshold_button (tk.Button): The button to change the threshold time.
           start_button (tk.Button): The button to start and stop the stopwatch.
           reset_button (tk.Button): The button to reset the stopwatch.
           save_info (tk.Button): The button to save the current time to an Excel file.
       """

    threshold_time = 60

    def __init__(self, main_window):

        self.GUI_window = main_window
        self.is_running = False
        self.is_mouse_tracking = False
        self.update_time_id = None
        self.start_time = None
        self.elapsed_time = 0

        self.time_label = tk.Label(main_window, text="00:00:00", font=("Helvetica", 60))
        self.time_label.pack(pady=5)

        self.threshold_label = tk.Label(main_window, text=f"Threshold: {self.threshold_time} s")
        self.threshold_label.pack(side=tk.TOP, padx=1)

        self.change_threshold_button = tk.Button(
            main_window, text="Change Threshold", command=self.change_threshold, width=15, height=2
        )
        self.change_threshold_button.pack(side=tk.LEFT, padx=10)

        self.start_button = tk.Button(
            main_window, text="Start Track", command=self.toggle_mouse_tracking_and_start_stopwatch, width=10, height=2
        )
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(
            main_window,
            text="Reset",
            command=self.reset_stopwatch,
            state=tk.DISABLED,
            width=10,
            height=2,
        )
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.save_info = tk.Button(
            main_window, text="Save Time", command=self.save_time, width=10, height=2
        )
        self.save_info.pack(side=tk.LEFT, padx=10)

    """
        Methods:
        mouse_tracking(): Tracks mouse movement and controls the stopwatch based on whether or not the mouse moves. Uses the pyautogui library.
        change_threshold(): Changes the threshold time based on user input. Uses the tk.simpledialog library.
        toggle_mouse_tracking(): Toggles mouse tracking on and off. Uses the threading library.
        start_stopwatch(): Starts or stops the stopwatch. Uses the tkinter library.
        toggle_mouse_tracking_and_start_stopwatch(): Toggles mouse tracking and starts or stops the stopwatch. Uses the threading and tkinter libraries.
        update_time(): Updates the elapsed time of the stopwatch. Uses the tkinter library.
        display_time(): Formats and displays the elapsed time of the stopwatch. Uses the tkinter library.
        reset_stopwatch(): Resets the stopwatch. Uses the tkinter library.
        save_time(): Saves the current time of the stopwatch to an Excel file. Uses the openpyxl and tkinter.filedialog libraries.
        """
    def mouse_tracking(self):
        prev_position = None
        position_time = None

        while self.is_mouse_tracking:
            # Get the current mouse position
            position = pyautogui.position()

            if position == prev_position:

                if time.time() - position_time > self.threshold_time:

                    if self.is_running:

                        self.start_stopwatch()
            else:

                if not self.is_running:

                    self.start_stopwatch()

                prev_position = position
                position_time = time.time()
            # Force update the label in the GUI
            self.GUI_window.update()
            # Add a small delay to reduce CPU usage
            time.sleep(0.01)

    def change_threshold(self):
        new_threshold = simpledialog.askinteger(
            "Change Threshold Time",
            "Enter new threshold time (seconds):",
            initialvalue=self.threshold_time,

        )
        if new_threshold is not None:

            self.threshold_time = new_threshold
            self.threshold_label.config(text=f"Threshold: {self.threshold_time} s")

    def toggle_mouse_tracking(self):
        self.is_mouse_tracking = not self.is_mouse_tracking
        if self.is_mouse_tracking:

            tracking_thread = threading.Thread(target=self.mouse_tracking)
            tracking_thread.start()

        else:
            pass

    def start_stopwatch(self):
        if not self.is_running:

            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_time()
            self.start_button.config(text="Stop Track")
            self.reset_button.config(state=tk.NORMAL)
        else:
            self.is_running = False

            if self.update_time_id is not None:
                self.GUI_window.after_cancel(self.update_time_id)
                self.update_time_id = None

            self.start_button.config(text="Start Track")

    def toggle_mouse_tracking_and_start_stopwatch(self):
        self.toggle_mouse_tracking()
        self.start_stopwatch()

    def update_time(self):
        if self.is_running:

            self.elapsed_time = (
                time.time() - self.start_time
            )

            self.display_time()
            self.update_time_id = self.GUI_window.after(100, self.update_time)

    def display_time(self):
        # Calculate hours, minutes, and seconds
        hours = int(
            self.elapsed_time // 3600
        )
        minutes = int(
            self.elapsed_time % 3600 // 60
        )
        seconds = int(
            self.elapsed_time % 60
        )

        # Format the time as a string and update the label
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        self.time_label.config(text=time_str)

    def reset_stopwatch(self):
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0
        self.display_time()
        self.start_button.config(text="Start")
        self.reset_button.config(state=tk.DISABLED)

    def save_time(self):
        current_date = date.today()
        date_string = current_date.strftime("%d-%m-%Y")
        session_time = self.elapsed_time
        session_string = time.strftime("%H:%M:%S", time.gmtime(session_time))
        file_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel Files", "*.xlsx")],
            initialfile=f"Session_time{date_string}.xlsx"
        )

        if file_path:
            # Check if the file already exist
            try:
                workbook = openpyxl.load_workbook(file_path)
            except FileNotFoundError:
                # If the file doesn't exist, create a new workbook
                workbook = openpyxl.Workbook()

            sheet = workbook.active
            sheet.append([date_string, session_string])
            workbook.save(file_path)
