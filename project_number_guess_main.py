from PyQt6 import QtWidgets
from gui import Ui_MainWindow
from project_number_guess import NumberGuess


class NumberGuessApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        """user has to enter their name and click New Game in order to start the game"""
        self.game = None

        """connect buttons to methods"""
        self.ui.submit_button.clicked.connect(self.submit_guess)
        self.ui.new_game_button.clicked.connect(self.start_new_game)

        self.update_ui(started=False)

    def submit_guess(self):
        """handle guess submission."""
        if not self.game:
            self.ui.feedback_label.setText("Start a new game first!")
            return

        try:
            guess = int(self.ui.guess_input.text())
            if not self.game.min_num <= guess <= self.game.max_num:
                self.ui.feedback_label.setText(
                    f"Enter a number between {self.game.min_num} and {self.game.max_num}."
                )
                return
            feedback = self.game.check_guess(guess)
            self.ui.feedback_label.setText(feedback)
            self.ui.attempts_label.setText(f"Attempts: {self.game.attempts}")
            if feedback == "Correct!":
                name = self.ui.name_input.text()
                self.game.save_high_score(name)
                self.display_high_scores()
        except ValueError:
            self.ui.feedback_label.setText("Please enter a valid number.")

    def start_new_game(self):
        """start a new game with a specific range after validating the name input."""
        name = self.ui.name_input.text().strip()
        if not name:
            QtWidgets.QMessageBox.warning(self, "Name Required", "Please enter your name to start the game.")
            return

        min_num, max_num = 1, 100  # Default range
        self.game = NumberGuess(min_num, max_num)
        self.update_ui(started=True)

    def update_ui(self, started: bool):
        """update the UI based on if the game has started."""
        if not started:
            self.ui.feedback_label.setText("Enter your name and start a new game.")
            self.ui.attempts_label.setText("Attempts: 0")
            self.ui.high_scores_label.setText("High Scores:")
            self.ui.guess_input.clear()
        else:
            self.ui.feedback_label.setText(
                f"Guess a number between {self.game.min_num} and {self.game.max_num}"
            )
            self.ui.attempts_label.setText("Attempts: 0")
            self.ui.guess_input.clear()
            self.display_high_scores()

    def display_high_scores(self):
        """display the high scores"""
        scores = self.game.load_high_scores()
        high_scores = "\n".join(
            [f"{name}: {attempts}" for name, attempts in scores.items()]
        )
        self.ui.high_scores_label.setText(f"High Scores:\n{high_scores}")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = NumberGuessApp()
    main_window.show()
    sys.exit(app.exec())
