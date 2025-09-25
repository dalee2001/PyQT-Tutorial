'''
More Advanced PyQt5 GUI Application
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QDateEdit, QHeaderView, QHBoxLayout, QComboBox
from PyQt5.QtCore import QDate, Qt
import csv

'''
QApplication - manages the GUI and needed for every PyQt App. ALWAYS import
QWidget - base class for all UI elements (windows, panels, dialogs)
QLabel - display static text or images
QLineEdit - Text input/entry field for single-line text
QPushButton - clickable button
QVBoxLayout - layout manager that arranges widgets vertically
QHBoxLayout - layout manager that arranges widgets horizontally
QMessageBox - Pop up box to give users info, warnings, or errors
QTableWidget - a table widget that lets you show data in rows and columns
QTableWidgetItem - an item (cell) inside the table (text, icons, checkboxes)
QDateEdit - a date input widget, allows selecting or typing a date
QHeaderView - manages the headers of tables, supports resizing/stretching
QComboBox - a dropdown menu widget for selecting one option from a list
QDate - represents a date (used to set default values or manipulate dates)
Qt - contains enums and flags like ItemIsUserCheckable for checkboxes, alignment options
csv - standard Python module for reading from and writing to CSV files
'''


# Base class for OOP approach, inherit from QWidget so we are a type of QWidget
class PyQtApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Table App")     # App name
        self.setGeometry(500,200, 500, 400)     # Set size for our window (horizontal of widget on the screen, vertical of widget on the screen, width of widget, height of widget in pixels)
        
        # Set background color of window
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f9fc;
            }
            QLabel {
                color: #003366;
                font-size: 14px;
            }
            QLineEdit, QDateEdit {
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
                background-color: #cce0ff;  /* light blue base */
                alternate-background-color:  #a7c8fa;  /* slightly darker light blue */
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

        # Input Fields
        self.name_field = QLineEdit()          # Create text field
        self.name_field.setPlaceholderText("Enter your name")   # Placeholder text
        layout.addWidget(QLabel("Name: "))      # Label for text field
        layout.addWidget(self.name_field)       # Add text field to layout

        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Enter your email")   # Placeholder text
        layout.addWidget(QLabel("Email: "))      # Label for text field
        layout.addWidget(self.email_field)       # Add text field to layout

        self.dob_field = QDateEdit()                       # Create a date input widget for birthdays
        self.dob_field.setDisplayFormat("MM/dd/yyyy")      # Force display in DD/MM/YYYY format
        self.dob_field.setCalendarPopup(True)              # Enable calendar popup for easier date selection
        self.dob_field.setDate(QDate.currentDate())        # Set default date to today
        layout.addWidget(QLabel("Date of Birth: "))        # Label for date field
        layout.addWidget(self.dob_field)                   # Add date field to layout

        # Buttons in Horizontal Layout
        button_layout = QHBoxLayout()  # Create a vertical layout for buttons

        # Submit Button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_action)

        # Quit Button
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.quit_action)  # Perform quit action when clicked

        button_layout.addWidget(self.submit_button)
        button_layout.addWidget(self.quit_button)
        layout.addLayout(button_layout)  # Add button layout to main layout


        # Table with columns
        self.table = QTableWidget(0, 5)  # 0 rows, 5 column
        self.table.setHorizontalHeaderLabels(["Names", "Email", "Date of Birth", "Remote", "Language"])  # Set the headers for each column
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Make columns stretch to fit the table width
        self.table.setAlternatingRowColors(True)  # Alternate row colors for better readability
        layout.addWidget(self.table)

        self.setLayout(layout)                        # Need to associate the layout with the window


    def submit_action(self):
        name = self.name_field.text().strip()          # getter for text, then strip all white space from this string
        email = self.email_field.text().strip()
        birthday = self.dob_field.date().toString("MM/dd/yyyy")


        if not (name and email and birthday):  # Check if all fields are filled
            QMessageBox.warning(self, "Incomplete Input", "Please fill in all fields.")
        else:
            # Add row to table
            row_position = self.table.rowCount()  # Get current number of rows
            self.table.insertRow(row_position)    # Insert a new row at the end
            self.table.setItem(row_position, 0, QTableWidgetItem(name))      # Set name in first column
            self.table.setItem(row_position, 1, QTableWidgetItem(email))     # Set email in second column
            self.table.setItem(row_position, 2, QTableWidgetItem(birthday))  # Set birthday in third column

            # Remote checkbox in fourth column
            remote_item = QTableWidgetItem()        # Create an empty table item
            remote_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)  # Make it checkable and enabled
            remote_item.setCheckState(Qt.Unchecked)  # Default to unchecked
            self.table.setItem(row_position, 3, remote_item)  # Add checkbox to fourth column

            # Language ComboBox in fifth column (Dropdown menu)
            language_combo = QComboBox()  # Create a combo box
            language_combo.addItems(["English", "Spanish", "French", "German", "Chinese", "Japanese"])  # Add language options
            language_combo.setCurrentIndex(0)  # Set default to first language
            self.table.setItem(row_position, 4, QTableWidgetItem())  # Placeholder item for the combo box
            self.table.setCellWidget(row_position, 4, language_combo)  # Set the combo box as the cell widget


        # Clear input fields after submission
        self.name_field.clear()
        self.email_field.clear()
        self.dob_field.setDate(QDate.currentDate())  # reset safely to today


        self.name_field.setFocus()  # Set focus back to the name field for convenience    

    def save_table_to_csv(self, filename="table_data.csv"):
        row_count = self.table.rowCount()           # Get the total number of rows in the table
        col_count = self.table.columnCount()        # Get the total number of columns in the table

        # Open a CSV file for writing. 'w' mode overwrites the file if it exists.
        # 'newline=""' prevents extra blank lines between rows on some systems.
        # 'encoding="utf-8"' ensures proper handling of non-English characters.
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)               # Create a CSV writer object to write rows to the file

            # Write the table headers as the first row in the CSV
            headers = [self.table.horizontalHeaderItem(col).text() for col in range(col_count)]
            # Loop through all columns, get each header's text, and store in a list
            writer.writerow(headers)                # Write the header row to the CSV

            # Loop through each row in the table to write its data
            for row in range(row_count):
                row_data = []                        # Initialize a list to hold the current row's data

                # Loop through each column in the current row
                for col in range(col_count):

                    if col == 3:  # Remote checkbox column
                        item = self.table.item(row, col)  # Get the QTableWidgetItem from this cell
                        if item is not None:
                            # Check if the checkbox is checked; write "Yes" if checked, "No" otherwise
                            row_data.append("Yes" if item.checkState() == Qt.Checked else "No")
                        else:
                            row_data.append("No")  # If the cell is empty, default to "No"

                    elif col == 4:  # Language ComboBox column
                        combo = self.table.cellWidget(row, col)  # Get the QComboBox widget from this cell
                        if combo is not None:
                            row_data.append(combo.currentText())  # Save the currently selected language
                        else:
                            row_data.append("")  # If no combo box exists, leave blank

                    else:
                        # For normal text cells (Name, Email, Date of Birth)
                        item = self.table.item(row, col)  # Get the QTableWidgetItem
                        # Append its text if it exists; otherwise, append an empty string
                        row_data.append(item.text() if item is not None else "")

                # After processing all columns, write the row data to the CSV
                writer.writerow(row_data)


    def quit_action(self):
        self.save_table_to_csv()  # Save table data to CSV before quitting
        QApplication.quit()       # Quit the application






if __name__ == "__main__":
    app = QApplication(sys.argv)                    # Initializes application
    window = PyQtApp()                              # Create instance of our class
    window.show()                                   # Show method to run app
    sys.exit(app.exec())                            # sys.exit to exit app