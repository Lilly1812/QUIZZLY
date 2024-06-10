import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from pathlib import Path
from Library import showLibrary,INSERTQUESTION
#  this is a branch
class MainWindow(QMainWindow):
    DESIGNER_FILE: str = "form.ui"

    def __init__(self) -> None:
        super().__init__()
        print("Initializing MainWindow...")
        designer_files_path = Path(__file__).resolve().parent.joinpath(self.DESIGNER_FILE)
        print(f"Loading UI file from: {designer_files_path}")
        self.ui = uic.loadUi(designer_files_path, self)
        print("UI file loaded successfully.")  
        
    # tuong tac main
        self.ui.teacher.clicked.connect(self.SwitchToTeacherWidget)
        self.ui.student.clicked.connect(self.SwitchToStudentWidget)
    # tuong tac TEACHER    
        self.ui.library.clicked.connect(self.SwitchToLIBRARYWidget)
        self.ui.history_teacher.clicked.connect(self.SwitchToHistoryWidget)
        # tuong tac nut back
        self.ui.BACK.clicked.connect(self.SwitchToMAINWidget)
        self.ui.BACK_5.clicked.connect(self.SwitchToTeacherWidget)
        self.ui.BACK_4.clicked.connect(self.SwitchToMAINWidget)
        self.ui.BACK_6.clicked.connect(self.SwitchToStudentWidget)
        self.ui.BACK_7.clicked.connect(self.SwitchToStudentWidget)
        self.ui.BACK_2.clicked.connect(self.SwitchToMAINWidget)
        self.ui.BACK_8.clicked.connect(self.HideAddWidget)
             # tuong tac STUDENT
        self.ui.practicemode.clicked.connect(self.SwitchToPracticemodeWidget)
        self.ui.testmode.clicked.connect(self.SwitchToTestmodeWidget)
        self.ui.history_student.clicked.connect(self.SwitchToHistoryWidget)
            # tuong tac LIBRARY
        self.ui.add_widget.hide()
        self.ui.add_button.clicked.connect(self.ShowAddWidget)
        self.ui.enter_button.clicked.connect(INSERTQUESTION)
        self.ui.enter_button.clicked.connect(self.Clearthetext)
        showLibrary(self)
    def SwitchToTeacherWidget(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.TEACHER)
    def SwitchToStudentWidget(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.STUDENT)
    def SwitchToLIBRARYWidget(self) :
        self.ui.stackedWidget.setCurrentWidget(self.ui.LIBRARY_teacher)
    def ShowAddWidget(self) :
        self.ui.add_widget.show()
    def HideAddWidget(self) :    
        self.ui.add_widget.hide()
    def SwitchToHistoryWidget(self) :
        self.ui.stackedWidget.setCurrentWidget(self.ui.History)
    def SwitchToMAINWidget(self) :
        self.ui.stackedWidget.setCurrentWidget(self.ui.MAIN)
    def SwitchToPracticemodeWidget(self) :
        self.ui.stackedWidget.setCurrentWidget(self.ui.Practicemode)
    def SwitchToTestmodeWidget(self) :
        self.ui.stackedWidget.setCurrentWidget(self.ui.Testmode)
    def SwitchToMAINWidget(self) :
        self.ui.stackedWidget.setCurrentWidget(self.ui.MAIN)
    def Clearthetext(self):
        self.edit_ID.clear()
        self.edit_Question.clear()
        self.edit_ansA.clear()
        self.edit_ansB.clear()
        self.edit_ansC.clear()
        self.edit_ansD.clear()
        self.edit_correctans.clear()

    

if __name__ == "__main__":
    print("Starting application...")
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    print("Showing the main window...")
    sys.exit(app.exec())
