from PySide6.QtWidgets import (QApplication, QTextEdit,QMenu, QMainWindow,
                               QSpacerItem, QHBoxLayout, QVBoxLayout, QWidget,
                               QDockWidget, QPushButton)
from PySide6.QtGui import QAction, QActionGroup, QIcon, QFontMetricsF
from PySide6.QtCore import Qt, QSize

import sys
from keyboard_factory_db.commonnames import *


class KeyboardPushButton(QPushButton):

    def __init__(self, keys=["", "", "", "", "", "", ""],
                       icon= QIcon(), text="", objectName="", parent=None
                 ):

        super().__init__(icon, text, parent)

        self.keys = keys
        self.setObjectName(objectName)
        self.setFocusPolicy(Qt.NoFocus)
        self.underLeft = keys[INPUT_TEXT]
        self.underRight = keys[SHIFT_INPUT_TEXT]
        self.upperLeft = keys[ALT_INPUT_TEXT]
        self.upperRight = keys[SHIFT_ALT_INPUT_TEXT]

    def setKeys(self, keys):
        self.keys = keys
        self.underLeft = keys[INPUT_TEXT]
        self.underRight = keys[SHIFT_INPUT_TEXT]
        self.upperLeft = keys[ALT_INPUT_TEXT]
        self.upperRight = keys[SHIFT_ALT_INPUT_TEXT]

  

    def sizeHint(self):
        
        font = self.font()
        matrics = QFontMetricsF(font)
        width = matrics.horizontalAdvance(self.text())
        
        if self.objectName() == KEY_TAB:
            
            return QSize(width+20, 40)
        elif self.objectName() == KEY_CAPSLOCK:
            return QSize(width+40, 40)
        elif self.objectName() == KEY_LEFTSHIFT:
            return QSize(width+60, 40)
        elif self.objectName() == KEY_ENTER:
            return QSize(width+30, 80)
        elif self.objectName() == KEY_SPACE:
            return QSize(width+120, 40)

        return QSize(width, 40)

    def minimumSizeHint(self):
        
        font = self.font()
        matrics = QFontMetricsF(font)
        width = matrics.horizontalAdvance(self.text())

        if self.objectName() == KEY_ENTER:
            
            return QSize(width+30, 80)
        elif self.objectName() == KEY_SPACE:
            return QSize(width+120, 40)

        return QSize(width+20, 40)


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

        self.edit = TextEdit(self)
        self.setCentralWidget(self.edit)

    def initUI(self):
        self.keyboardDockWidget = QDockWidget("Keyboard")
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.keyboardDockWidget)
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

        self.initKeyboard()

    def initKeyboard(self):
        

        self.Key_Escape = KeyboardPushButton(objectName = KEY_ESCAPE)
        self.Key_F1 = KeyboardPushButton(objectName=KEY_F1)
        self.Key_F2 = KeyboardPushButton(objectName=KEY_F2)
        self.Key_F3 = KeyboardPushButton(objectName=KEY_F3)
        self.Key_F4 = KeyboardPushButton(objectName=KEY_F4)
        self.Key_F5 = KeyboardPushButton(objectName=KEY_F5)
        self.Key_F6 = KeyboardPushButton(objectName=KEY_F6)
        self.Key_F7 = KeyboardPushButton(objectName=KEY_F7)
        self.Key_F8 = KeyboardPushButton(objectName=KEY_F8)
        self.Key_F9 = KeyboardPushButton(objectName=KEY_F9)
        self.Key_F10 = KeyboardPushButton(objectName=KEY_F10)
        self.Key_F11 = KeyboardPushButton(objectName=KEY_F11)
        self.Key_F12 = KeyboardPushButton(objectName=KEY_F12)
        
        
        self.Key_1 = KeyboardPushButton(objectName=KEY_1)
        self.Key_2 = KeyboardPushButton(objectName=KEY_2)
        self.Key_3 = KeyboardPushButton(objectName=KEY_3)
        self.Key_4 = KeyboardPushButton(objectName=KEY_4)
        self.Key_5 = KeyboardPushButton(objectName=KEY_5)
        self.Key_6 = KeyboardPushButton(objectName=KEY_6)
        self.Key_7 = KeyboardPushButton(objectName=KEY_7)
        self.Key_8 = KeyboardPushButton(objectName=KEY_8)
        self.Key_9 = KeyboardPushButton(objectName=KEY_9)
        self.Key_0 = KeyboardPushButton(objectName=KEY_0)
        

        self.Key_A = KeyboardPushButton(objectName=KEY_A)
        self.Key_B = KeyboardPushButton(objectName=KEY_B)
        self.Key_C = KeyboardPushButton(objectName=KEY_C)
        self.Key_D = KeyboardPushButton(objectName=KEY_D)
        self.Key_E = KeyboardPushButton(objectName=KEY_E)
        self.Key_F = KeyboardPushButton(objectName=KEY_F)
        self.Key_G = KeyboardPushButton(objectName=KEY_G)
        self.Key_H = KeyboardPushButton(objectName=KEY_H)
        self.Key_I = KeyboardPushButton(objectName=KEY_I)
        self.Key_J = KeyboardPushButton(objectName=KEY_J)
        self.Key_K = KeyboardPushButton(objectName=KEY_K)
        self.Key_L = KeyboardPushButton(objectName=KEY_L)
        self.Key_M = KeyboardPushButton(objectName=KEY_M)
        self.Key_N = KeyboardPushButton(objectName=KEY_N)
        self.Key_O = KeyboardPushButton(objectName=KEY_O)
        self.Key_P = KeyboardPushButton(objectName=KEY_P)
        self.Key_Q = KeyboardPushButton(objectName=KEY_Q)
        self.Key_R = KeyboardPushButton(objectName=KEY_R)
        self.Key_S = KeyboardPushButton(objectName=KEY_S)
        self.Key_T = KeyboardPushButton(objectName=KEY_T)
        self.Key_U = KeyboardPushButton(objectName=KEY_U)
        self.Key_V = KeyboardPushButton(objectName=KEY_V)
        self.Key_W = KeyboardPushButton(objectName=KEY_W)
        self.Key_X = KeyboardPushButton(objectName=KEY_X)
        self.Key_Y = KeyboardPushButton(objectName=KEY_Y)
        self.Key_Z = KeyboardPushButton(objectName=KEY_Z)


        self.Key_IME = KeyboardPushButton(objectName=KEY_IME)
        self.Key_Tab = KeyboardPushButton(objectName=KEY_TAB)
        
        self.Key_CapsLock = KeyboardPushButton(objectName=KEY_CAPSLOCK)
        self.Key_LeftShift = KeyboardPushButton(objectName=KEY_LEFTSHIFT)
        self.Key_LeftControl  = KeyboardPushButton(objectName=KEY_LEFTCONTROL)
        self.Key_WindowMark = KeyboardPushButton(objectName=KEY_WINDOW)
        self.Key_LeftAlt = KeyboardPushButton(objectName=KEY_LEFTALT)
        self.Key_NoConversion = KeyboardPushButton(objectName=KEY_NOCONVERSION)
        self.Key_Space = KeyboardPushButton(objectName=KEY_SPACE)
        self.Key_Conversion = KeyboardPushButton(objectName=KEY_CONVERSION)
        self.Key_Katakana = KeyboardPushButton(objectName=KEY_KATAKANA)
        self.Key_RightAlt = KeyboardPushButton(objectName=KEY_RIGHTALT)
        self.Key_Menu = KeyboardPushButton(objectName=KEY_TOOL)
        
        
        self.Key_RightCtrl = KeyboardPushButton(objectName=KEY_RIGHTCONTROL)
        

        self.Key_Enter = KeyboardPushButton(objectName=KEY_ENTER)
        self.Key_Colon = KeyboardPushButton(objectName=KEY_COLON)
        self.Key_Semicolon = KeyboardPushButton(objectName=KEY_SEMICOLON)
        self.Key_At = KeyboardPushButton(objectName=KEY_AT)
        self.Key_Comma = KeyboardPushButton(objectName=KEY_COMMA)
        self.Key_Period = KeyboardPushButton(objectName=KEY_PERIOD)
        self.Key_Slash = KeyboardPushButton(objectName=KEY_SLASH)
        self.Key_Backslash = KeyboardPushButton(objectName=KEY_BACKSLASH)
        self.Key_BracketLeft = KeyboardPushButton(objectName=KEY_BRACKETLEFT)
        self.Key_BracketRight = KeyboardPushButton(objectName=KEY_BRACKETRIGHT)
        self.Key_Minus = KeyboardPushButton(objectName=KEY_MINUS)
        self.Key_AsciiCircum = KeyboardPushButton(objectName=KEY_CIRCUMFLEX)
        self.Key_Bar = KeyboardPushButton(objectName=KEY_BAR)
        self.Key_BackSpace = KeyboardPushButton(objectName=KEY_BACKSPACE)
       
        self.Key_RightShift = KeyboardPushButton(objectName=KEY_RIGHTSHIFT)
   
        
        self.keyDicts = KeyDict({Qt.Key_F1:self.Key_F1, Qt.Key_F2:self.Key_F2, Qt.Key_F3: self.Key_F3, Qt.Key_F4: self.Key_F4, Qt.Key_F5: self.Key_F5, Qt.Key_F6: self.Key_F6, Qt.Key_F7: self.Key_F7, Qt.Key_F8: self.Key_F8, Qt.Key_F9: self.Key_F9, Qt.Key_F10: self.Key_F10, Qt.Key_F11: self.Key_F11, Qt.Key_F12: self.Key_F12,
                                 Qt.Key_1:self.Key_1, Qt.Key_2:self.Key_2, Qt.Key_3: self.Key_3, Qt.Key_4: self.Key_4, Qt.Key_5: self.Key_5, Qt.Key_6: self.Key_6, Qt.Key_7: self.Key_7, Qt.Key_8: self.Key_8, Qt.Key_9: self.Key_9, Qt.Key_0: self.Key_0,
                                 Qt.Key_A:self.Key_A, Qt.Key_B:self.Key_B, Qt.Key_C: self.Key_C, Qt.Key_D: self.Key_D, Qt.Key_E: self.Key_E, Qt.Key_F: self.Key_F, Qt.Key_G: self.Key_G, Qt.Key_H: self.Key_H, Qt.Key_I: self.Key_I, Qt.Key_J: self.Key_J, Qt.Key_K: self.Key_K, Qt.Key_L: self.Key_L, Qt.Key_M:self.Key_M,
                                 Qt.Key_N:self.Key_N, Qt.Key_O:self.Key_O, Qt.Key_P: self.Key_P, Qt.Key_Q: self.Key_Q, Qt.Key_R: self.Key_R, Qt.Key_S: self.Key_S, Qt.Key_T: self.Key_T, Qt.Key_U: self.Key_U, Qt.Key_V: self.Key_V, Qt.Key_W: self.Key_W, Qt.Key_X: self.Key_X, Qt.Key_Y:self.Key_Y, Qt.Key_Z: self.Key_Z,
                                 Qt.Key_Minus: self.Key_Minus, Qt.Key_AsciiCircum: self.Key_AsciiCircum, Qt.Key_Bar: self.Key_Bar, Qt.Key_At: self.Key_At, Qt.Key_BracketLeft: self.Key_BracketLeft, Qt.Key_Semicolon: self.Key_Semicolon, Qt.Key_Colon: self.Key_Colon, Qt.Key_BracketRight: self.Key_BracketRight,
                                 Qt.Key_Comma: self.Key_Comma, Qt.Key_Period:self.Key_Period, Qt.Key_Slash: self.Key_Slash, Qt.Key_Backslash: self.Key_Backslash,
                                 Qt.Key_Space: self.Key_Space,
                                 Qt.Key_Exclam:self.Key_1, Qt.Key_QuoteDbl: self.Key_2,
                                 Qt.Key_NumberSign: self.Key_3, Qt.Key_Dollar: self.Key_4,
                                 Qt.Key_Percent: self.Key_5,
                                 Qt.Key_Ampersand: self.Key_6, Qt.Key_Apostrophe: self.Key_7,
                                 Qt.Key_ParenLeft: self.Key_8, Qt.Key_ParenRight: self.Key_9,
                                Qt.Key_AsciiTilde: self.Key_AsciiCircum, Qt.Key_Bar: self.Key_Backslash,
                                Qt.Key_Asterisk: self.Key_Colon, Qt.Key_BraceLeft: self.Key_BracketLeft,
                                Qt.Key_BraceRight: self.Key_BracketRight, Qt.Key_QuoteLeft: self.Key_At,
                                Qt.Key_AsciiTilde: self.Key_AsciiCircum,Qt.Key_Plus:self.Key_Semicolon,
                                Qt.Key_Question: self.Key_Slash, Qt.Key_Equal: self.Key_Minus,
                                Qt.Key_Underscore: self.Key_Backslash, Qt.Key_Less:self.Key_Comma,
                                 Qt.Key_Greater: self.Key_Period})
       
                                       



        column = 0
        escapeSpacerItem = QSpacerItem(40, 40)
        f4SpacerItem = QSpacerItem(20, 40)
        f8SpacerItem = QSpacerItem(20, 40)
        
        self.fLKH = self.functionLineKeyboardHBoxLayout = QHBoxLayout()
 
        self.fLKH.addWidget(self.Key_Escape )
        self.fLKH.addItem(escapeSpacerItem)
        self.fLKH.addWidget(self.Key_F1)
        self.fLKH.addWidget(self.Key_F2)
        self.fLKH.addWidget(self.Key_F3)
        self.fLKH.addWidget(self.Key_F4)
        self.fLKH.addItem(f4SpacerItem)
        self.fLKH.addWidget(self.Key_F5)
        self.fLKH.addWidget(self.Key_F6)
        self.fLKH.addWidget(self.Key_F7)
        self.fLKH.addWidget(self.Key_F8)
        self.fLKH.addItem(f8SpacerItem)
        self.fLKH.addWidget(self.Key_F9)
        self.fLKH.addWidget(self.Key_F10)
        self.fLKH.addWidget(self.Key_F11)
        self.fLKH.addWidget(self.Key_F12)
        
        self.nLKH = self.numberLineKeyboardHBoxLayout = QHBoxLayout()
        self.nLKH.addWidget(self.Key_IME)
        self.nLKH.addWidget(self.Key_1)
        self.nLKH.addWidget(self.Key_2)
        self.nLKH.addWidget(self.Key_3)
        self.nLKH.addWidget(self.Key_4)
        self.nLKH.addWidget(self.Key_5)
        self.nLKH.addWidget(self.Key_6)
        self.nLKH.addWidget(self.Key_7)
        self.nLKH.addWidget(self.Key_8)
        self.nLKH.addWidget(self.Key_9)
        self.nLKH.addWidget(self.Key_0)
        self.nLKH.addWidget(self.Key_Minus)
        self.nLKH.addWidget(self.Key_AsciiCircum)
        self.nLKH.addWidget(self.Key_Bar)

        

        self.tACLKV = self.tabAndCapsLockKeyboardVBoxLayout = QVBoxLayout()
        self.tACLKEH = self.tabAndCapsLockKeyboardEnterHBoxLayout = QHBoxLayout()
        self.tLKH = self.tabLineKeyboardHBoxLayout = QHBoxLayout()
        
        self.tLKH.addWidget(self.Key_Tab)
        self.tLKH.addWidget(self.Key_Q)
        self.tLKH.addWidget(self.Key_W)
        self.tLKH.addWidget(self.Key_E)
        self.tLKH.addWidget(self.Key_R)
        self.tLKH.addWidget(self.Key_T)
        self.tLKH.addWidget(self.Key_Y)
        self.tLKH.addWidget(self.Key_U)
        self.tLKH.addWidget(self.Key_I)
        self.tLKH.addWidget(self.Key_O)
        self.tLKH.addWidget(self.Key_P)
        self.tLKH.addWidget(self.Key_At)
        self.tLKH.addWidget(self.Key_BracketLeft)
        

        self.cLLKH = QHBoxLayout()
        self.cLLKH.addWidget(self.Key_CapsLock) 
        self.cLLKH.addWidget(self.Key_A)
        self.cLLKH.addWidget(self.Key_S)
        self.cLLKH.addWidget(self.Key_D)
        self.cLLKH.addWidget(self.Key_F)
        self.cLLKH.addWidget(self.Key_G)
        self.cLLKH.addWidget(self.Key_H)
        self.cLLKH.addWidget(self.Key_J)
        self.cLLKH.addWidget(self.Key_K)
        self.cLLKH.addWidget(self.Key_L)
        self.cLLKH.addWidget(self.Key_Semicolon)
        self.cLLKH.addWidget(self.Key_Colon)
        self.cLLKH.addWidget(self.Key_BracketRight)

        self.slkH = self.shiftLineKeyboardHBoxLayout = QHBoxLayout()
        self.slkH.addWidget(self.Key_LeftShift)
        self.slkH.addWidget(self.Key_Z)
        self.slkH.addWidget(self.Key_X)
        self.slkH.addWidget(self.Key_C)
        self.slkH.addWidget(self.Key_V)
        self.slkH.addWidget(self.Key_B)
        self.slkH.addWidget(self.Key_N)
        self.slkH.addWidget(self.Key_M)
        self.slkH.addWidget(self.Key_Comma)
        self.slkH.addWidget(self.Key_Period)
        self.slkH.addWidget(self.Key_Slash)
        self.slkH.addWidget(self.Key_Backslash)


        self.cLKH = self.ctrlLineKeyboardHBoxLayout = QHBoxLayout()
        self.cLKH.addWidget(self.Key_LeftControl)
        self.cLKH.addWidget(self.Key_WindowMark)
        self.cLKH.addWidget(self.Key_LeftAlt)
        self.cLKH.addWidget(self.Key_NoConversion)
        self.cLKH.addWidget(self.Key_Space)
        self.cLKH.addWidget(self.Key_Conversion)
        self.cLKH.addWidget(self.Key_Katakana)
        self.cLKH.addWidget(self.Key_RightAlt)
        self.cLKH.addWidget(self.Key_Menu)
        self.cLKH.addWidget(self.Key_RightCtrl)
   
    
        vSpacerItem =  QSpacerItem(500, 20)
        
        self.keyboardVBoxLayout = QVBoxLayout()
        
        self.keyboardVBoxLayout.addLayout(self.fLKH)
        self.keyboardVBoxLayout.addItem(vSpacerItem)
        self.keyboardVBoxLayout.addLayout(self.nLKH)
        
        self.tACLKV.addLayout(self.tLKH)
        self.tACLKV.addLayout(self.cLLKH)
        self.tACLKEH.addLayout(self.tACLKV, 90)
        self.tACLKEH.addWidget(self.Key_Enter, 10)
        self.tACLKEH.setSpacing(1)

        self.keyboardVBoxLayout.addLayout(self.tACLKEH)
        self.keyboardVBoxLayout.addLayout(self.slkH)
        self.keyboardVBoxLayout.addLayout(self.cLKH)
        self.keyboardVBoxLayout.setSpacing(1)

        self.keyboardWidget = QWidget()
        self.keyboardWidget.setLayout(self.keyboardVBoxLayout)
        self._window.keyboardDockWidget.setWidget(self.keyboardWidget)        
        
        self.changeWritingSystem()

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
