'''
Simple PyQt5 app with a table to display submitted names.
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem

'''
QApplication - manages the GUI and needed for every PyQt App. ALWAYS import
QWidget - base class for all UI elements
QLabel - display static text
QLineEdit - Text input/entry
QPushButton - clickable putton
QVBoxLayout - layour mmanagement and arranges widgets vertically
QMessageBox - Pop up box to give users info
QTableWidget - a table widget that lets you show data in rows and columns
QTableWidgetItem - an item (cell) inside the table (text, icons, etc.)
'''


# Base class for OOP approach, inherit from QWidget so we are a type of QWidget
class PyQtApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Table App")     # App name
        self.setGeometry(100,100, 400, 200)     # Set size for our window (horizontal of widget on the screen, vertical of widget on the screen, width of widget, height of widget in pixels)
        
        # Set background color of window
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f9fc;
            }
            QLabel {
                color: #003366;
                font-size: 14px;
            }
            QLineEdit {
                border: 2px solid #007BFF;
                border-radius: 5px;
                padding: 8px;
                font-size: 14px;
            }
            QPushButton {
                background-color: #007BFF;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QTableWidget {
                background-color: white;
                border: 2px solid #007BFF;
                border-radius: 5px;
                gridline-color: #dcdcdc;
                font-size: 14px;
                selection-background-color: #007BFF;
                selection-color: white;
            }
            QHeaderView::section {
                background-color: #007BFF;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
        """
        )
        
        
        self.init_ui()                          # Call our method to create the widgets and layout    

    # Create all of our widgets and layout
    def init_ui(self):
        layout = QVBoxLayout()          # Create the layout

        # Label + input field
        self.label = QLabel("Enter your name: ", self)     # Display text in the main window
        layout.addWidget(self.label)                         # Need to add widget to our layour

        self.text_field = QLineEdit()                  # Place it in the window
        self.text_field.setPlaceholderText("Type your name here...")     # Place holder text
        layout.addWidget(self.text_field)

        # Submit button
        self.submit_button = QPushButton("Submit", self)      # This is the text, and this is the window it should be associated with
        self.submit_button.clicked.connect(self.submit_action)          # Buttons clicked, connect, connect to submit action function
        layout.addWidget(self.submit_button)

        # Quit button
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.close)         # Built in method to close the window when clicked.
        layout.addWidget(self.quit_button)

        # Table to show submitted names
        self.table = QTableWidget(0, 1)  # 0 rows, 1 column
        self.table.setHorizontalHeaderLabels(["Names"])
        layout.addWidget(self.table)

        self.setLayout(layout)                        # Need to associate the layout with the window


    def submit_action(self):
        user_input = self.text_field.text().strip()          # getter for text, then strip all white space from this string
        if user_input:
            # Add the name to the table
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(user_input))
            
            # Show confirmation popup
            QMessageBox.information(self, "Success", "Successfully submitted")

            # Clear the input field after submission
            self.text_field.clear()  
        else:
            # Warning if user puts no input
            QMessageBox.warning(self, "No Input", "Please enter your name.")      






if __name__ == "__main__":
    app = QApplication(sys.argv)                    # Initializes application
    window = PyQtApp()                              # Create instance of our class
    window.show()                                   # Show method to run app

    sys.exit(app.exec())                            # sys.exit to exit app
