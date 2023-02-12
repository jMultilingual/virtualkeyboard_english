from PySide6.QtWidgets import QApplication, QTextEdit,QMenu, QMainWindow
from PySide6.QtGui import QAction, QActionGroup
import sys
from keyboard_factory_db.commonnames import *

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.edit = TextEdit(self)
        self.setCentralWidget(self.edit)

    def initUI(self):

        self.keyboardMenu = QMenu(title="Keyboard")
        self.writingSystemChangeMenu = QMenu(title="Change")
        self.keyboardMenu.addMenu(self.writingSystemChangeMenu)
        self.menuBar().addMenu(self.keyboardMenu)

        self.en_GB_Action = QAction(text="Alphabet(United Kingdom)",
                                     triggered = self.writingSystemChanged,
                                     data = en_GB,
                                     checkable = True,
                                     checked = True
                                     )

        self.ru_RU_Action = QAction(text="Cyric(Russia)",
                                     triggered = self.writingSystemChanged,
                                     data = ru_RU,
                                     checkable = True
                                    )
        self.zh_CN_Action = QAction(text="Simplified Chinese",
                                     triggered = self.writingSystemChanged,
                                     data = zh_CN,
                                     checkable=True)

        self.ko_KR_Action = QAction(text="Hangul",
                                    triggered = self.writingSystemChanged,
                                    data = ko_KR,
                                    checkable = True
                                    )
        
        self.hi_IN_Action = QAction(text="Devanagari(India)",
                                    triggered = self.writingSystemChanged,
                                    data = hi_IN,
                                    checkable = True
                                    )
        
        self.ar_EG_Action = QAction(text="Arabic(Egypt)",
                                    triggered = self.writingSystemChanged,
                                    data = ar_EG,
                                    checkable = True
                                    )

        self.gez_ET_Action = QAction(text="Ge'ez(Ethiopea)",
                                     triggered = self.writingSystemChanged,
                                     data = gez_ET,
                                     checkable = True
                                     )

        self.km_KH_Action = QAction(text="Khmer(Cambodia)",
                                    triggered = self.writingSystemChanged,
                                    data = km_KH,
                                    checkable = True
                                    )
        self.yi_CN_Action = QAction(text="Yi",
                                    triggered = self.writingSystemChanged,
                                    data = yi_CN,
                                    checkable = True
                                    )
        self.bo_TA_Action = QAction(text="Bopomofo(Chinese Taipei)",
                                    triggered = self.writingSystemChanged,
                                    checkable = True
                                    )

        self.hi_EG_Action = QAction(text="Hieroglyph",
                                    triggered = self.writingSystemChanged,
                                    data=hi_EG,
                                    checkable=True
                                    )

        self.cu_PE_Action = QAction(text="Cuneiform",
                                    triggered = self.writingSystemChanged,
                                    data = cu_PE,
                                    checkable = True
                                    )

        
        self.actionGroup = QActionGroup(self)
        self.actionGroup.addAction(self.en_GB_Action)
        self.actionGroup.addAction(self.ru_RU_Action)
        self.actionGroup.addAction(self.zh_CN_Action)
        self.actionGroup.addAction(self.ko_KR_Action)        
        self.actionGroup.addAction(self.hi_IN_Action)
        self.actionGroup.addAction(self.ar_EG_Action)
        self.actionGroup.addAction(self.gez_ET_Action)
        self.actionGroup.addAction(self.km_KH_Action)
        self.actionGroup.addAction(self.yi_CN_Action)
        self.actionGroup.addAction(self.bo_TA_Action)
        self.actionGroup.addAction(self.hi_EG_Action)
        self.actionGroup.addAction(self.cu_PE_Action)
        self.writingSystemChangeMenu.addActions(
            [self.en_GB_Action, self.ru_RU_Action,
             self.zh_CN_Action, self.ko_KR_Action,
             self.hi_IN_Action, self.ar_EG_Action,
             self.gez_ET_Action, self.km_KH_Action,
             self.yi_CN_Action, self.bo_TA_Action,
             self.hi_EG_Action, self.cu_PE_Action
             ]
            )
    def writingSystemChanged(self):
        self.edit.writingSystem = self.sender().data()
        self.edit.changeWritingSystem()
    

class TextEdit(QTextEdit):

    def __init__(self, window, parent=None):
        super().__init__(parent)

        self._window = window

        self.writingSystem = en_GB
    

    def window(self):
        return self._window

    def changeWritingSystem(self):
        pass
    


def main():

    app = (QApplication([])
           if QApplication.instance() is None
           else
           QApplication.instance())

    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
