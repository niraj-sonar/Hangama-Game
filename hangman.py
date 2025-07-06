import random
import tkinter as tk
from tkinter import messagebox

def select_word(difficulty):
    words = {
        "easy": {"cat": "A common pet", "dog": "Man's best friend", "bat": "A flying mammal",
                 "sun":"The star at the center of our solar system", "moon":"Earth's natural satellite,visible at night"},
        "medium": {"python": "A popular programming language", "developer": "A person who writes software", 
                   "hangman": "A classic word-guessing game"},
        "hard": {"algorithm": "A step-by-step procedure for calculations","encyclopedia": "A book or set of books with information on many subjects",
                 "biochemistry":"The study of chemical processes in living organisms", "architecture":"The art and science of designing buildings"}
    }
    word, hint = random.choice(list(words[difficulty].items()))
    return word, hint

def initialize_game(word):
    return {
        "word": word,
        "hidden_word": ["_"] * len(word),
        "guessed_letters": set(),
        "attempts_left": 6,
        "score": 0
    }

def process_guess(game_state, guess):
    word = game_state["word"]
    hidden_word = game_state["hidden_word"]
    guessed_letters = game_state["guessed_letters"]
    
    if guess in guessed_letters:
        return game_state, "Already guessed!"
    
    guessed_letters.add(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        game_state["score"] += 10  # Increase score for correct guess
        return game_state, "Correct guess!"
    else:
        game_state["attempts_left"] -= 1
        game_state["score"] -= 5  # Deduct score for wrong guess
        return game_state, "Wrong guess!"

def update_display():
    word_label.config(text=" ".join(game_state["hidden_word"]))
    attempts_label.config(text=f"Attempts left: {game_state['attempts_left']}")
    score_label.config(text=f"Score: {game_state['score']}")

def make_guess():
    guess = entry.get().lower()
    entry.delete(0, tk.END)
    if len(guess) != 1 or not guess.isalpha():
        messagebox.showwarning("Invalid Input", "Enter a single letter.")
        return
    
    global game_state
    game_state, message = process_guess(game_state, guess)
    messagebox.showinfo("Result", message)
    update_display()
    
    if "_" not in game_state["hidden_word"]:
        celebrate_victory()
    elif game_state["attempts_left"] == 0:
        messagebox.showinfo("Game Over", f"Game over! The word was '{game_state['word']}'.\nFinal Score: {game_state['score']}")
        root.quit()

def celebrate_victory():
    celebration_window = tk.Toplevel(root)
    celebration_window.title("Congratulations!")
    celebration_window.geometry("300x200")
    tk.Label(celebration_window, text="🎉 Congratulations! You won! 🎉", font=("Arial", 14)).pack(pady=20)
    tk.Label(celebration_window, text=f"Final Score: {game_state['score']}").pack(pady=10)
    tk.Button(celebration_window, text="Close", command=root.quit).pack(pady=20)

def start_game():
    global game_state
    difficulty = difficulty_var.get()
    word, hint = select_word(difficulty)
    game_state = initialize_game(word)
    hint_label.config(text=f"Hint: {hint}")
    update_display()

root = tk.Tk()
root.title("Hangman Game")

difficulty_var = tk.StringVar(value="easy")

tk.Label(root, text="Choose Difficulty:").pack()
tk.Radiobutton(root, text="Easy", variable=difficulty_var, value="easy").pack()
tk.Radiobutton(root, text="Medium", variable=difficulty_var, value="medium").pack()
tk.Radiobutton(root, text="Hard", variable=difficulty_var, value="hard").pack()



tk.Button(root, text="Start Game", command=start_game).pack()

hint_label = tk.Label(root, text="")
hint_label.pack()
word_label = tk.Label(root, text="")
word_label.pack()
attempts_label = tk.Label(root, text="")
attempts_label.pack()
score_label = tk.Label(root, text="")
score_label.pack()

entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Guess", command=make_guess).pack()

root.mainloop()


