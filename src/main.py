import sys
from widget import ExtensionRenamerApp
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = ExtensionRenamerApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()