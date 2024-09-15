from PyQt5.QtWidgets import QApplication
from ui import LoudnessMeterUI  # Import from loudness_ui.py

# Main application
if __name__ == "__main__":
    app = QApplication([])
    window = LoudnessMeterUI()
    window.show()
    app.exec_()
