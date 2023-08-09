#PYQT Imports 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QLineEdit, QPushButton, QWidget, QHBoxLayout, QComboBox, QStyledItemDelegate, QTableWidgetItem, QAbstractItemView
from PyQt5.Qt import Qt
from PyQt5.QtCore import QObject, pyqtSlot, QDateTime

import sys 
import os 
import signal

from GUI.rover import Ui_MainWindow 
from Modules.utilities import *
from Pre_Generate.processing import * 

from Post_Generate.excel import *
from Post_Generate.cannabisReport import *
from Post_Generate.pesticidesReport import *
from Post_Generate.mushroomReport import *;

REPORT_TYPES = ['', 'THC', 'Pesticides/Toxins', 'Mushrooms']


class MainWindow(QMainWindow): 

    def __init__(self): 
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App"); 
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.defineReportType()
        self.ui.generateReportBtn.setVisible(False)
        self.ui.pages.setCurrentIndex(0)
        self.ui.reportsInfo.hide()
        self.showMaximized()
 
    #Page Buttons 
    @pyqtSlot()
    def on_createReportPageBtn_clicked(self): 
        self.ui.pages.setCurrentIndex(0)
        
    @pyqtSlot()
    def on_settingsBtn_clicked(self): 
        self.ui.pages.setCurrentIndex(2);
         
    #Page Stack  
    def on_pages_currentChanged(self, index): 
        if(index == 0): 
            self.ui.headerLabel.setText("Create Report") 
           
        if(index == 1): 
            self.clearReportPage(); 
            self.ui.generateReportBtn.setVisible(True)
            self.ui.reportsInfo.show()
            
            selected_report = self.ui.reportSelector.currentText() 
            self.ui.headerLabel.setText(selected_report + ' Report') 
 
            
            
            
        else: 
            self.ui.generateReportBtn.setVisible(False)
            self.ui.reportsInfo.hide()
        if(index == 2): 
            self.ui.headerLabel.setText("Settings")  
            self.loadSettings()
    
    #Create Report Page 
    def defineReportType(self): 
        
        self.ui.reportSelector.clear()
        self.ui.reportSelector.addItems(REPORT_TYPES)
        
    
    @pyqtSlot() 
    def on_browseFileBtn_clicked(self): 
        fileLocation = openFile()

        if(fileLocation): 
            self.ui.fileLocationLabel.setText(fileLocation)
            self.fileLocation = fileLocation

    
    @pyqtSlot()
    def on_proceedBtn_clicked(self): 
        
        #TODO: check if is .xslx file
        errorChecks = [0,0]
        
        reportType = self.ui.reportSelector.currentText()
        fileLocation = self.ui.fileLocationLabel.text()
        
        if(reportType != ''): 
            errorChecks[0] = 0
        else: 
            errorChecks[0] = 1; 
            
        if(fileLocation != ''): 
            errorChecks[1] = 0 
        else: 
            errorChecks[1] = 1; 
        
        if(sum(errorChecks) == 0): 
            self.ui.pages.setCurrentIndex(1);
            self.resetCreateReportPage()
            self.reportPage(reportType, fileLocation)
        else: 
            #TODO: error box 
            print("Please Try Again")
        
    def resetCreateReportPage(self): 
        self.ui.fileLocationLabel.setText('')
        self.ui.reportSelector.setCurrentIndex(0)

    
    def reportPage(self, reportType, fileLocation): 
        self.reportType = reportType
        self.fileName = fileLocation
        print('Report Type: ', reportType)
        print('File Location: ', fileLocation)

        self.ui.clientTable.horizontalHeader().setDefaultSectionSize(100)
        self.ui.clientTable.verticalHeader().setDefaultSectionSize(30)
        self.ui.fileNameLabel.setText(fileLocation) 
        
        if(reportType == 'THC'): 
            print('running THC scan')
            self.ui.headerLabel.setText('THC Report')
            self.prepareThcReport(fileLocation)
            
        else: 
            self.ui.headerLabel.setText('Pesticides and Toxins Report')
            print('Scanning pesticdes/toxins report')
            self.preparePestReport(fileLocation) 

    
    
    def prepareThcReport(self, fileLocaiton): 
        print('Prepare THC Report')
        self.jobNums, self.recovery, sampleData2, self.sampleData = scanTHC(fileLocaiton)
        #print('Recovery:', self.recovery)
        
        self.populateClientInfo(self.jobNums);
        self.thcSampleSet(self.sampleData); 
    
    
    def preparePestReport(self, fileLocation): 
        print('Prepare Pestcides/Toxins Report')
        print(fileExtenCheck(self.fileLocation))
        
        self.jobNums, self.sampleNumbers, self.sampleData, self.recovery = scanPest(self.fileLocation)
        self.populateClientInfo(self.jobNums)
        self.pesticidesSampleSet(self.sampleNumbers)

    
    
    #TODO: when the client is None, define all the values as being blank 
    #TODO: redo the processing information
    def populateClientInfo(self, jobNums): 
        print('**Job Numbers')
        print(jobNums)
        
        totalJobs = len(jobNums)
        jobsInfoLocation = {}
        self.clientInfo = {}
        self.sampleNames = {}
        
        for job in jobNums: 
            location = scanForTXTFolders(job)
            jobsInfoLocation[job] = location
        
        for key, value in jobsInfoLocation.items(): 
            print(key, value)
            
            
            temp, sampelNames = processClientInfo(key, value)
            self.sampleNames[key] = sampelNames
            self.clientInfo[key] = temp; 

                
        self.ui.clientTable.setColumnCount(totalJobs)
        self.ui.clientTable.setHorizontalHeaderLabels(jobNums)
        
        currentColumn = 0; 
        defaultWidth = 200
        
        for key, value in self.clientInfo.items(): 
            print(key, value) 
            if(value != None): 
                for index, (key2,value2) in enumerate(value.items()): 
                    item = QTableWidgetItem(value2)
                    self.ui.clientTable.setItem(index, currentColumn, item)
            
            currentColumn+= 1; 
            

        for column in range(self.ui.clientTable.columnCount()):
            self.ui.clientTable.setColumnWidth(column, defaultWidth) 
            
        #self.ui.clientTable.resizeColumnsToContents() 
        
        print('**Client Info')
        for key, value in self.clientInfo.items(): 
            print(key, value )
            
        print('**Sample Names')
        for key, value in self.sampleNames.items(): 
            print(key, value)
         
    def thcSampleSet(self, sampleData): 
   
        print('**Sample Names')
        for key, value in self.sampleNames.items():
            print(key, value)
        
        horizontalHeaders = ['Sample Number', 'Units', 'Baisc/Deluxe', 'Single/Multi', 'De/Un/Mo', 'Unit Value','Sample Name']; 
        unitItems = ['mg/g & Percent (Moisture)', 'mg/mL & Percent (Density)', 'mg/unit & mg/g (Unit Mass)', 'Percent Only' ]
        reportType = ['Basic Report', 'Deluxe Report']
        batch = ['Multi', 'Single']
        
        self.ui.tableWidget.setColumnCount(len(horizontalHeaders))
        self.ui.tableWidget.setHorizontalHeaderLabels(horizontalHeaders)
        
        for key, value in sampleData.items(): 
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            
            item = QTableWidgetItem(str(key))
            self.ui.tableWidget.setItem(row, 0, item)
            self.addComboBox(row, 1, unitItems)
            self.addComboBox(row, 2, reportType)
            self.addComboBox(row, 3, batch)
            
            try: 
                sampleName = self.sampleNames[key[:6]][key]
                sampleName  = re.sub(r"\s+", " ", sampleName.strip())
                item2 = QTableWidgetItem(sampleName)
                self.ui.tableWidget.setItem(row, 6, item2)
                
            except: 
                print('Error getting sample names') 
            
        
        self.ui.tableWidget.resizeColumnsToContents()  
        self.ui.tableWidget.setColumnWidth(0, 150)
        self.ui.tableWidget.setColumnWidth(1, 200)

        for i in range(3): 
            self.ui.tableWidget.setColumnWidth(3+i, 150) 
            
        self.ui.tableWidget.setColumnWidth(4, 250); 
        
        
    def pesticidesSampleSet(self, sampleNumbers): 
        #TODO: can process the type as well from the file 
        #TODO: resize the sample Names Section 
        #TODO: are sample names getting changed and relabled when we edit them? 
        
        horizontalHeaders = ['Sample Number', 'Type', 'Toxins', 'Single/Multi', 'Sample Name']
        pestType = ['Bud', 'Oil', 'Paper'] 
        toxinType = ['Pesticides', 'Toxins Only', 'Both']
        batchType = ['Multi', 'Single']
        
        self.ui.tableWidget.setColumnCount(len(horizontalHeaders))
        self.ui.tableWidget.setHorizontalHeaderLabels(horizontalHeaders)
        
        for sampleNumber in sampleNumbers: 
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            
            item = QTableWidgetItem(str(sampleNumber))
            self.ui.tableWidget.setItem(row, 0, item)

            self.addComboBox(row, 1, pestType)
            self.addComboBox(row, 2, toxinType)
            self.addComboBox(row, 3, batchType)
            
            try: 
                sampleName = self.sampleNames[sampleNumber[:6]][sampleNumber] 
                sampleName  = re.sub(r"\s+", " ", sampleName.strip())
                
                item2 = QTableWidgetItem(sampleName)
                self.ui.tableWidget.setItem(row, 4, item2)
                
            except: 
                print('Error getting sample names')
            
            #self.ui.tableWidget.resizeColumnsToContents()  
            defaultWidth = 150
            sampleNumberWidth = 100
            sampleNameWidth = 250
            
            for i in range(5): 
                self.ui.tableWidget.setColumnWidth(i, defaultWidth) 
    
                if(i == 0): 
                    self.ui.tableWidget.setColumnWidth(i, sampleNumberWidth)
                if(i == 4):
                    self.ui.tableWidget.setColumnWidth(i, sampleNameWidth)
        
    def addComboBox(self, row, col, items):
        combo = QComboBox()
        combo.addItems(items)
        self.ui.tableWidget.setCellWidget(row, col, combo)
        
    @pyqtSlot()  
    def on_generateReportBtn_clicked(self): 
    
        if(self.reportType == 'THC'):
            #print('****Generating THC Report')
            textSections = [0,4,5,6]
            sampleInfo = self.getSampleInfo(textSections)
            generateThcReport(self.jobNums, self.clientInfo, sampleInfo, self.sampleData, self.recovery, self.fileName)
        else: 
            #print('****Generating Potency and Toxins Report') 
            textSections = [0,4]
            sampleInfo = self.getSampleInfo(textSections)
            generatePestReport(self.jobNums, self.clientInfo, self.sampleNames, sampleInfo, self.sampleData, self.recovery, self.fileName)
            
                        
    #TODO: if sample name is blank just give it the sample number instead
    def getSampleInfo(self, textSections): 

        sampleInfo = {}
                
        for row in range(self.ui.tableWidget.rowCount()):
            currentSampleRowInfo = []
            
            for column in range(self.ui.tableWidget.columnCount()): 
                if(column in textSections): 
                    item = self.ui.tableWidget.item(row, column)
                    if item is not None:
                        currentSampleRowInfo.append(item.text())
                    else: 
                        currentSampleRowInfo.append('')
                else: 
                    combo = self.ui.tableWidget.cellWidget(row, column)
                    if combo is not None:
                        combo_box = self.ui.tableWidget.cellWidget(row, column)
                        current_text = combo_box.currentText()
                        currentSampleRowInfo.append(current_text)
                    else: 
                        currentSampleRowInfo.append('')
            
            sampleName = currentSampleRowInfo[0] 
            sampleInfo[sampleName] = currentSampleRowInfo;
            
        print('**Sample Infomration')
        for key, value in sampleInfo.items(): 
            print(key, value) 
            
        return sampleInfo; 
    
    
    def clearReportPage(self): 
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(0)
        self.ui.tableWidget.setHorizontalHeaderLabels([])
        self.ui.clientTable.clearContents()
        self.ui.clientTable.setColumnCount(0)
        self.ui.clientTable.setHorizontalHeaderLabels([])
        
    
    def updateClientInfo(self): 
        pass; 
        

    #Settings Page 
    @pyqtSlot() 
    def on_saveOutputBtn_clicked(self): 
        self.setFile('output')
        
    @pyqtSlot()
    def on_saveTxtBtn_clicked(self): 
        self.setFile('txtLocation')
        
    #TODO: update the output change
    def setFile(self, fileName): 

        location = getFileLocation()
        locations = loadLocations()
        locations[fileName] = location
        #saveLocation(locations)

        if(locations != ''): 
            saveLocation(locations)

    def loadSettings(self): 
        locations = loadLocations(); 
    
        if(locations == None): 
            pass; 
            print("No Stuff")
            
        else: 
            
            print(locations)
            self.ui.reportOutputLabel.setText(locations['output'])
            self.ui.txtLocationLabel.setText(locations['txtLocation'])
        
    @pyqtSlot()
    def on_loqBtn_clicked(self): 
        
       updateLOQ(); 
        
        
        