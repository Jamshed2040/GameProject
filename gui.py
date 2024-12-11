from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Feedback label
        self.feedback_label = QtWidgets.QLabel(self.centralwidget)
        self.feedback_label.setGeometry(QtCore.QRect(50, 20, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.feedback_label.setFont(font)
        self.feedback_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.feedback_label.setObjectName("feedback_label")
        self.feedback_label.setText("Guess a number between 1 and 100")  # Set text directly

        # Guess input
        self.guess_input = QtWidgets.QLineEdit(self.centralwidget)
        self.guess_input.setGeometry(QtCore.QRect(150, 70, 100, 30))
        font.setPointSize(10)
        self.guess_input.setFont(font)
        self.guess_input.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.guess_input.setObjectName("guess_input")

        # Submit button
        self.submit_button = QtWidgets.QPushButton(self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(150, 110, 100, 30))
        self.submit_button.setObjectName("submit_button")
        self.submit_button.setText("Submit")  # Set text directly

        # Attempts label
        self.attempts_label = QtWidgets.QLabel(self.centralwidget)
        self.attempts_label.setGeometry(QtCore.QRect(50, 150, 300, 20))
        font.setPointSize(10)
        self.attempts_label.setFont(font)
        self.attempts_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.attempts_label.setObjectName("attempts_label")
        self.attempts_label.setText("Attempts: 0")  # Set text directly

        # High scores label
        self.high_scores_label = QtWidgets.QLabel(self.centralwidget)
        self.high_scores_label.setGeometry(QtCore.QRect(50, 180, 300, 100))
        font.setPointSize(10)
        self.high_scores_label.setFont(font)
        self.high_scores_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        self.high_scores_label.setObjectName("high_scores_label")
        self.high_scores_label.setText("High Scores:")  # Set text directly

        # Name input
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setGeometry(QtCore.QRect(50, 300, 150, 30))
        font.setPointSize(10)
        self.name_input.setFont(font)
        self.name_input.setPlaceholderText("Enter your name")  # Set placeholder text directly
        self.name_input.setObjectName("name_input")

        # New game button
        self.new_game_button = QtWidgets.QPushButton(self.centralwidget)
        self.new_game_button.setGeometry(QtCore.QRect(250, 300, 100, 30))
        self.new_game_button.setObjectName("new_game_button")
        self.new_game_button.setText("New Game")  # Set text directly

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
