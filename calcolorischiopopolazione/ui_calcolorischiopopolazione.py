# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_calcolorischiopopolazione.ui'
#
# Created: Wed Apr 29 10:00:09 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FloodRisk(object):
    def setupUi(self, FloodRisk):
        FloodRisk.setObjectName(_fromUtf8("FloodRisk"))
        FloodRisk.resize(739, 611)
        self.pushButtonSalvaProgetto = QtGui.QPushButton(FloodRisk)
        self.pushButtonSalvaProgetto.setEnabled(True)
        self.pushButtonSalvaProgetto.setGeometry(QtCore.QRect(10, 540, 131, 31))
        self.pushButtonSalvaProgetto.setObjectName(_fromUtf8("pushButtonSalvaProgetto"))
        self.pushButtonLoadLayer = QtGui.QPushButton(FloodRisk)
        self.pushButtonLoadLayer.setGeometry(QtCore.QRect(150, 540, 381, 31))
        self.pushButtonLoadLayer.setObjectName(_fromUtf8("pushButtonLoadLayer"))
        self.horizontalLayoutWidget = QtGui.QWidget(FloodRisk)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 580, 721, 31))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.progressBar = QtGui.QProgressBar(self.horizontalLayoutWidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setAlignment(QtCore.Qt.AlignHCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtGui.QProgressBar.TopToBottom)
        self.progressBar.setFormat(_fromUtf8(""))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.horizontalLayout.addWidget(self.progressBar)
        self.buttonBox = QtGui.QDialogButtonBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Help)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout.addWidget(self.buttonBox)
        self.toolButtonEsegui_2 = QtGui.QToolButton(FloodRisk)
        self.toolButtonEsegui_2.setGeometry(QtCore.QRect(540, 540, 191, 31))
        self.toolButtonEsegui_2.setObjectName(_fromUtf8("toolButtonEsegui_2"))
        self.groupBox = QtGui.QGroupBox(FloodRisk)
        self.groupBox.setGeometry(QtCore.QRect(10, 300, 721, 101))
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox {border: 1px solid gray; border-radius: 5px; margin-top: 7px; margin-bottom: 7px; padding: 0px} QGroupBox::title {top:-7 ex;left: 10px; subcontrol-origin: border}"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 461, 31))
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 60, 421, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(500, 30, 211, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(500, 10, 221, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.groupBox_3 = QtGui.QGroupBox(FloodRisk)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 400, 721, 141))
        self.groupBox_3.setStyleSheet(_fromUtf8("QGroupBox {border: 1px solid gray; border-radius: 5px; margin-top: 7px; margin-bottom: 7px; padding: 0px} QGroupBox::title {top:-7 ex;left: 10px; subcontrol-origin: border}"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButtonIstogrammi = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonIstogrammi.setGeometry(QtCore.QRect(650, 90, 61, 31))
        self.pushButtonIstogrammi.setText(_fromUtf8(""))
        self.pushButtonIstogrammi.setIconSize(QtCore.QSize(30, 25))
        self.pushButtonIstogrammi.setObjectName(_fromUtf8("pushButtonIstogrammi"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 301, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 301, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_green_pop = QtGui.QLabel(self.groupBox_3)
        self.label_green_pop.setGeometry(QtCore.QRect(670, 40, 21, 21))
        self.label_green_pop.setText(_fromUtf8(""))
        self.label_green_pop.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Users/asus/Desktop/Progetto Tesi Laurea/green20.png")))
        self.label_green_pop.setObjectName(_fromUtf8("label_green_pop"))
        self.label_red_pop = QtGui.QLabel(self.groupBox_3)
        self.label_red_pop.setEnabled(True)
        self.label_red_pop.setGeometry(QtCore.QRect(670, 40, 21, 21))
        self.label_red_pop.setText(_fromUtf8(""))
        self.label_red_pop.setPixmap(QtGui.QPixmap(_fromUtf8("../../../../Users/asus/Desktop/Progetto Tesi Laurea/red20.png")))
        self.label_red_pop.setObjectName(_fromUtf8("label_red_pop"))
        self.txtShellFilePath_4 = QtGui.QLineEdit(self.groupBox_3)
        self.txtShellFilePath_4.setGeometry(QtCore.QRect(10, 40, 631, 26))
        self.txtShellFilePath_4.setObjectName(_fromUtf8("txtShellFilePath_4"))
        self.pushButtonView_2 = QtGui.QPushButton(self.groupBox_3)
        self.pushButtonView_2.setGeometry(QtCore.QRect(580, 90, 61, 31))
        self.pushButtonView_2.setText(_fromUtf8(""))
        self.pushButtonView_2.setIconSize(QtCore.QSize(30, 25))
        self.pushButtonView_2.setObjectName(_fromUtf8("pushButtonView_2"))
        self.txtShellFilePath_7 = QtGui.QLineEdit(self.groupBox_3)
        self.txtShellFilePath_7.setGeometry(QtCore.QRect(10, 90, 561, 26))
        self.txtShellFilePath_7.setObjectName(_fromUtf8("txtShellFilePath_7"))
        self.groupBox_2 = QtGui.QGroupBox(FloodRisk)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 721, 291))
        self.groupBox_2.setStyleSheet(_fromUtf8("QGroupBox {border: 1px solid gray; border-radius: 5px; margin-top: 7px; margin-bottom: 7px; padding: 0px} QGroupBox::title {top:-7 ex;left: 10px; subcontrol-origin: border}"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.txtShellFilePath_3 = QtGui.QLineEdit(self.groupBox_2)
        self.txtShellFilePath_3.setGeometry(QtCore.QRect(10, 150, 621, 26))
        self.txtShellFilePath_3.setObjectName(_fromUtf8("txtShellFilePath_3"))
        self.btnChooseShellFile_3 = QtGui.QPushButton(self.groupBox_2)
        self.btnChooseShellFile_3.setGeometry(QtCore.QRect(640, 150, 61, 28))
        self.btnChooseShellFile_3.setText(_fromUtf8(""))
        self.btnChooseShellFile_3.setIconSize(QtCore.QSize(30, 25))
        self.btnChooseShellFile_3.setObjectName(_fromUtf8("btnChooseShellFile_3"))
        self.txtShellFilePath = QtGui.QLineEdit(self.groupBox_2)
        self.txtShellFilePath.setEnabled(False)
        self.txtShellFilePath.setGeometry(QtCore.QRect(10, 50, 621, 26))
        self.txtShellFilePath.setObjectName(_fromUtf8("txtShellFilePath"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 230, 301, 18))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.txtShellFilePath_tempi = QtGui.QLineEdit(self.groupBox_2)
        self.txtShellFilePath_tempi.setGeometry(QtCore.QRect(10, 250, 621, 26))
        self.txtShellFilePath_tempi.setObjectName(_fromUtf8("txtShellFilePath_tempi"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 301, 18))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 301, 18))
        self.label.setObjectName(_fromUtf8("label"))
        self.txtShellFilePath_velocita = QtGui.QLineEdit(self.groupBox_2)
        self.txtShellFilePath_velocita.setGeometry(QtCore.QRect(10, 200, 621, 26))
        self.txtShellFilePath_velocita.setObjectName(_fromUtf8("txtShellFilePath_velocita"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 301, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.txtShellFilePath_2 = QtGui.QLineEdit(self.groupBox_2)
        self.txtShellFilePath_2.setEnabled(False)
        self.txtShellFilePath_2.setGeometry(QtCore.QRect(10, 100, 621, 26))
        self.txtShellFilePath_2.setObjectName(_fromUtf8("txtShellFilePath_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 301, 18))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnChooseShellFile_velocita = QtGui.QPushButton(self.groupBox_2)
        self.btnChooseShellFile_velocita.setGeometry(QtCore.QRect(640, 200, 61, 28))
        self.btnChooseShellFile_velocita.setText(_fromUtf8(""))
        self.btnChooseShellFile_velocita.setIconSize(QtCore.QSize(30, 25))
        self.btnChooseShellFile_velocita.setObjectName(_fromUtf8("btnChooseShellFile_velocita"))
        self.btnChooseShellFile_tempi = QtGui.QPushButton(self.groupBox_2)
        self.btnChooseShellFile_tempi.setGeometry(QtCore.QRect(640, 250, 61, 28))
        self.btnChooseShellFile_tempi.setText(_fromUtf8(""))
        self.btnChooseShellFile_tempi.setIconSize(QtCore.QSize(30, 25))
        self.btnChooseShellFile_tempi.setObjectName(_fromUtf8("btnChooseShellFile_tempi"))

        self.retranslateUi(FloodRisk)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FloodRisk.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FloodRisk.reject)
        QtCore.QMetaObject.connectSlotsByName(FloodRisk)

    def retranslateUi(self, FloodRisk):
        FloodRisk.setWindowTitle(_translate("FloodRisk", "FloodRisk | Loss of Life (LOL) Scenario", None))
        self.pushButtonSalvaProgetto.setText(_translate("FloodRisk", "Save Project", None))
        self.pushButtonLoadLayer.setText(_translate("FloodRisk", "Add all Layers to Map Canvas", None))
        self.toolButtonEsegui_2.setText(_translate("FloodRisk", "Run Simulation", None))
        self.groupBox.setTitle(_translate("FloodRisk", "Set Methodology", None))
        self.radioButton.setText(_translate("FloodRisk", "Dam Failure Scenarios - U.S. Department of Homeland Security", None))
        self.radioButton_2.setText(_translate("FloodRisk", "SUFRI: Methodology for pluvial and river flooding risk", None))
        self.label_16.setText(_translate("FloodRisk", "Set Understanding", None))
        self.groupBox_3.setTitle(_translate("FloodRisk", "Output Data", None))
        self.label_4.setText(_translate("FloodRisk", "Population at Risk Layer:", None))
        self.label_8.setText(_translate("FloodRisk", "Global Summary Table:", None))
        self.groupBox_2.setTitle(_translate("FloodRisk", "Set Input Data", None))
        self.label_10.setText(_translate("FloodRisk", "Warning Time Vector Layer:", None))
        self.label_9.setText(_translate("FloodRisk", "Flow Velocity Raster Layer:", None))
        self.label.setText(_translate("FloodRisk", "Project (.dmg) File:", None))
        self.label_3.setText(_translate("FloodRisk", "Water Depth Raster Layer:", None))
        self.label_2.setText(_translate("FloodRisk", "SpatiaLite Geodatabase:", None))

