# Import the tkinter and time modules
import tkinter as tk
import time

# Define a function to update the time
def update_time():
  # Get the current time in HH:MM:SS format
  current_time = time.strftime("%H:%M:%S")
  # Display the time on the label
  time_label.config(text=current_time)
  # Call the function again after 1 second
  root.after(1000, update_time)

# Create the root window
root = tk.Tk()
# Set the title of the window
root.title("Digital Clock")
# Set the size of the window
root.geometry("200x100")
# Set the background color of the window
root.config(bg="black")

# Create a label to display the time
time_label = tk.Label(root, font=("Arial", 40), fg="white", bg="black")
# Place the label at the center of the window
time_label.pack(anchor="center")

# Call the update_time function
update_time()

# Start the main loop
root.mainloop()
