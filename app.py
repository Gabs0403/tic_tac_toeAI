import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QGridLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import random
import time



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic Tac Toe")
        self.showMaximized()

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.menu()

    def menu(self):
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
        btn_easy = QPushButton("Easy 🤓 ")
        btn_easy.setFixedSize(200, 60)
        btn_easy.clicked.connect(lambda: self.initializeBoard("Easy"))

        btn_impossible = QPushButton("Impossible 🔥")
        btn_impossible.setFixedSize(200, 60)
        btn_impossible.clicked.connect(lambda: self.initializeBoard("Impossible"))

        btn_easy.setObjectName("btn_easy")
        btn_impossible.setObjectName("btn_impossible")


        buttons_layout = QHBoxLayout()

        buttons_layout.setContentsMargins(50, 20, 50, 20)
        buttons_layout.addWidget(btn_easy)
        buttons_layout.addWidget(btn_impossible)


        # Add widgets to vertical layout (all centered)
        
        vertical_layout.addStretch(1)
        vertical_layout.addWidget(label_question, alignment=Qt.AlignCenter)
        vertical_layout.addWidget(label_difficulty, alignment=Qt.AlignCenter)
        vertical_layout.addLayout(buttons_layout)

        # images
        
        robot_img = QLabel()
        robot_pixmap = QPixmap("robot.png")  # 👈 replace with your robot image path
        robot_pixmap = robot_pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        robot_img.setPixmap(robot_pixmap)
        robot_img.setAlignment(Qt.AlignCenter)

        board_img = QLabel()
        board_pixmap = QPixmap("tic tac toe.png")  # 👈 replace with your tic tac toe board image path
        board_pixmap = board_pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        board_img.setPixmap(board_pixmap)
        board_img.setAlignment(Qt.AlignCenter)

        images_layout = QHBoxLayout()

        images_layout.addWidget(board_img, alignment=Qt.AlignCenter)
        images_layout.addWidget(robot_img, alignment=Qt.AlignCenter)
        images_layout.setSpacing(30)

        vertical_layout.addLayout(images_layout)

        vertical_layout.addStretch(2) 

        # Center the vertical layout in outer layout
        outer_layout.addLayout(vertical_layout)

        outer_layout.setAlignment(Qt.AlignCenter)

        # Assign layout to central widget
        self.central_widget.setLayout(outer_layout)

        # Apply styles
        self.setStyleSheet("""
                QMainWindow {
                    background: qlineargradient(
                        x1:0, y1:0, x2:0, y2:1,
                        stop:0 #24D2F9, stop:1 #187bcd
                    );
                    font-family: 'Segoe UI';
                }

                QLabel {
                    font-size: 48px;
                    font-weight: bold;
                    color: #ffffff;
                    text-align: center;
                }

                QLabel#label_difficulty {
                    font-size: 22px;
                    color: #f1f1f1;
                }

                QPushButton#btn_easy, QPushButton#btn_impossible {
                    background-color: #FFC31F;
                    color: #222222;
                    font-size: 20px;
                    font-weight: bold;
                    border-radius: 15px;
                    padding: 12px;
                    min-width: 220px;
                    min-height: 60px;
                }

                QPushButton#btn_easy:hover, QPushButton#btn_impossible:hover {
                    background-color: #FFD84D;
                }

                QPushButton#btn_easy:pressed, QPushButton#btn_impossible:pressed {
                    background-color: #E6AC00;
                }
            """)
        
        self.game_state = {
            "board": [
                        ["", "", ""],
                        ["", "", ""],
                        ["", "", ""]
                    ],
            "current_player": "",
            "difficulty": "",
            "status": ""
        }
    

    
    def initializeBoard(self, difficulty):
        
        self.game_state["difficulty"] = difficulty

        # Clear the old central widget (menu)
        self.takeCentralWidget()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Main layout
        board_layout = QVBoxLayout()
        board_layout.setAlignment(Qt.AlignCenter)

        # Container for the grid
        grid_container = QWidget()
        grid_container.setFixedSize(540, 540)  # 3x3 * 120px
        grid_layout = QGridLayout(grid_container)
        grid_layout.setSpacing(0)  
        grid_layout.setContentsMargins(0, 0, 0, 0)

        self.board_buttons = []

        for row in range(3):
            for col in range(3):
                button = QPushButton("O")
                button.setFixedSize(180, 180)
                button.clicked.connect(self.handleClick)
                button.setObjectName(f"cell_{row}_{col}")  # unique ID for styling
                grid_layout.addWidget(button, row, col)
                
                self.board_buttons.append(button)

        board_layout.addWidget(grid_container, alignment=Qt.AlignCenter)

        self.central_widget.setLayout(board_layout)

        #  Apply styles for the BOARD
        self.central_widget.setStyleSheet("""
        QWidget {
            background: #f4f4f9;  /* same for window and board background */
        }

        QPushButton {
            background-color: #f4f4f9;  /* same as background */
            font-size: 120px;
            font-weight: bold;
            color: #3F5977;
            border: 1px solid black;  /* remove all borders first */
        }

        /* Top row */
        QPushButton#cell_0_0, QPushButton#cell_0_1, QPushButton#cell_0_2 {
            border-bottom: 3px solid black;
        }

        /* Middle row */
        QPushButton#cell_1_0, QPushButton#cell_1_1, QPushButton#cell_1_2 {
            border-top: 3px solid black;
            border-bottom: 3px solid black;
        }

        /* Bottom row */
        QPushButton#cell_2_0, QPushButton#cell_2_1, QPushButton#cell_2_2 {
            border-top: 3px solid black;
        }

        /* Left column */
        QPushButton#cell_0_0, QPushButton#cell_1_0, QPushButton#cell_2_0 {
            border-right: 3px solid black;
        }

        /* Middle column */
        QPushButton#cell_0_1, QPushButton#cell_1_1, QPushButton#cell_2_1 {
            border-left: 3px solid black;
            border-right: 3px solid black;
        }

        /* Right column */
        QPushButton#cell_0_2, QPushButton#cell_1_2, QPushButton#cell_2_2 {
            border-left: 3px solid black;
        }
    """)

        
        list_players = ["Player", "AI"]

        # self.game_state = startGame(difficulty, random.choice(list_players))
    
    def handleClick(self):
        if(self.game_state["current_player"] == "AI"):
            return
        self.changeStateAllButtons(False)
        # self.game_state = applyMove(self.game_state, button.row, button.col)
        self.update_board(self.game_state["board"])
        time.sleep(2)
        # self.game_state = AI_move(self.game_state)
        self.update_board(self.game_state["board"])
        self.changeStateAllButtons(True)

    def changeStateAllButtons(self, enabled: bool):
        for button in self.board_buttons:
            button.setEnabled(enabled)


    def update_board(self, board):
        #Disable 
        
        pass







# Run app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
