# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rover.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1377, 890)
        MainWindow.setMinimumSize(QtCore.QSize(1377, 768))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 100))
        self.centralwidget.setStyleSheet("#sidebar {\n"
"    background-color:black; \n"
"\n"
"}\n"
"\n"
"#sidebar QPushButton {\n"
"    color:white; \n"
"    text-align:left; \n"
"    \n"
"    border: none; \n"
"    padding:2px; \n"
"}\n"
"\n"
"#sidebar QPushButton:hover {\n"
"    border-radius: 5px; \n"
"    background-color:grey; \n"
"}\n"
"\n"
"\n"
"#sidebarTitle {\n"
"    color: white;  \n"
"    font-size: 22px;\n"
"      font-weight: bold;\n"
"      text-transform: uppercase;\n"
"}\n"
"\n"
"\n"
"#dashboardText {\n"
"    color:grey;\n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color:#f5f6f7; \n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sidebar = QtWidgets.QWidget(self.centralwidget)
        self.sidebar.setMinimumSize(QtCore.QSize(200, 0))
        self.sidebar.setMaximumSize(QtCore.QSize(200, 16777215))
        self.sidebar.setObjectName("sidebar")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sidebar)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.sidebarTitle = QtWidgets.QLabel(self.sidebar)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.sidebarTitle.setFont(font)
        self.sidebarTitle.setObjectName("sidebarTitle")
        self.verticalLayout_3.addWidget(self.sidebarTitle)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.dashboardText = QtWidgets.QLabel(self.sidebar)
        self.dashboardText.setObjectName("dashboardText")
        self.verticalLayout_3.addWidget(self.dashboardText)
        self.createReportPageBtn = QtWidgets.QPushButton(self.sidebar)
        self.createReportPageBtn.setCheckable(True)
        self.createReportPageBtn.setObjectName("createReportPageBtn")
        self.verticalLayout_3.addWidget(self.createReportPageBtn)
        self.historyBtn = QtWidgets.QPushButton(self.sidebar)
        self.historyBtn.setCheckable(True)
        self.historyBtn.setObjectName("historyBtn")
        self.verticalLayout_3.addWidget(self.historyBtn)
        self.settingsBtn = QtWidgets.QPushButton(self.sidebar)
        self.settingsBtn.setCheckable(True)
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_3.addWidget(self.settingsBtn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.sidebar)
        self.mainBody = QtWidgets.QWidget(self.centralwidget)
        self.mainBody.setStyleSheet("#header {\n"
"    background-color: white; \n"
"    box-shadow: 0 4px 4px rgba(0, 0, 0, 0.4);\n"
"}\n"
"\n"
"#header QLabel {\n"
"    color:black; \n"
"}\n"
"\n"
"#header > QPushButton {\n"
"    color: white; \n"
"    background-color:#87c869;\n"
"    padding:6px; \n"
"    border-radius: 5px\n"
"}\n"
"#header > QPushButton:hover {\n"
"    background-color:green; \n"
"} \n"
"\n"
"#pages {\n"
"    background-color:#f5f6f7;  \n"
"    margin:0 15 0 15; \n"
"    \n"
"}\n"
"#pages > QWidget{\n"
"    background-color:white; \n"
"    border-radius: 10px\n"
"}")
        self.mainBody.setObjectName("mainBody")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainBody)
        self.verticalLayout.setContentsMargins(0, 0, 0, 12)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QWidget(self.mainBody)
        self.header.setMinimumSize(QtCore.QSize(0, 80))
        self.header.setMaximumSize(QtCore.QSize(16777215, 110))
        self.header.setObjectName("header")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_9.setContentsMargins(20, 0, -1, 8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.widget_8 = QtWidgets.QWidget(self.header)
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 100))
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.headerLabel = QtWidgets.QLabel(self.widget_8)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.headerLabel.setFont(font)
        self.headerLabel.setStyleSheet("")
        self.headerLabel.setObjectName("headerLabel")
        self.verticalLayout_8.addWidget(self.headerLabel)
        self.reportsInfo = QtWidgets.QWidget(self.widget_8)
        self.reportsInfo.setObjectName("reportsInfo")
        self.formLayout = QtWidgets.QFormLayout(self.reportsInfo)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 2, 0, 2)
        self.formLayout.setObjectName("formLayout")
        self.subtitle2 = QtWidgets.QLabel(self.reportsInfo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subtitle2.setFont(font)
        self.subtitle2.setObjectName("subtitle2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.subtitle2)
        self.totalTestsLabel = QtWidgets.QLabel(self.reportsInfo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.totalTestsLabel.setFont(font)
        self.totalTestsLabel.setObjectName("totalTestsLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.totalTestsLabel)
        self.subTitle1 = QtWidgets.QLabel(self.reportsInfo)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.subTitle1.setFont(font)
        self.subTitle1.setObjectName("subTitle1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.subTitle1)
        self.fileNameLabel = QtWidgets.QLabel(self.reportsInfo)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fileNameLabel)
        self.verticalLayout_8.addWidget(self.reportsInfo)
        self.horizontalLayout_9.addWidget(self.widget_8)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem3)
        self.generateReportBtn = QtWidgets.QPushButton(self.header)
        self.generateReportBtn.setObjectName("generateReportBtn")
        self.horizontalLayout_9.addWidget(self.generateReportBtn)
        self.verticalLayout.addWidget(self.header)
        self.pages = QtWidgets.QStackedWidget(self.mainBody)
        self.pages.setObjectName("pages")
        self.CreateReport = QtWidgets.QWidget()
        self.CreateReport.setStyleSheet("#dataEntryWidget {\n"
"    border: 2px solid grey; \n"
"    border-radius: 5px;\n"
"    \n"
"    \n"
"}\n"
"\n"
"#proceedBtn {\n"
"    background-color:#87c869;\n"
"    color:white; \n"
"    padding:5px; \n"
"}")
        self.CreateReport.setObjectName("CreateReport")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.CreateReport)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.CreateReport)
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.container = QtWidgets.QWidget(self.widget)
        self.container.setObjectName("container")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.container)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem5)
        self.dataEntryWidget = QtWidgets.QWidget(self.container)
        self.dataEntryWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.dataEntryWidget.setObjectName("dataEntryWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dataEntryWidget)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.dataEntryWidget)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setRowWrapPolicy(QtWidgets.QFormLayout.DontWrapRows)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.reportSelector = QtWidgets.QComboBox(self.widget_3)
        self.reportSelector.setObjectName("reportSelector")
        self.reportSelector.addItem("")
        self.reportSelector.setItemText(0, "")
        self.reportSelector.addItem("")
        self.reportSelector.addItem("")
        self.reportSelector.addItem("")
        self.reportSelector.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reportSelector)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.groupBox = QtWidgets.QGroupBox(self.dataEntryWidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(-1, 0, -1, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.browseFileBtn = QtWidgets.QPushButton(self.groupBox)
        self.browseFileBtn.setObjectName("browseFileBtn")
        self.gridLayout.addWidget(self.browseFileBtn, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.widget_5 = QtWidgets.QWidget(self.dataEntryWidget)
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.fileLocationLabel = QtWidgets.QLineEdit(self.widget_5)
        self.fileLocationLabel.setReadOnly(True)
        self.fileLocationLabel.setObjectName("fileLocationLabel")
        self.horizontalLayout_5.addWidget(self.fileLocationLabel)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.proceedBtn = QtWidgets.QPushButton(self.dataEntryWidget)
        self.proceedBtn.setObjectName("proceedBtn")
        self.verticalLayout_2.addWidget(self.proceedBtn)
        self.verticalLayout_10.addWidget(self.dataEntryWidget)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem6)
        self.horizontalLayout_3.addWidget(self.container)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.widget)
        self.pages.addWidget(self.CreateReport)
        self.Report = QtWidgets.QWidget()
        self.Report.setObjectName("Report")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Report)
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.clientWidget = QtWidgets.QWidget(self.Report)
        self.clientWidget.setObjectName("clientWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.clientWidget)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.clientInfoLabel = QtWidgets.QLabel(self.clientWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.clientInfoLabel.setFont(font)
        self.clientInfoLabel.setStyleSheet("QWidget QTableWidget {\n"
"        background-color: lightgray;\n"
"        border: 1px solid gray;\n"
"}\n"
"    \n"
"QTableWidget::item {\n"
"        padding: 5px;\n"
"}\n"
"    \n"
"QTableWidget::item:selected {\n"
"        background-color: blue;\n"
"        color: white;\n"
"}")
        self.clientInfoLabel.setObjectName("clientInfoLabel")
        self.verticalLayout_5.addWidget(self.clientInfoLabel)
        self.clientTable = QtWidgets.QTableWidget(self.clientWidget)
        self.clientTable.setStyleSheet("QTableWidget {\n"
"        background-color: white;\n"
"        border: 1px solid gray;\n"
"}\n"
"    \n"
"QTableWidget::item {\n"
"        padding: 5px;\n"
"}\n"
"    \n"
"QTableWidget::item:selected {\n"
"        background-color: blue;\n"
"        color: white;\n"
"}")
        self.clientTable.setObjectName("clientTable")
        self.clientTable.setColumnCount(1)
        self.clientTable.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.clientTable.setHorizontalHeaderItem(0, item)
        self.clientTable.horizontalHeader().setCascadingSectionResizes(False)
        self.clientTable.horizontalHeader().setDefaultSectionSize(150)
        self.clientTable.horizontalHeader().setSortIndicatorShown(False)
        self.clientTable.horizontalHeader().setStretchLastSection(False)
        self.clientTable.verticalHeader().setDefaultSectionSize(21)
        self.clientTable.verticalHeader().setMinimumSectionSize(30)
        self.clientTable.verticalHeader().setSortIndicatorShown(False)
        self.clientTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.clientTable)
        self.verticalLayout_4.addWidget(self.clientWidget)
        self.SampleWidget = QtWidgets.QWidget(self.Report)
        self.SampleWidget.setMinimumSize(QtCore.QSize(0, 100))
        self.SampleWidget.setObjectName("SampleWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.SampleWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sampleLabel = QtWidgets.QLabel(self.SampleWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.sampleLabel.setFont(font)
        self.sampleLabel.setObjectName("sampleLabel")
        self.verticalLayout_6.addWidget(self.sampleLabel)
        self.tableWidget = QtWidgets.QTableWidget(self.SampleWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_6.addWidget(self.tableWidget)
        self.verticalLayout_4.addWidget(self.SampleWidget)
        self.pages.addWidget(self.Report)
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Settings)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.widget_7 = QtWidgets.QWidget(self.Settings)
        self.widget_7.setMinimumSize(QtCore.QSize(700, 0))
        self.widget_7.setStyleSheet("#widget_7 {\n"
"    border: 2px solid grey; \n"
"    border-radius: 5px;\n"
"}")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        self.widget_2 = QtWidgets.QWidget(self.widget_7)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.widget_2)
        self.label_11.setMinimumSize(QtCore.QSize(140, 0))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.reportOutputLabel = QtWidgets.QLineEdit(self.widget_2)
        self.reportOutputLabel.setReadOnly(True)
        self.reportOutputLabel.setObjectName("reportOutputLabel")
        self.horizontalLayout_7.addWidget(self.reportOutputLabel)
        self.saveOutputBtn = QtWidgets.QPushButton(self.widget_2)
        self.saveOutputBtn.setObjectName("saveOutputBtn")
        self.horizontalLayout_7.addWidget(self.saveOutputBtn)
        self.verticalLayout_7.addWidget(self.widget_2)
        self.widget_6 = QtWidgets.QWidget(self.widget_7)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        self.label_12.setMinimumSize(QtCore.QSize(140, 0))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.txtLocationLabel = QtWidgets.QLineEdit(self.widget_6)
        self.txtLocationLabel.setReadOnly(True)
        self.txtLocationLabel.setObjectName("txtLocationLabel")
        self.horizontalLayout_8.addWidget(self.txtLocationLabel)
        self.saveTxtBtn = QtWidgets.QPushButton(self.widget_6)
        self.saveTxtBtn.setObjectName("saveTxtBtn")
        self.horizontalLayout_8.addWidget(self.saveTxtBtn)
        self.verticalLayout_7.addWidget(self.widget_6)
        self.label_6 = QtWidgets.QLabel(self.widget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.widget_10 = QtWidgets.QWidget(self.widget_7)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.widget_10)
        self.label_5.setMinimumSize(QtCore.QSize(140, 0))
        self.label_5.setMaximumSize(QtCore.QSize(140, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.recoveryNameLabel = QtWidgets.QLineEdit(self.widget_10)
        self.recoveryNameLabel.setEnabled(False)
        self.recoveryNameLabel.setMinimumSize(QtCore.QSize(0, 0))
        self.recoveryNameLabel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.recoveryNameLabel.setObjectName("recoveryNameLabel")
        self.horizontalLayout_6.addWidget(self.recoveryNameLabel)
        self.setRecoveryName = QtWidgets.QPushButton(self.widget_10)
        self.setRecoveryName.setMinimumSize(QtCore.QSize(85, 0))
        self.setRecoveryName.setMaximumSize(QtCore.QSize(85, 16777215))
        self.setRecoveryName.setObjectName("setRecoveryName")
        self.horizontalLayout_6.addWidget(self.setRecoveryName)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_7.addWidget(self.widget_10)
        self.widget_11 = QtWidgets.QWidget(self.widget_7)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.widget_11)
        self.label_7.setMinimumSize(QtCore.QSize(140, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.stdSettingsVal = QtWidgets.QSpinBox(self.widget_11)
        self.stdSettingsVal.setMinimumSize(QtCore.QSize(100, 0))
        self.stdSettingsVal.setObjectName("stdSettingsVal")
        self.horizontalLayout_10.addWidget(self.stdSettingsVal)
        self.setStdBtn = QtWidgets.QPushButton(self.widget_11)
        self.setStdBtn.setMinimumSize(QtCore.QSize(85, 0))
        self.setStdBtn.setMaximumSize(QtCore.QSize(85, 16777215))
        self.setStdBtn.setObjectName("setStdBtn")
        self.horizontalLayout_10.addWidget(self.setStdBtn)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)
        self.verticalLayout_7.addWidget(self.widget_11)
        self.widget_9 = QtWidgets.QWidget(self.widget_7)
        self.widget_9.setObjectName("widget_9")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget_9)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_13 = QtWidgets.QLabel(self.widget_9)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.loqBtn = QtWidgets.QPushButton(self.widget_9)
        self.loqBtn.setMaximumSize(QtCore.QSize(100000, 16777215))
        self.loqBtn.setObjectName("loqBtn")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.loqBtn)
        self.verticalLayout_7.addWidget(self.widget_9)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem11)
        self.widget_12 = QtWidgets.QWidget(self.widget_7)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem12)
        self.saveSettingsBtn = QtWidgets.QPushButton(self.widget_12)
        self.saveSettingsBtn.setMinimumSize(QtCore.QSize(100, 0))
        self.saveSettingsBtn.setObjectName("saveSettingsBtn")
        self.horizontalLayout_11.addWidget(self.saveSettingsBtn)
        self.verticalLayout_7.addWidget(self.widget_12)
        self.horizontalLayout_4.addWidget(self.widget_7)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.pages.addWidget(self.Settings)
        self.historyPage = QtWidgets.QWidget()
        self.historyPage.setObjectName("historyPage")
        self.widget_4 = QtWidgets.QWidget(self.historyPage)
        self.widget_4.setGeometry(QtCore.QRect(210, 130, 531, 421))
        self.widget_4.setObjectName("widget_4")
        self.pages.addWidget(self.historyPage)
        self.verticalLayout.addWidget(self.pages)
        self.horizontalLayout.addWidget(self.mainBody)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1377, 22))
        self.menubar.setMinimumSize(QtCore.QSize(0, 0))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pages.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sidebarTitle.setText(_translate("MainWindow", "MB LABS LTD"))
        self.dashboardText.setText(_translate("MainWindow", "Dashboard"))
        self.createReportPageBtn.setText(_translate("MainWindow", "Create Report"))
        self.historyBtn.setText(_translate("MainWindow", "History"))
        self.settingsBtn.setText(_translate("MainWindow", "Settings"))
        self.headerLabel.setText(_translate("MainWindow", "REPORTS "))
        self.subtitle2.setText(_translate("MainWindow", "Total Jobs:"))
        self.totalTestsLabel.setText(_translate("MainWindow", "This ia a test label as"))
        self.subTitle1.setText(_translate("MainWindow", "FileName:"))
        self.fileNameLabel.setText(_translate("MainWindow", "This a a test label"))
        self.generateReportBtn.setText(_translate("MainWindow", "Generate Report"))
        self.label_2.setText(_translate("MainWindow", "Report Type "))
        self.reportSelector.setItemText(1, _translate("MainWindow", "THC "))
        self.reportSelector.setItemText(2, _translate("MainWindow", "Toxins "))
        self.reportSelector.setItemText(3, _translate("MainWindow", "Potency"))
        self.reportSelector.setItemText(4, _translate("MainWindow", "Mushrooms"))
        self.groupBox.setTitle(_translate("MainWindow", "Attach A File "))
        self.browseFileBtn.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Select a File"))
        self.label_4.setText(_translate("MainWindow", "File Location"))
        self.proceedBtn.setText(_translate("MainWindow", "Proceed"))
        self.clientInfoLabel.setText(_translate("MainWindow", "Client Information"))
        item = self.clientTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Client Name"))
        item = self.clientTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Date"))
        item = self.clientTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time"))
        item = self.clientTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Attention"))
        item = self.clientTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Address 1 "))
        item = self.clientTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Address 2 "))
        item = self.clientTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Address 3 "))
        item = self.clientTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "Sample Type "))
        item = self.clientTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "Sample Type 2 "))
        item = self.clientTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "Number of Samples"))
        item = self.clientTable.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "Recieve Temp"))
        item = self.clientTable.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "Telephone"))
        item = self.clientTable.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "Email"))
        item = self.clientTable.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "Fax "))
        item = self.clientTable.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "Payment Info"))
        item = self.clientTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Test"))
        self.sampleLabel.setText(_translate("MainWindow", "Sample Information"))
        self.label.setText(_translate("MainWindow", "File Locations"))
        self.label_11.setText(_translate("MainWindow", "Report output "))
        self.saveOutputBtn.setText(_translate("MainWindow", "browse"))
        self.label_12.setText(_translate("MainWindow", "TXT location "))
        self.saveTxtBtn.setText(_translate("MainWindow", "browse"))
        self.label_6.setText(_translate("MainWindow", "Preferences"))
        self.label_5.setText(_translate("MainWindow", "Recovery Name"))
        self.setRecoveryName.setText(_translate("MainWindow", "Set"))
        self.label_7.setText(_translate("MainWindow", "STD PPM (stdconc)"))
        self.setStdBtn.setText(_translate("MainWindow", "Set"))
        self.label_13.setText(_translate("MainWindow", "Update Potency Values"))
        self.loqBtn.setText(_translate("MainWindow", "update LOQ Files"))
        self.saveSettingsBtn.setText(_translate("MainWindow", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
