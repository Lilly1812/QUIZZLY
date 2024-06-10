import pyodbc
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem

def createDatabase():# Connect to your SQL Server
    conn = pyodbc.connect('DRIVER={SQL Server};'
                        'SERVER=LILLYC\SQLEXPRESS;'
                        'Trusted_Connection=yes;'
                        'DATABASE=master;'  # Connect to master database to create a new database
                        )

    cursor = conn.cursor()

def createTable():# Create QUIZZLY database
    cursor.execute('CREATE DATABASE QUIZZLY')

    # Connect to the new QUIZZLY database
    conn = pyodbc.connect('DRIVER={SQL Server};'
                        'SERVER=LILLYC\SQLEXPRESS;'
                        'DATABASE=QUIZZLY;'
                        'Trusted_Connection=yes;'  # Set autocommit mode
                        )

    cursor = conn.cursor()

# Create Library table
    cursor.execute("""
        CREATE TABLE Library (
            ID VARCHAR(255) PRIMARY KEY,
            Question NVARCHAR(255) NOT NULL,
            AnsA NVARCHAR(255) NOT NULL,
            AnsB NVARCHAR(255) NOT NULL,
            AnsC NVARCHAR(255) NOT NULL,
            AnsD NVARCHAR(255) NOT NULL,
            CorrectAns CHAR(1) NOT NULL
        )
    """)

    # Insert sample questions into the Library table
    cursor.execute("""
        INSERT INTO Library (ID, Question, AnsA, AnsB, AnsC, AnsD, CorrectAns) VALUES
        (1, 'What is the capital city of Japan?', 'Seoul', 'Beijing', 'Tokyo', 'Bangkok', 'C'),
        (2, 'Who wrote the play "Romeo and Juliet"?', 'William Shakespeare', 'Charles Dickens', 'Jane Austen', 'Mark Twain', 'A'),
        (3, 'What is the boiling point of water?', '90°C', '100°C', '110°C', '120°C', 'B'),
        (4, 'What is the largest planet in our solar system?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'C'),
        (5, 'Which element has the chemical symbol O?', 'Gold', 'Oxygen', 'Osmium', 'Oganesson', 'B'),
        (6, 'Who is known as the "Father of Computers"?', 'Albert Einstein', 'Isaac Newton', 'Charles Babbage', 'Nikola Tesla', 'C'),
        (7, 'What is the currency of the United Kingdom?', 'Euro', 'Dollar', 'Pound Sterling', 'Yen', 'C'),
        (8, 'Which country is the largest by land area?', 'United States', 'China', 'Canada', 'Russia', 'D'),
        (9, 'Who painted the ceiling of the Sistine Chapel?', 'Leonardo da Vinci', 'Michelangelo', 'Raphael', 'Donatello', 'B'),
        (10, 'What is the hardest natural substance on Earth?', 'Gold', 'Iron', 'Diamond', 'Silver', 'C');
    """)
    conn.commit()
    conn.close()


def showLibrary(self):
    # Assuming you have a connection to the database QUIZZLY
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=LILLYC\SQLEXPRESS;'
                          'DATABASE=QUIZZLY;'
                          'Trusted_Connection=yes;'  # Set autocommit mode
                          )
    cursor = conn.cursor()
    # Select all rows from Library table
    cursor.execute("SELECT * FROM Library")
    rows = cursor.fetchall()
    # Clear the table
    self.tableWidget_2.setRowCount(0)
    # Add rows to the table
    for row_number, row_data in enumerate(rows):
        self.tableWidget_2.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.tableWidget_2.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    conn.commit()
    conn.close()
            
def INSERTQUESTION(self):
        # Assuming you have a connection to the database QUIZZLY
        
    conn = pyodbc.connect('DRIVER={SQL Server};'
                          'SERVER=LILLYC\SQLEXPRESS;'
                          'DATABASE=QUIZZLY;'
                          'Trusted_Connection=yes;'  # Set autocommit mode
                          )
    cursor = conn.cursor()
    # Get text from QLineEdit widgets
    ID = self.edit_ID.text()
    Question = self.edit_Question.text()
    AnsA = self.edit_ansA.text()
    AnsB = self.edit_ansB.text()
    AnsC = self.edit_ansC.text()
    AnsD = self.edit_ansD.text()
    CorrectAns = self.edit_correctans.text()
    # Insert into Library table
    cursor.execute("""
        INSERT INTO Library (ID, Question, AnsA, AnsB, AnsC, AnsD, CorrectAns)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, ID, Question, AnsA, AnsB, AnsC, AnsD, CorrectAns)
    conn.commit()
    conn.close()