from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QGridLayout, QMainWindow)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import os
from loudness_analyzer import analyze_loudness  # Import from loudness_analysis.py

# Thread for running the analysis
class AnalysisThread(QThread):
    analysis_done = pyqtSignal(float, dict)  # Signal emitted when analysis is complete

    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        try:
            # Run the loudness analysis in this thread
            result = analyze_loudness(self.file_path)
            if result is not None:
                loudness_lufs, penalties = result
                self.analysis_done.emit(loudness_lufs, penalties)
            else:
                self.analysis_done.emit(None, {})
        except Exception as e:
            print(f"Error in analysis thread: {e}")
            self.analysis_done.emit(None, {})

# PyQt5 UI
class LoudnessMeterUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Loudness Meter")
        self.analysis_thread = None

        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Upload Button
        self.upload_button = QPushButton("Upload Audio")
        self.upload_button.clicked.connect(self.upload_file)
        self.layout.addWidget(self.upload_button)

        # Drag and Drop Label
        self.drag_drop_label = QLabel("Drag and Drop Audio Here")
        self.drag_drop_label.setAlignment(Qt.AlignCenter)
        self.drag_drop_label.setStyleSheet("border: 2px dashed #aaa; padding: 20px;")
        self.layout.addWidget(self.drag_drop_label)
        self.setAcceptDrops(True)  # Enable drag and drop

        # Result Label
        self.result_label = QLabel("No analysis yet")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.result_label)

        # Grid for showing penalties
        self.penalty_grid = QGridLayout()
        self.layout.addLayout(self.penalty_grid)

        # Export Button
        self.export_button = QPushButton("Export Results")
        self.export_button.clicked.connect(self.export_results)
        self.layout.addWidget(self.export_button, alignment=Qt.AlignRight)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        try:
            urls = event.mimeData().urls()
            if urls:
                file_path = urls[0].toLocalFile()
                self.process_audio_file(file_path)
        except Exception as e:
            print(f"Error during drag and drop: {e}")

    def upload_file(self):
        try:
            file_dialog = QFileDialog(self)
            file_dialog.setOption(QFileDialog.DontUseNativeDialog, True)  # Use non-native file dialog
            file_path, _ = file_dialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.wav *.mp3 *.flac)")
            if file_path:
                self.process_audio_file(file_path)
        except Exception as e:
            print(f"Error during file upload: {e}")

    def process_audio_file(self, file_path):
        try:
            self.result_label.setText("Analyzing...")

            # Start the analysis thread
            self.analysis_thread = AnalysisThread(file_path)
            self.analysis_thread.analysis_done.connect(self.show_analysis)
            self.analysis_thread.start()

            self.drag_drop_label.setText('File uploaded: ' + os.path.basename(file_path))
        except Exception as e:
            print(f"Error processing audio file: {e}")

    def show_analysis(self, loudness_lufs, penalties):
        try:
            if loudness_lufs is not None:
                self.result_label.setText(f"LUFS: {loudness_lufs:.2f}")

                # Clear penalty grid
                while self.penalty_grid.count():
                    item = self.penalty_grid.takeAt(0)
                    widget = item.widget()
                    if widget:
                        widget.deleteLater()

                # Update grid with penalties
                for i, (platform, penalty) in enumerate(penalties.items()):
                    label = QLabel(f"{platform}: {penalty:.2f} dB")  # Penalty as negative value
                    self.penalty_grid.addWidget(label, i, 0)
            else:
                self.result_label.setText("Error analyzing audio.")
        except Exception as e:
            print(f"Error displaying analysis: {e}")

    def export_results(self):
        try:
            file_dialog = QFileDialog(self)
            save_path, _ = file_dialog.getSaveFileName(self, "Save Results", "", "Text Files (*.txt)")
            if save_path:
                with open(save_path, 'w') as f:
                    f.write(f"{self.result_label.text()}\n\n")
                    for i in range(self.penalty_grid.count()):
                        widget = self.penalty_grid.itemAt(i).widget()
                        if widget:
                            f.write(widget.text() + '\n')
        except Exception as e:
            print(f"Error exporting results: {e}")
