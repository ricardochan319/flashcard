import pandas as pd
import tkinter as tk

BACKGROUND_COLOR = "#B1DDC6"
FONT_COLOR = "black"
FONT_SIZE = 72

class FlashcardApp:
    def __init__(self, csv_file):
        self.flashcards = pd.DataFrame()
        self.current_flashcard = None
        self.csv_file = csv_file
        self.root = tk.Tk()

    def load_flashcards(self):
        """Load flashcards from the CSV file."""
        self.flashcards = pd.read_csv(self.csv_file)

    def shuffle_flashcards(self):
        """Shuffle the flashcards using random.sample."""
        self.flashcards = self.flashcards.sample(frac=1).reset_index(drop=True)

    def get_next_flashcard(self):
        """Get the next flashcard in the shuffled order."""
        if self.current_flashcard is None or len(self.flashcards) == 0:
            self.shuffle_flashcards()

        self.current_flashcard = self.flashcards.iloc[0]
        self.flashcards = self.flashcards.iloc[1:]

        return self.current_flashcard

    def reveal_english(self):
        """Reveal the English translation on the flashcard."""
        flashcard = self.get_next_flashcard()
        card_back_image = tk.PhotoImage(file="images/card_back.png")
        self.flashcard_label.config(image=card_back_image)
        self.flashcard_label.image = card_back_image
        self.flashcard_label_text.set(flashcard['English'])
        self.flashcard_label.config(compound='center', font=("Helvetica", FONT_SIZE), bg=BACKGROUND_COLOR, fg=FONT_COLOR, anchor='center')
        self.reveal_button.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def reveal_french(self):
        """Reveal the French word on the flashcard."""
        flashcard = self.get_next_flashcard()
        card_front_image = tk.PhotoImage(file="images/card_front.png")
        self.flashcard_label.config(image=card_front_image)
        self.flashcard_label.image = card_front_image
        self.flashcard_label_text.set(flashcard['French'])
        self.flashcard_label.config(compound='center', font=("Helvetica", FONT_SIZE), bg=BACKGROUND_COLOR, fg=FONT_COLOR, anchor='center')
        self.reveal_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def start_app(self):
        """Start the French Flashcard App."""
        self.root.title("French Flashcard App")
        self.root.geometry("900x650")
        self.root.configure(bg=BACKGROUND_COLOR)
        self.flashcard_label_text = tk.StringVar()
        self.flashcard_label = tk.Label(self.root, textvariable=self.flashcard_label_text, compound='center', bg=BACKGROUND_COLOR)
        self.flashcard_label.pack(pady=20)
        button_frame = tk.Frame(self.root, bg=BACKGROUND_COLOR)
        button_frame.pack(pady=5)
        self.reveal_button = tk.Button(button_frame, text="Reveal English", command=self.reveal_english, state=tk.DISABLED, bg=BACKGROUND_COLOR)
        self.reveal_button.pack(side=tk.LEFT, padx=5)
        self.next_button = tk.Button(button_frame, text="Next Flashcard", command=self.reveal_french, state=tk.NORMAL, bg=BACKGROUND_COLOR)
        self.next_button.pack(side=tk.LEFT, padx=5)
        self.load_flashcards()
        self.reveal_french()

        self.root.mainloop()

if __name__ == "__main__":
    app = FlashcardApp("data/french_words.csv")
    app.start_app()
