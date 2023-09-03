from renamer import Renamer
from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFileDialog, QMessageBox, QSizePolicy, QSpacerItem, QHBoxLayout, QFrame
from PyQt6.QtGui import QAction, QIcon

class ExtensionRenamerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 150)
        self.setWindowTitle("Extension Renamer")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        widget = QFrame()
        widget.setFrameShape(QFrame.Shape.StyledPanel)
        widget.setFrameShadow(QFrame.Shadow.Raised)
        widget.setLineWidth(2)
        widget.setMidLineWidth(2)
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

        #OLD EXTENSION LABEL AND INPUT FIELDS
        old_extention = QHBoxLayout()
        old_extention.setSpacing(10)
        self.old_extension_label = QLabel("Old Extension:")
        old_extention.addWidget(self.old_extension_label)
        self.old_extension_input = QLineEdit(self)
        old_extention.addWidget(self.old_extension_input)
        self.layout.addLayout(old_extention)

        #NEW EXTENSION LABEL AND INPUT FIELDS
        new_extension = QHBoxLayout()
        new_extension.setSpacing(5)
        self.new_extension_label = QLabel("New Extension:")
        new_extension.addWidget(self.new_extension_label)
        self.new_extension_input = QLineEdit(self)
        new_extension.addWidget(self.new_extension_input)
        self.layout.addLayout(new_extension)

        #ADDING SPACE
        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        self.layout.addItem(spacer)

        # BUTTONS
        button_layout = QHBoxLayout()

        self.add_files_button = QPushButton("Add Files")
        self.add_files_button.setFixedSize(100, 30)
        self.add_files_button.clicked.connect(self.add_files)
        button_layout.addWidget(self.add_files_button) # add the frame containing the button to the button layout

        self.rename_button = QPushButton("Rename Files")
        self.rename_button.setFixedSize(100, 30)
        self.rename_button.clicked.connect(self.rename_files)
        button_layout.addWidget(self.rename_button)

        # Add the button_layout to the main layout
        self.layout.addLayout(button_layout)

        # MENU BAR
        menu_bar = self.menuBar()

        # File menu
        file_menu = menu_bar.addMenu("&File")
        about_action = QAction(QIcon("src\icons\info (1).svg"), "About", self)
        file_menu.addAction(about_action)
        about_action.triggered.connect(self.show_about)
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.close)

        # View menu
        view_menu = menu_bar.addMenu("&View")
        fullscreen_action = QAction(QIcon("src\icons\info (1).svg"), "Fullscreen", self)
        fullscreen_action.triggered.connect(self.toggle_fullscreen)
        view_menu.addAction(fullscreen_action)

        self.file_paths = []

# CUSTOM SLOTS

    def show_about(self):
        about_dialog = QMessageBox()
        about_dialog.setIcon(QMessageBox.Icon.Information)
        about_dialog.setWindowTitle("About")
        about_text = (
        "<strong style='font-size: 16px;'>Extension Renamer Application</strong><br>"
        "Version 1.0<br><br>"
        "Created by ken"
        )
        about_dialog.setText(about_text)
        about_dialog.setStandardButtons(QMessageBox.StandardButton.Close)
        about_dialog.exec()

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def add_files(self):
        self.file_paths.clear()
        files, _ = QFileDialog.getOpenFileNames(self, "Select Files to Rename", "", "All Files (*);;Text Files (*.txt)")
        self.file_paths.extend(files)

    def rename_files(self):
        old_extension = self.old_extension_input.text()
        new_extension = self.new_extension_input.text()

        if not old_extension or not new_extension:
            message = (
                "<strong style='font-size: 14px;'>Please provide both old and new extensions.</strong><br>"
            )
            self.show_error_message(message)
            return

        renamer = Renamer(old_extension, new_extension)
        renamed_files = renamer.rename_files(self.file_paths)

        if renamed_files:
            # self.show_info_message("Renaming completed.\n\nRenamed Files:\n\n" + "\n".join(renamed_files))
            message = (
            "<strong style='font-size: 14px;'>Renaming completed.</strong><br><br>"
            "<em>Renamed Files:</em><br>"
            "<ul>"
        )
            message += "\n".join(f"<li>{file}</li>" for file in renamed_files)
            message += "</ul>"

            self.show_info_message(message)
            # Clear the input fields after renaming is done
            self.old_extension_input.clear()
            self.new_extension_input.clear()
        else:
            self.show_info_message("No files were renamed.")

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.exec()

    def show_info_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Information")
        msg_box.setText(message)
        msg_box.exec()