import sys, os
from PySide2 import QtWidgets, QtCore, QtGui
import MainWindow

debugging = True

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class MainApplication(QtWidgets.QApplication):
    def __init__(self):
        try:
            super().__init__(sys.argv)
            print("[        ] Starting main application...")


            
            
            
            os.chdir(os.path.expanduser("~"))

            self.window = MainWindow.MainWindow()
            

        

            self.exec_()
        except Exception as e:
            if(debugging):
                raise e

MainApplication()