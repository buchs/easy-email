# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ReadWindow.ui'
#
# Created: Sun Feb 24 07:20:41 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(794, 476)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 85, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(6, -1, 6, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_reply = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_reply.sizePolicy().hasHeightForWidth())
        self.btn_reply.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_reply.setFont(font)
        self.btn_reply.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 0);"))
        self.btn_reply.setObjectName(_fromUtf8("btn_reply"))
        self.horizontalLayout.addWidget(self.btn_reply)
        self.btn_replyall = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_replyall.sizePolicy().hasHeightForWidth())
        self.btn_replyall.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_replyall.setFont(font)
        self.btn_replyall.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 0);"))
        self.btn_replyall.setObjectName(_fromUtf8("btn_replyall"))
        self.horizontalLayout.addWidget(self.btn_replyall)
        self.btn_forward = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_forward.sizePolicy().hasHeightForWidth())
        self.btn_forward.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_forward.setFont(font)
        self.btn_forward.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 0);"))
        self.btn_forward.setObjectName(_fromUtf8("btn_forward"))
        self.horizontalLayout.addWidget(self.btn_forward)
        self.btn_delete = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_delete.sizePolicy().hasHeightForWidth())
        self.btn_delete.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_delete.setFont(font)
        self.btn_delete.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 0);"))
        self.btn_delete.setObjectName(_fromUtf8("btn_delete"))
        self.horizontalLayout.addWidget(self.btn_delete)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pointer = QtGui.QFrame(self.centralwidget)
        self.pointer.setMinimumSize(QtCore.QSize(100, 0))
        self.pointer.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.pointer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pointer.setFrameShadow(QtGui.QFrame.Raised)
        self.pointer.setObjectName(_fromUtf8("pointer"))
        self.horizontalLayout.addWidget(self.pointer)
        self.btn_attachs = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_attachs.sizePolicy().hasHeightForWidth())
        self.btn_attachs.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_attachs.setFont(font)
        self.btn_attachs.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 0);"))
        self.btn_attachs.setObjectName(_fromUtf8("btn_attachs"))
        self.horizontalLayout.addWidget(self.btn_attachs)
        self.btn_close = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_close.setFont(font)
        self.btn_close.setStyleSheet(_fromUtf8("background-color: rgb(255, 85, 0);"))
        self.btn_close.setObjectName(_fromUtf8("btn_close"))
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.date_from = QtGui.QHBoxLayout()
        self.date_from.setObjectName(_fromUtf8("date_from"))
        self.date_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date_label.sizePolicy().hasHeightForWidth())
        self.date_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.date_label.setFont(font)
        self.date_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.date_label.setObjectName(_fromUtf8("date_label"))
        self.date_from.addWidget(self.date_label)
        self.date = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.date.setFont(font)
        self.date.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.date.setObjectName(_fromUtf8("date"))
        self.date_from.addWidget(self.date)
        self.from_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_label.sizePolicy().hasHeightForWidth())
        self.from_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.from_label.setFont(font)
        self.from_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.from_label.setObjectName(_fromUtf8("from_label"))
        self.date_from.addWidget(self.from_label)
        self.frm = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.frm.setFont(font)
        self.frm.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.frm.setObjectName(_fromUtf8("frm"))
        self.date_from.addWidget(self.frm)
        self.verticalLayout.addLayout(self.date_from)
        self.subject_layout = QtGui.QHBoxLayout()
        self.subject_layout.setObjectName(_fromUtf8("subject_layout"))
        self.subj_label = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subj_label.sizePolicy().hasHeightForWidth())
        self.subj_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.subj_label.setFont(font)
        self.subj_label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 0);"))
        self.subj_label.setObjectName(_fromUtf8("subj_label"))
        self.subject_layout.addWidget(self.subj_label)
        self.subject = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.subject.setFont(font)
        self.subject.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.subject.setObjectName(_fromUtf8("subject"))
        self.subject_layout.addWidget(self.subject)
        self.verticalLayout.addLayout(self.subject_layout)
        self.body = QtWebKit.QWebView(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(16)
        self.body.setFont(font)
        self.body.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.body.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.body.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.body.setObjectName(_fromUtf8("body"))
        self.verticalLayout.addWidget(self.body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Message - Reading", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_reply.setText(QtGui.QApplication.translate("MainWindow", "Reply", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_replyall.setText(QtGui.QApplication.translate("MainWindow", "Reply All", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_forward.setText(QtGui.QApplication.translate("MainWindow", "Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_delete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_attachs.setText(QtGui.QApplication.translate("MainWindow", "Show Attachments", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_close.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.date_label.setText(QtGui.QApplication.translate("MainWindow", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.date.setText(QtGui.QApplication.translate("MainWindow", "12/12/12", None, QtGui.QApplication.UnicodeUTF8))
        self.from_label.setText(QtGui.QApplication.translate("MainWindow", "From:", None, QtGui.QApplication.UnicodeUTF8))
        self.frm.setText(QtGui.QApplication.translate("MainWindow", "email", None, QtGui.QApplication.UnicodeUTF8))
        self.subj_label.setText(QtGui.QApplication.translate("MainWindow", "Subject:", None, QtGui.QApplication.UnicodeUTF8))
        self.subject.setText(QtGui.QApplication.translate("MainWindow", "subject", None, QtGui.QApplication.UnicodeUTF8))

from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

