# MouseActivityStopwatch
I am a professional poker player, and currently, I specialize in Pot Limit Omaha. I had significant difficulties in assessing my overall work time during the day while playing on various poker rooms/applications, each with its unique settings. Opening tables sometimes involved long waits for willing players (sometimes even hours, depending on the stakes). That's why I created a stopwatch that utilizes mouse activity to track time. Thanks to it, I can see my actual playing time at the end of the day and record the amount of time to monitor my weekly goals.

This is my first project created in Python, which, despite numerous challenges I encountered, made me fall in love with programming. While developing additional features for the stopwatch, I had to seek knowledge from various sources, such as official documentation, YouTube tutorials explaining library functionality, questions on Stack Overflow, and many hours of collaboration with ChatGPT, which served as my virtual mentor, helping me better understand certain functions and optimize code and its descriptions.

## Widgets
1. Change Threshold: Clicking this button will open a window where you can change the time threshold, expressed in seconds. You can also modify the threshold while the timer is running, without affecting the current time measurement. The stopwatch will continue to function, and the new threshold value will be applied from that moment.

2. Start Tracking: Clicking this button will initiate the tracking of mouse movements by the stopwatch, and it will count time until the specified threshold is reached.

3. Reset: This option allows you to reset the elapsed time on the stopwatch.

4. Save Time: Here, you can save (or create if the file doesn't exist) a file in XLS format. This file will record the currently elapsed time in the tracker and append the current date in the format dd-mm-yy. You can overwrite an existing file, and the new data will be added to columns A:B without overwriting any previously entered data.



## Libraries Used

- [Tkinter](https://docs.python.org/3/library/tkinter.html): Tkinter is Python's standard GUI (Graphical User Interface) package.

- [Time](https://docs.python.org/3/library/time.html): The `time` module provides various time-related functions.

- [Datetime](https://docs.python.org/3/library/datetime.html): The `datetime` module is used for working with dates and times.

- [Openpyxl](https://openpyxl.readthedocs.io/en/stable/): Openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm/xltx/xltm files.

- [Pyautogui](https://pyautogui.readthedocs.io/en/latest/): PyAutoGUI is a Python module to programmatically control the mouse and keyboard.

- [Threading](https://docs.python.org/3/library/threading.html): The `threading` module is used for multi-threading in Python.

For more information about each library, please refer to the linked documentation.

## Future Features

Standalone RNG: RNG will be a random number generator that will be useful for individuals who employ GTO (Game Theory Optimal) in their gameplan
