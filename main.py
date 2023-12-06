import tkinter as tk
import pandas as pd
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("French Flashcard App")

        # Load data from CSV
        self.flashcard_data = pd.read_csv("data/french_words.csv")

        # Initialize variables
        self.current_card = None

        # Create UI elements
        self.label = tk.Label(root, font=('Arial', 24), height=5, width=30, relief='solid')
        self.label.pack(pady=20)

        # Create buttons
        self.show_button = tk.Button(root, text="Show Answer", command=self.show_answer)
        self.next_button = tk.Button(root, text="Next Card", command=self.next_card)

        self.show_button.pack(side="left", padx=10)
        self.next_button.pack(side="right", padx=10)

        # Load the first card
        self.next_card()

    def next_card(self):
        # Get a random row from the dataframe
        self.current_card = self.flashcard_data.sample()

        # Display the French word on the label
        self.label.config(text=self.current_card["French"].values[0])

        # Enable the "Show Answer" button
        self.show_button.config(state="normal")

    def show_answer(self):
        # Replace the French word with the English translation on the label
        english_translation = self.current_card["English"].values[0]
        self.label.config(text=english_translation)

        # Disable the "Show Answer" button after showing the answer
        self.show_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
