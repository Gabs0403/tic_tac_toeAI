import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic Tac Toe")
        self.showMaximized()  # Start maximized
        self.setFixedSize(self.geometry().width(), self.geometry().height())

        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Outer layout (horizontal, centers everything)
        outer_layout = QHBoxLayout()

        # Inner layout (vertical, actual content)
        vertical_layout = QVBoxLayout()
        vertical_layout.setSpacing(20)  # spacing between widgets

        # Labels
        label_question = QLabel("Can you defeat me?")
        label_difficulty = QLabel("Select a difficulty:")
        label_difficulty.setObjectName("label_difficulty")

        # Buttons
        btn_easy = QPushButton("Easy")
        btn_easy.setFixedSize(200, 60)

        btn_impossible = QPushButton("Impossible")
        btn_impossible.setFixedSize(200, 60)

        # Add widgets to vertical layout (all centered)
        vertical_layout.addWidget(label_question, alignment=Qt.AlignCenter)
        vertical_layout.addWidget(label_difficulty, alignment=Qt.AlignCenter)
        vertical_layout.addWidget(btn_easy, alignment=Qt.AlignCenter)
        vertical_layout.addWidget(btn_impossible, alignment=Qt.AlignCenter)

        # Center the vertical layout in outer layout
        outer_layout.addLayout(vertical_layout)
        outer_layout.setAlignment(Qt.AlignCenter)

        # Assign layout to central widget
        central_widget.setLayout(outer_layout)

        # Apply styles
        self.setStyleSheet("""
            QMainWindow {
                background-color: #8DD9CE;
            }

            QLabel {
                font-size: 48px;
                font-weight: bold;
                color: #AC7C49;
            }

            QLabel#label_difficulty {
                font-size: 22px;
                color: #8E8B7C;
            }

            QPushButton {
                background-color: #3F5977;
                color: white;
                font-size: 20px;
                border-radius: 15px;
                padding: 12px;
                min-width: 200px;
            }
            QPushButton:hover {
                background-color: #2E455E;
            }
            QPushButton:pressed {
                background-color: #1C2D3E;
            }
        """)


# Run app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
