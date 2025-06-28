from PyQt6.QtWidgets import QApplication, QMainWindow

from src.gui_models import (
    anki_settings_model,
    shortcut_settings_model,
    tenten_parser_settings_model,
)
from src.ui_files.app_settings_window import Ui_app_settings


class MainApplication(QApplication):
    """Main application object"""

    def __init__(self, argv):
        super().__init__(argv)

        self.window = MainWindow()
        self.window.show()


class MainWindow(QMainWindow):
    """Main window object that contains the gui components"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_app_settings()
        self.ui.setupUi(self)

        self.anki_settings = anki_settings_model.AnkiSettings()
        self.tenten_settings = tenten_parser_settings_model.ParserSettings()
        self.shortcut_settings = shortcut_settings_model.ShortcutSettings()

        # TODO: connect ui elements to
