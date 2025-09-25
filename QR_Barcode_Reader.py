import cv2 # OpenCV library for image processing
import time    # Library for time-related functions
import sys     # System-specific parameters and functions
from pyzbar.pyzbar import decode  # Library for decoding barcodes and QR codes
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import QTimer

# img = cv2.imread('tutorial.png')     # This is how you read images from a file

class ScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR and Barcode Scanner")  # Set the window title
        self.setGeometry(200, 200, 500, 400)           # Set the window size and position

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Label to show messages
        self.message_label = QLabel("Click 'Start Scanning' to begin.")
        self.layout.addWidget(self.message_label)

        # Start scan button
        self.start_button = QPushButton("Start Scanning")
        self.start_button.clicked.connect(self.start_scanning)
        self.layout.addWidget(self.start_button)

        # Stop Scan button
        self.stop_button = QPushButton("Stop Scanning")
        self.stop_button.clicked.connect(self.stop_scanning)
        self.layout.addWidget(self.stop_button)
        self.stop_button.setEnabled(False)  # Disable stop button initially

        # Camera setup
        self.cap = None                 # Camera capture object
        self.timer = QTimer()           # Timer to control frame capture
        self.timer.timeout.connect(self.scan_frame)  # Connect timer to scan_frame method
        self.used_codes = []            # List to store already used QR codes

    def start_scanning(self):
        self.cap = cv2.VideoCapture(0)  # Start video capture from the webcam
        self.cap.set(3, 640)            # Set width
        self.cap.set(4, 480)            # Set height

        self.message_label.setText("Scanning...")   # Update message
        self.start_button.setEnabled(False)  # Disable start button
        self.stop_button.setEnabled(True)    # Enable stop button
        self.timer.start(100)                # Start timer to capture frames every 100 ms

    def stop_scanning(self):
        self.timer.stop()              # Stop the timer
        if self.cap:
            self.cap.release()       # Release the camera
            cv2.destroyAllWindows()  # Close any OpenCV windows
        self.message_label.setText("Scanning stopped.")  # Update message
        self.start_button.setEnabled(True)   # Enable start button
        self.stop_button.setEnabled(False)   # Disable stop button

    def scan_frame(self):
        if not self.cap:
            return
        
        success, frame = self.cap.read()  # Read a frame from the webcam
        if not success:
            self.message_label.setText("Failed to capture frame.")
            return
        
        for code in decode(frame):  # Decode any QR codes in the frame
            code_data = code.data.decode('utf-8')
            if code_data not in self.used_codes:
                self.used_codes.append(code_data)  # Add the code to the list of used codes
                self.message_label.setText(f"Approved: {code_data}")  # Update message
                print(f"Approved: {code_data}")  # Print to console
                time.sleep(1)  # Short delay to avoid duplicates
            else:
                self.message_label.setText(f"This code has already been used.")
                print("This code has already been used.")  # Print to console
                time.sleep(1)  # Short delay to avoid duplicates

        # Show the video feed
        cv2.imshow('QR and Barcode Scanner', frame)
        cv2.waitKey(1)  # Wait for 1 ms before capturing the next frame


            

if __name__ == "__main__":
    app = QApplication(sys.argv)                    # Initializes application
    window = ScannerApp()                              # Create instance of our class
    window.show()                                   # Show method to run app
    sys.exit(app.exec())                            # sys.exit to exit app