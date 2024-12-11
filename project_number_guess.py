import random
import json
from typing import Dict


class NumberGuess:
    def __init__(self, min_num: int = 1, max_num: int = 100):
        """
        initialize a new game with a specific range.
        """

        self.min_num = min_num
        self.max_num = max_num
        self.reset_game()
        self.high_scores_file = "high_scores.json"

    def reset_game(self):
        """start a new game by generating a new target number."""
        self.target = random.randint(self.min_num, self.max_num)
        self.attempts = 0

    def check_guess(self, guess: int) -> str:
        """
        check if the guess is correct, too high, or too low.
        """
        self.attempts += 1
        if guess < self.target:
            return "Too Low"
        elif guess > self.target:
            return "Too High"
        else:
            return "Correct!"

    def save_high_score(self, name: str):
        """save the high score to a file"""
        try:
            scores = self.load_high_scores()
            scores[name] = min(scores.get(name, float("inf")), self.attempts)
            with open(self.high_scores_file, "w") as file:
                json.dump(scores, file)
        except Exception as e:
            print(f"Error saving high score: {e}")

    def load_high_scores(self) -> Dict[str, int]:
        """load high scores from a file."""
        try:
            with open(self.high_scores_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error loading high scores: {e}")
            return {}
