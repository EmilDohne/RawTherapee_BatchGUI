# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(641, 531)
        Form.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(20,20,20);\n"
"	font: 10pt \"Consolas\"; \n"
"	color: rgb(201,201,201);\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	background-color: rgb(30, 30, 30);\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	min-height: 25px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: rgb(201, 201, 201);\n"
"	border: none;\n"
"	border-radius: 12px;\n"
"	min-height: 25px;\n"
"	color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLabel {\n"
"	min-width: 150px;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.mainLayoutInner = QVBoxLayout()
        self.mainLayoutInner.setSpacing(9)
        self.mainLayoutInner.setObjectName(u"mainLayoutInner")
        self.mainLayoutInner.setContentsMargins(9, 9, 6, 9)
        self.inputHLayout = QHBoxLayout()
        self.inputHLayout.setObjectName(u"inputHLayout")
        self.inputHLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(150, 0))

        self.inputHLayout.addWidget(self.label)

        self.inputLineEdit = QLineEdit(Form)
        self.inputLineEdit.setObjectName(u"inputLineEdit")

        self.inputHLayout.addWidget(self.inputLineEdit)


        self.mainLayoutInner.addLayout(self.inputHLayout)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayoutInner.addItem(self.verticalSpacer)

        self.outputHLayout = QHBoxLayout()
        self.outputHLayout.setObjectName(u"outputHLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(150, 0))

        self.outputHLayout.addWidget(self.label_2)

        self.outputLineEdit = QLineEdit(Form)
        self.outputLineEdit.setObjectName(u"outputLineEdit")

        self.outputHLayout.addWidget(self.outputLineEdit)


        self.mainLayoutInner.addLayout(self.outputHLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"min-width: 130px;")

        self.horizontalLayout.addWidget(self.label_5)

        self.addFolderCheckBox = QCheckBox(Form)
        self.addFolderCheckBox.setObjectName(u"addFolderCheckBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addFolderCheckBox.sizePolicy().hasHeightForWidth())
        self.addFolderCheckBox.setSizePolicy(sizePolicy1)
        self.addFolderCheckBox.setChecked(True)

        self.horizontalLayout.addWidget(self.addFolderCheckBox)


        self.mainLayoutInner.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayoutInner.addItem(self.verticalSpacer_2)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"background-color: rgb(201, 201, 201);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.mainLayoutInner.addWidget(self.line)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayoutInner.addItem(self.verticalSpacer_3)

        self.profileHLayout = QHBoxLayout()
        self.profileHLayout.setObjectName(u"profileHLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(150, 0))

        self.profileHLayout.addWidget(self.label_3)

        self.processingProfileLineEdit = QLineEdit(Form)
        self.processingProfileLineEdit.setObjectName(u"processingProfileLineEdit")

        self.profileHLayout.addWidget(self.processingProfileLineEdit)


        self.mainLayoutInner.addLayout(self.profileHLayout)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayoutInner.addItem(self.verticalSpacer_5)

        self.rawHLayout = QHBoxLayout()
        self.rawHLayout.setObjectName(u"rawHLayout")
        self.rawHLayout.setContentsMargins(-1, -1, 0, 0)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(150, 0))

        self.rawHLayout.addWidget(self.label_4)

        self.rawFormatComboBox = QComboBox(Form)
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.addItem("")
        self.rawFormatComboBox.setObjectName(u"rawFormatComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.rawFormatComboBox.sizePolicy().hasHeightForWidth())
        self.rawFormatComboBox.setSizePolicy(sizePolicy2)

        self.rawHLayout.addWidget(self.rawFormatComboBox)


        self.mainLayoutInner.addLayout(self.rawHLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 217, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayoutInner.addItem(self.verticalSpacer_4)

        self.runHLayout = QHBoxLayout()
        self.runHLayout.setObjectName(u"runHLayout")
        self.runHLayout.setContentsMargins(-1, 0, -1, -1)
        self.statusLabel = QLabel(Form)
        self.statusLabel.setObjectName(u"statusLabel")

        self.runHLayout.addWidget(self.statusLabel)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.runHLayout.addItem(self.horizontalSpacer)

        self.runPushButton = QPushButton(Form)
        self.runPushButton.setObjectName(u"runPushButton")
        self.runPushButton.setMinimumSize(QSize(100, 25))

        self.runHLayout.addWidget(self.runPushButton)


        self.mainLayoutInner.addLayout(self.runHLayout)

        self.verticalSpacer_6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.mainLayoutInner.addItem(self.verticalSpacer_6)

        self.progressHLayout = QHBoxLayout()
        self.progressHLayout.setObjectName(u"progressHLayout")
        self.progressHLayout.setContentsMargins(-1, -1, -1, 0)
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(30, 30, 30);\n"
"	border-radius: 5px;\n"
"	border: 0px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: rgb(201, 201, 201);\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.progressHLayout.addWidget(self.progressBar)

        self.progressLabel = QLabel(Form)
        self.progressLabel.setObjectName(u"progressLabel")
        self.progressLabel.setMinimumSize(QSize(50, 0))
        self.progressLabel.setStyleSheet(u"min-width: 50;")
        self.progressLabel.setAlignment(Qt.AlignCenter)

        self.progressHLayout.addWidget(self.progressLabel)


        self.mainLayoutInner.addLayout(self.progressHLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.sysOutLabel = QLabel(Form)
        self.sysOutLabel.setObjectName(u"sysOutLabel")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sysOutLabel.sizePolicy().hasHeightForWidth())
        self.sysOutLabel.setSizePolicy(sizePolicy3)
        self.sysOutLabel.setMinimumSize(QSize(150, 0))
        self.sysOutLabel.setStyleSheet(u"")
        self.sysOutLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout_2.addWidget(self.sysOutLabel)


        self.mainLayoutInner.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.mainLayoutInner)


        self.retranslateUi(Form)

        self.rawFormatComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Input Directory:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Output Directory:", None))
#if QT_CONFIG(tooltip)
        self.label_5.setToolTip(QCoreApplication.translate("Form", u"Create an extra subfolder for each valid input folder. \n"
"E.g. if an input folder is /<Input>/HDRI_01 the output will be /<Output>/HDRI_01/HDRI_01", None))
#endif // QT_CONFIG(tooltip)
        self.label_5.setText(QCoreApplication.translate("Form", u"Create Subfolder", None))
        self.addFolderCheckBox.setText("")
#if QT_CONFIG(tooltip)
        self.label_3.setToolTip(QCoreApplication.translate("Form", u"RawTherapee Processing file (*.pp3). If empty, default is used", None))
#endif // QT_CONFIG(tooltip)
        self.label_3.setText(QCoreApplication.translate("Form", u"Processing Profile:", None))
#if QT_CONFIG(tooltip)
        self.processingProfileLineEdit.setToolTip(QCoreApplication.translate("Form", u"RawTherapee Processing file (*.pp3). If empty, default is used", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_4.setToolTip(QCoreApplication.translate("Form", u"Specify which raw file format to look for, based on valid files for RawTherapee", None))
#endif // QT_CONFIG(tooltip)
        self.label_4.setText(QCoreApplication.translate("Form", u"RAW File Format:", None))
        self.rawFormatComboBox.setItemText(0, QCoreApplication.translate("Form", u"3FR", None))
        self.rawFormatComboBox.setItemText(1, QCoreApplication.translate("Form", u"ARW", None))
        self.rawFormatComboBox.setItemText(2, QCoreApplication.translate("Form", u"ARQ", None))
        self.rawFormatComboBox.setItemText(3, QCoreApplication.translate("Form", u"CR2", None))
        self.rawFormatComboBox.setItemText(4, QCoreApplication.translate("Form", u"CR3", None))
        self.rawFormatComboBox.setItemText(5, QCoreApplication.translate("Form", u"CRF", None))
        self.rawFormatComboBox.setItemText(6, QCoreApplication.translate("Form", u"CRW", None))
        self.rawFormatComboBox.setItemText(7, QCoreApplication.translate("Form", u"DCR", None))
        self.rawFormatComboBox.setItemText(8, QCoreApplication.translate("Form", u"DNG", None))
        self.rawFormatComboBox.setItemText(9, QCoreApplication.translate("Form", u"FFF", None))
        self.rawFormatComboBox.setItemText(10, QCoreApplication.translate("Form", u"IIQ", None))
        self.rawFormatComboBox.setItemText(11, QCoreApplication.translate("Form", u"KDC", None))
        self.rawFormatComboBox.setItemText(12, QCoreApplication.translate("Form", u"MEF", None))
        self.rawFormatComboBox.setItemText(13, QCoreApplication.translate("Form", u"MOS", None))
        self.rawFormatComboBox.setItemText(14, QCoreApplication.translate("Form", u"MRW", None))
        self.rawFormatComboBox.setItemText(15, QCoreApplication.translate("Form", u"NEF", None))
        self.rawFormatComboBox.setItemText(16, QCoreApplication.translate("Form", u"NRW", None))
        self.rawFormatComboBox.setItemText(17, QCoreApplication.translate("Form", u"ORF", None))
        self.rawFormatComboBox.setItemText(18, QCoreApplication.translate("Form", u"PEF", None))
        self.rawFormatComboBox.setItemText(19, QCoreApplication.translate("Form", u"RAF", None))
        self.rawFormatComboBox.setItemText(20, QCoreApplication.translate("Form", u"RAW", None))
        self.rawFormatComboBox.setItemText(21, QCoreApplication.translate("Form", u"RW2", None))
        self.rawFormatComboBox.setItemText(22, QCoreApplication.translate("Form", u"RWL", None))
        self.rawFormatComboBox.setItemText(23, QCoreApplication.translate("Form", u"RWZ", None))
        self.rawFormatComboBox.setItemText(24, QCoreApplication.translate("Form", u"SR2", None))
        self.rawFormatComboBox.setItemText(25, QCoreApplication.translate("Form", u"SRW", None))

#if QT_CONFIG(tooltip)
        self.rawFormatComboBox.setToolTip(QCoreApplication.translate("Form", u"Specify which raw file format to look for, based on valid files for RawTherapee", None))
#endif // QT_CONFIG(tooltip)
        self.statusLabel.setText("")
        self.runPushButton.setText(QCoreApplication.translate("Form", u"Run", None))
        self.progressLabel.setText(QCoreApplication.translate("Form", u"0/0", None))
#if QT_CONFIG(tooltip)
        self.sysOutLabel.setToolTip(QCoreApplication.translate("Form", u"Program output window", None))
#endif // QT_CONFIG(tooltip)
        self.sysOutLabel.setText("")
    # retranslateUi

