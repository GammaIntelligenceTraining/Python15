import tkinter as tk
import random

# List of words to choose from
word_list = ['python', 'hangman', 'tkinter', 'programming']

# Select a random word from the list
chosen_word = random.choice(word_list)
hidden_word = ['_' for _ in chosen_word]  # To display _ for the chosen word
attempts_left = 6  # Number of wrong attempts allowed
guessed_letters = []


def submit_guess():
    global attempts_left
    
    letter = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    if letter in guessed_letters:
        message_label.config(text="You already guessed that letter.")
        return
    
    guessed_letters.append(letter)
    
    if letter in chosen_word:
        message_label.config(text="Good guess!")
        for i, l in enumerate(chosen_word):
            if l == letter:
                hidden_word[i] = letter
    else:
        attempts_left -= 1
        message_label.config(text=f"Wrong guess! You have {attempts_left} attempts left.")
    
    word_label.config(text=" ".join(hidden_word))
    lives_label.config(text=f"Lives: {attempts_left}")
    
    # Check if the game is won or lost
    if "_" not in hidden_word:
        message_label.config(text="Congratulations, you won!")
        guess_button.config(state=tk.DISABLED)
    elif attempts_left == 0:
        message_label.config(text=f"You lost! The word was '{chosen_word}'.")
        guess_button.config(state=tk.DISABLED)

# Setup the Tkinter window
root = tk.Tk()
root.title("Hangman Game")

# Labels and entry field
word_label = tk.Label(root, text=" ".join(hidden_word), font=('Helvetica', 20))
word_label.pack(pady=10)

guess_entry = tk.Entry(root)
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", command=submit_guess)
guess_button.pack(pady=10)

message_label = tk.Label(root, text="")
message_label.pack(pady=10)

lives_label = tk.Label(root, text=f"Lives: {attempts_left}")
lives_label.pack(pady=10)

# Start the main event loop
root.mainloop()