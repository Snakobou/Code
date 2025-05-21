import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QListWidget
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt

class StartScreen(QWidget):
    def __init__(self, switch_to_rebus_selection):
        super().__init__()
        self.switch_to_rebus_selection = switch_to_rebus_selection
        self.setWindowTitle("Мир ребусов")
        self.setGeometry(200, 200, 600, 700)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #667eea, stop:1 #764ba2);
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QLabel#titleLabel {
                font-size: 32px;
                font-weight: 700;
                margin-bottom: 20px;
                qproperty-alignment: 'AlignCenter';
                text-shadow: 2px 2px 5px rgba(0,0,0,0.5);
            }
            QPushButton {
                background-color: #9f7aea;
                border: none;
                border-radius: 30px;
                padding: 12px 35px;
                font-size: 16px;
                font-weight: 700;
                color: white;
                margin-top: 20px;
                box-shadow: 0 6px 15px rgba(159,122,234,0.6);
            }
            QPushButton:hover {
                background-color: #7c3aed;
            }
        """)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        titleLabel = QLabel("Добро пожаловать в Мир ребусов!")
        titleLabel.setObjectName("titleLabel")
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titleLabel)

        startButton = QPushButton("Начать")
        startButton.clicked.connect(lambda: self.switch_to_rebus_selection(self))
        layout.addWidget(startButton)

        self.setLayout(layout)

class RebusSelectionScreen(QWidget):
    def __init__(self, switch_to_rebus_solver):
        super().__init__()
        self.switch_to_rebus_solver = switch_to_rebus_solver
        self.setWindowTitle("Выбор ребусов")
        self.setGeometry(200, 200, 800, 600)  # Увеличиваем размеры окна
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #667eea, stop:1 #764ba2);
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QListWidget {
                font-size: 24px;  /* Увеличиваем размер шрифта */
                color: #333;
                background-color: #ffffff;
                border-radius: 10px;
            }
            QListWidget::item:hover {
                background-color: #d3d3d3;  /* Подсветка при наведении */
            }
            QPushButton {
                background-color: #9f7aea;
                border: none;
                border-radius: 30px;
                padding: 12px 35px;
                font-size: 16px;
                font-weight: 700;
                color: white;
                margin-top: 20px;
                box-shadow: 0 6px 15px rgba(159,122,234,0.6);
            }
            QPushButton:hover {
                background-color: #7c3aed;
            }
        """)

        self.rebus_data = [
            ("images/rebus1.png", "Подсказка: можно залезть", "лестница"),
            ("images/rebus2.png", "Подсказка: национальность", "русский"),
            ("images/rebus3.png", "Подсказка: можно скушать", "лимон"),
            ("images/rebus4.png", "Подсказка: можно надеть", "сапоги"),
            ("images/rebus5.png", "Подсказка: вид спорта", "футбол"),
        ]

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.rebus_list = QListWidget()
        self.rebus_list.setSpacing(10)

        # Добавляем текстовые обозначения для ребусов
        for idx in range(len(self.rebus_data)):
            self.rebus_list.addItem(f"{idx + 1} ребус")

        self.rebus_list.itemClicked.connect(self.open_rebus_solver)

        layout.addWidget(self.rebus_list, alignment=Qt.AlignmentFlag.AlignCenter)  # Центрируем список

        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignCenter)  # Центрируем кнопку "Назад"

        self.setLayout(layout)

    def open_rebus_solver(self, item):
        index = self.rebus_list.row(item)
        image_path, hint, answer = self.rebus_data[index]
        self.switch_to_rebus_solver(image_path, hint, answer)

    def go_back(self):
        self.close()
        start_screen = StartScreen(switch_to_rebus_selection)
        start_screen.show()

class RebusSolverScreen(QWidget):
    def __init__(self, image_path, hint, correct_answer, selection_window):
        super().__init__()
        self.image_path = image_path
        self.hint = hint
        self.correct_answer = correct_answer
        self.selection_window = selection_window  # Сохраняем ссылку на окно выбора
        self.setWindowTitle("Решение ребуса")
        self.setGeometry(200, 200, 600, 700)
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                            stop:0 #667eea, stop:1 #764ba2);
                color: white;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            }
            QLabel {
                font-size: 24px;
                margin-bottom: 20px;
            }
            QLineEdit {
                padding: 10px;
                font-size: 14pt;
                border-radius: 10px;
                border: none;
                font-weight: 600;
                color: #333;
            }
            QPushButton {
                background-color: #9f7aea;
                border: none;
                border-radius: 30px;
                padding: 12px 35px;
                font-size: 16px;
                font-weight: 700;
                color: white;
                margin-top: 20px;
                box-shadow: 0 6px 15px rgba(159,122,234,0.6);
            }
            QPushButton:hover {
                background-color: #7c3aed;
            }
        """)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Загружаем изображение
        image_label = QLabel()
        pixmap = QPixmap(self.image_path)
        image_label.setPixmap(pixmap.scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))  # Изменяем размер изображения
        layout.addWidget(image_label)

        hintLabel = QLabel(self.hint)
        layout.addWidget(hintLabel)

        self.answer_input = QLineEdit()
        self.answer_input.setPlaceholderText("Ваш ответ")
        layout.addWidget(self.answer_input)

        check_button = QPushButton("Проверить")
        check_button.clicked.connect(self.check_answer)
        layout.addWidget(check_button)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.go_back)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def check_answer(self):
        user_answer = self.answer_input.text().strip().lower()
        if user_answer == self.correct_answer:
            self.result_label.setText("Верно!")
            self.result_label.setStyleSheet("color: green;")
        else:
            self.result_label.setText(f"Неверно! Правильный ответ: {self.correct_answer}")
            self.result_label.setStyleSheet("color: red;")

    def go_back(self):
        self.close()
        self.selection_window.show()  # Возвращаемся к окну выбора ребусов

rebis_window = None
rebus_selection_window = None

def switch_to_rebus_selection(start_screen):
    global rebus_selection_window
    start_screen.close()
    rebus_selection_window = RebusSelectionScreen(switch_to_rebus_solver)
    rebus_selection_window.show()

def switch_to_rebus_solver(image_path, hint, correct_answer):
    global rebis_window
    rebus_selection_window.close()
    rebis_window = RebusSolverScreen(image_path, hint, correct_answer, rebus_selection_window)  # Передаем ссылку на окно выбора
    rebis_window.show()

def main():
    app = QApplication(sys.argv)

    # Создаем начальный экран
    start_screen = StartScreen(switch_to_rebus_selection)
    start_screen.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()