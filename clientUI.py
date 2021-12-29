# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finalui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from ftplib import FTP
import re
import sys
import tkinter as tk
from tkinter import filedialog 

class Ui_MainWindow(object):
	def __init__(self):
		self.IP = None
		self.Name_User = None
		self.Password_User = None
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(600, 594)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox.setGeometry(QtCore.QRect(380, 80, 191, 101))
		self.groupBox.setObjectName("groupBox")
		self.btninfoserver = QtWidgets.QPushButton(self.groupBox)
		self.btninfoserver.setGeometry(QtCore.QRect(10, 20, 81, 31))
		self.btninfoserver.setObjectName("btninfoserver")
		self.btnquit = QtWidgets.QPushButton(self.groupBox)
		self.btnquit.setGeometry(QtCore.QRect(40, 60, 111, 31))
		self.btnquit.setObjectName("btnquit")
		self.btnquit.clicked.connect(self.defquit)
		self.btnreturnfolder = QtWidgets.QPushButton(self.groupBox)
		self.btnreturnfolder.setGeometry(QtCore.QRect(90, 20, 81, 31))
		self.btnreturnfolder.setObjectName("btnreturnfolder")
		self.btnreturnfolder.clicked.connect(self.returnfolder)


		self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_2.setGeometry(QtCore.QRect(40, -1, 531, 71))
		self.groupBox_2.setObjectName("groupBox_2")
		self.label_2 = QtWidgets.QLabel(self.groupBox_2)
		self.label_2.setGeometry(QtCore.QRect(10, 25, 21, 16))
		self.label_2.setObjectName("label_2")
		self.ip = QtWidgets.QTextEdit(self.groupBox_2)
		self.ip.setGeometry(QtCore.QRect(30, 20, 121, 31))
		self.ip.setObjectName("ip")
		self.label_3 = QtWidgets.QLabel(self.groupBox_2)
		self.label_3.setGeometry(QtCore.QRect(160, 25, 47, 13))
		self.label_3.setObjectName("label_3")
		self.name = QtWidgets.QTextEdit(self.groupBox_2)
		self.name.setGeometry(QtCore.QRect(200, 20, 141, 31))
		self.name.setObjectName("name")
		self.label_4 = QtWidgets.QLabel(self.groupBox_2)
		self.label_4.setGeometry(QtCore.QRect(350, 25, 41, 16))
		self.label_4.setObjectName("label_4")
		self.password = QtWidgets.QTextEdit(self.groupBox_2)
		self.password.setGeometry(QtCore.QRect(380, 20, 121, 31))
		self.password.setObjectName("password")

		self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_3.setGeometry(QtCore.QRect(40, 80, 331, 221))
		self.groupBox_3.setObjectName("groupBox_3")
		self.areadisplay = QtWidgets.QTextEdit(self.groupBox_3)
		self.areadisplay.setGeometry(QtCore.QRect(10, 20, 311, 191))
		self.areadisplay.setObjectName("areadisplay")

		self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_4.setGeometry(QtCore.QRect(40, 310, 271, 161))
		self.groupBox_4.setObjectName("groupBox_4")
		self.label = QtWidgets.QLabel(self.groupBox_4)
		self.label.setGeometry(QtCore.QRect(10, 20, 111, 31))
		self.label.setObjectName("label")
		self.edtcreatefoldel = QtWidgets.QTextEdit(self.groupBox_4)
		self.edtcreatefoldel.setGeometry(QtCore.QRect(70, 20, 121, 31))
		self.edtcreatefoldel.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
		self.edtcreatefoldel.setObjectName("edtcreatefoldel")
		self.btncreatefolder = QtWidgets.QPushButton(self.groupBox_4)
		self.btncreatefolder.setGeometry(QtCore.QRect(200, 20, 61, 31))
		self.btncreatefolder.setObjectName("btncreatefolder")
		self.btncreatefolder.clicked.connect(self.addfolder)
		self.label_5 = QtWidgets.QLabel(self.groupBox_4)
		self.label_5.setGeometry(QtCore.QRect(10, 76, 111, 16))
		self.label_5.setObjectName("label_5")
		self.edtmovetofolder = QtWidgets.QTextEdit(self.groupBox_4)
		self.edtmovetofolder.setGeometry(QtCore.QRect(70, 70, 121, 31))
		self.edtmovetofolder.setObjectName("edtmovetofolder")
		self.btnmovetofolder = QtWidgets.QPushButton(self.groupBox_4)
		self.btnmovetofolder.setGeometry(QtCore.QRect(200, 70, 61, 31))
		self.btnmovetofolder.setObjectName("btnmovetofolder")
		self.btnmovetofolder.clicked.connect(self.movetofolder)
		self.label_6 = QtWidgets.QLabel(self.groupBox_4)
		self.label_6.setGeometry(QtCore.QRect(10, 120, 111, 31))
		self.label_6.setObjectName("label_6")
		self.edtdeletefolder = QtWidgets.QTextEdit(self.groupBox_4)
		self.edtdeletefolder.setGeometry(QtCore.QRect(70, 120, 121, 31))
		self.edtdeletefolder.setObjectName("edtdeletefolder")
		self.btndeletefolder = QtWidgets.QPushButton(self.groupBox_4)
		self.btndeletefolder.setGeometry(QtCore.QRect(200, 120, 61, 31))
		self.btndeletefolder.setObjectName("btndeletefolder")
		self.btndeletefolder.clicked.connect(self.deletefolder)
		
		self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_5.setGeometry(QtCore.QRect(320, 310, 251, 61))
		self.groupBox_5.setObjectName("groupBox_5")
		self.label_7 = QtWidgets.QLabel(self.groupBox_5)
		self.label_7.setGeometry(QtCore.QRect(10, 24, 101, 16))
		self.label_7.setObjectName("label_7")
		self.edtdeletefile = QtWidgets.QTextEdit(self.groupBox_5)
		self.edtdeletefile.setGeometry(QtCore.QRect(50, 20, 121, 31))
		self.edtdeletefile.setObjectName("edtdeletefile")
		self.btndeletefile = QtWidgets.QPushButton(self.groupBox_5)
		self.btndeletefile.setGeometry(QtCore.QRect(180, 20, 61, 31))
		self.btndeletefile.setObjectName("btndeletefile")
		self.btndeletefile.clicked.connect(self.deletefile)

		self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_6.setGeometry(QtCore.QRect(320, 374, 251, 98))
		self.groupBox_6.setObjectName("groupBox_6")
		self.label_9 = QtWidgets.QLabel(self.groupBox_6)
		self.label_9.setGeometry(QtCore.QRect(10, 26, 53, 16))
		self.label_9.setObjectName("label_9")
		self.edtoldname = QtWidgets.QTextEdit(self.groupBox_6)
		self.edtoldname.setGeometry(QtCore.QRect(70, 20, 101, 31))
		self.edtoldname.setObjectName("edtoldname")
		self.btnrename = QtWidgets.QPushButton(self.groupBox_6)
		self.btnrename.setGeometry(QtCore.QRect(180, 40, 61, 31))
		self.btnrename.setObjectName("btnrename")
		self.btnrename.clicked.connect(self.rename)
		self.label_10 = QtWidgets.QLabel(self.groupBox_6)
		self.label_10.setGeometry(QtCore.QRect(10, 68, 51, 16))
		self.label_10.setObjectName("label_10")
		self.edtnewname = QtWidgets.QTextEdit(self.groupBox_6)
		self.edtnewname.setGeometry(QtCore.QRect(70, 60, 101, 31))
		self.edtnewname.setObjectName("edtnewname")
		
		self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
		self.groupBox_7.setGeometry(QtCore.QRect(40, 474, 531, 98))
		self.groupBox_7.setObjectName("groupBox_7")
		self.label_12 = QtWidgets.QLabel(self.groupBox_7)
		self.label_12.setGeometry(QtCore.QRect(10, 26, 101, 16))
		self.label_12.setObjectName("label_12")
		self.edtup_downfile = QtWidgets.QTextEdit(self.groupBox_7)
		self.edtup_downfile.setGeometry(QtCore.QRect(110, 20, 241, 31))
		self.edtup_downfile.setObjectName("edtup_downfile")
		self.ChooseFile = QtWidgets.QPushButton(self.groupBox_7)
		self.ChooseFile.setGeometry(QtCore.QRect(360, 20, 81, 31))
		self.ChooseFile.setObjectName("ChooseFile")
		self.ChooseFile.clicked.connect(self.defChoosefile)
		self.btnupload = QtWidgets.QPushButton(self.groupBox_7)
		self.btnupload.setGeometry(QtCore.QRect(450, 20, 81, 31))
		self.btnupload.setObjectName("btnupload")
		self.btnupload.clicked.connect(self.uploadfile)
		self.label_11 = QtWidgets.QLabel(self.groupBox_7)
		self.label_11.setGeometry(QtCore.QRect(10, 66, 101, 16))
		self.label_11.setObjectName("label_11")
		self.edtnamefiledownload = QtWidgets.QTextEdit(self.groupBox_7)
		self.edtnamefiledownload.setGeometry(QtCore.QRect(130, 60, 104, 31))
		self.edtnamefiledownload.setObjectName("edtnamefiledownload")
		self.btndownload = QtWidgets.QPushButton(self.groupBox_7)
		self.btndownload.setGeometry(QtCore.QRect(250, 60, 91, 31))
		self.btndownload.setObjectName("btndownload")
		self.btndownload.clicked.connect(self.downloadfile)

		self.listWidget = QtWidgets.QListWidget(self.centralwidget)
		self.listWidget.setGeometry(QtCore.QRect(390, 180, 181, 111))
		self.listWidget.setObjectName("listWidget")
		self.listWidget.clicked.connect(self.clickeditem)
		self.listWidget.itemDoubleClicked.connect(self.doubleclick)

		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "FTP Client"))
		self.groupBox.setTitle(_translate("MainWindow", "Main"))
		self.btnquit.setText(_translate("MainWindow", "Quit"))
		self.btnreturnfolder.setText(_translate("MainWindow", "Return"))
		self.btninfoserver.setText(_translate("MainWindow", "Connect"))
		self.groupBox_2.setTitle(_translate("MainWindow", "Information Connect"))
		self.label_2.setText(_translate("MainWindow", "IP:"))
		self.ip.setText("127.0.0.1")
		self.label_3.setText(_translate("MainWindow", "Name: "))
		self.name.setText("tbquang")
		self.password.setText("12345")
		self.label_4.setText(_translate("MainWindow", "Pass: "))
		self.groupBox_3.setTitle(_translate("MainWindow", "Display"))
		self.groupBox_4.setTitle(_translate("MainWindow", "Folder "))
		self.label.setText(_translate("MainWindow", "New Folder"))
		self.btncreatefolder.setText(_translate("MainWindow", "Add"))
		self.label_5.setText(_translate("MainWindow", "Move Folder"))
		self.btnmovetofolder.setText(_translate("MainWindow", "Move"))
		self.label_6.setText(_translate("MainWindow", "Del Folder"))
		self.btndeletefolder.setText(_translate("MainWindow", "Delete"))
		self.groupBox_5.setTitle(_translate("MainWindow", "File"))
		self.label_7.setText(_translate("MainWindow", "Del File"))
		self.btndeletefile.setText(_translate("MainWindow", " Delete"))
		self.groupBox_6.setTitle(_translate("MainWindow", "Rename Folder/File"))
		self.label_9.setText(_translate("MainWindow", " Old Name"))
		self.btnrename.setText(_translate("MainWindow", "Rename"))
		self.label_10.setText(_translate("MainWindow", "New Name"))
		self.groupBox_7.setTitle(_translate("MainWindow", "Upload/Dowload File"))
		self.label_12.setText(_translate("MainWindow", "Choose  File UpLoad"))
		self.ChooseFile.setText(_translate("MainWindow", "Choose File"))
		self.btnupload.setText(_translate("MainWindow", "Upload"))
		self.label_11.setText(_translate("MainWindow", "Name File Download"))
		self.btndownload.setText(_translate("MainWindow", "Download"))



	#Hàm lấy IP 
	def getIP(self):
		ip = self.ip.toPlainText()
		return ip
	def getName(self):
		name = self.name.toPlainText()
		return name
	def getPass(self):
		password = self.password.toPlainText()
		return password
	#Hàm xủ lý nút Connected server
	def Connect(self):
		con = self.btninfoserver.clicked.connect(self.inforserver)
	def inforserver(self):
		ip = ui.getIP()
		user_name = ui.getName()
		password = ui.getPass()
		if user_name == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Warning!!!")
			msg.setInformativeText("Please! Enter your username")
			msg.setWindowTitle("Warning")
			msg.exec_()	
		elif password == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please! Enter your password")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.connect(ip,21)
				ftp_client.login(user_name,password)
				self.areadisplay.insertPlainText("Connected to Server: "+ftp_client.getwelcome()+"\n")
				dem = 0
				for name in ftp_client.nlst():
					self.listWidget.insertItem(dem, name)
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! Try Again")
				msg.setWindowTitle("Error")
				msg.exec_()
	#Hàm xử lý nút Chọn file
	def defChoosefile(self):
		root = tk.Tk()
		root.withdraw()
		file_path = filedialog.askopenfilename()
		self.edtup_downfile.setText(file_path)
	#Hàm xử lý nút lấy thông tin Folder
	def inforfolder(self):
		try:
			self.areadisplay.insertPlainText("Infomation folder: "+ ftp_client.pwd() + "\n")
			for name in ftp_client.nlst():
				self.areadisplay.insertPlainText(name+"\n")
			#self.areadisplay.insertPlainText("Infor: "+ftp_client.retrlines('LIST')+"\n")
		except:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Oppp! Something was wrong! Try Again")
			msg.setWindowTitle("Error")
			msg.exec_()

	#Hàm xử lý nút thêm folder
	def addfolder(self):
		name_folder = self.edtcreatefoldel.toPlainText()
		if name_folder == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name Folder")
			msg.setWindowTitle("Error")
			msg.exec_()
		elif bool(re.match('^[a-zA-Z0-9]*$',name_folder))==False:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Names cannot contain special characters")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.mkd(name_folder)
				ftp_client.cwd(name_folder)
				for i in range(self.listWidget.count()):
					itemremove = self.listWidget.item(0)
					self.listWidget.takeItem(self.listWidget.row(itemremove))
				dem = 0
				for name in ftp_client.nlst():
					self.listWidget.insertItem(dem, name)
				self.areadisplay.insertPlainText("Created Successfully. The current directory: "+ ftp_client.pwd()+"\n")
				self.edtcreatefoldel.setText("")
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("The folder is available or no connection to server!!Please Enter Another Name or Connect to server before performing the operation ")
				msg.setWindowTitle("Error")
				msg.exec_()

	#Hàm xử lý nút xóa folder
	def deletefolder(self):
		name_folder_delete = self.edtdeletefolder.toPlainText()
		if name_folder_delete == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name Folder")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.rmd(name_folder_delete)
				for i in range(self.listWidget.count()):
					itemremove = self.listWidget.item(0)
					self.listWidget.takeItem(self.listWidget.row(itemremove))
				dem = 0
				for name in ftp_client.nlst():
					self.listWidget.insertItem(dem, name)
				self.areadisplay.insertPlainText("Deleted Successfully "+name_folder_delete+"\n")
				self.edtdeletefolder.setText("")               
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The folder does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

	#Hàm xử lý nút xóa file
	def deletefile(self):
		name_file_delete = self.edtdeletefile.toPlainText()
		if name_file_delete == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name Folder")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				ftp_client.delete(name_file_delete)
				for i in range(self.listWidget.count()):
					itemremove = self.listWidget.item(0)
					self.listWidget.takeItem(self.listWidget.row(itemremove))
				dem = 0
				for name in ftp_client.nlst():
					self.listWidget.insertItem(dem, name)
				self.areadisplay.insertPlainText("Deleted Successfully "+name_file_delete+"\n")
				self.edtdeletefile.setText("")
				
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The file does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

	#Hàm xử lý nút kiểm tra file
	def checkfile(self):
		name_file_check = self.edtdeletefile.toPlainText()
		if name_file_check == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Please Enter Name File")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				self.areadisplay.insertPlainText("File Size: "+ftp_client.size(name_file_check)+"\n")
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! 550 SIZE not allowed in ASCII mode.")
				msg.setWindowTitle("Error")
				msg.exec_()


	#Hàm xử lý nút đổi tên file            
	def rename(self):
		old_name = self.edtoldname.toPlainText()
		new_name = self.edtnewname.toPlainText()
		if old_name == "" or new_name == "" :
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Warning!!!")
			msg.setInformativeText("Please Enter Name Folder/File")
			msg.setWindowTitle("Warning")
			msg.exec_()
		elif bool(re.match('^[a-zA-Z0-9.]*$',new_name))==False:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Names cannot contain special characters")
			msg.setWindowTitle("Error")
			msg.exec_()

		else:
			try:
				ftp_client.rename(old_name,new_name)
				for i in range(self.listWidget.count()):
					itemremove = self.listWidget.item(0)
					self.listWidget.takeItem(self.listWidget.row(itemremove))
				dem = 0
				for name in ftp_client.nlst():
					self.listWidget.insertItem(dem, name)
				self.areadisplay.insertPlainText("Changed successfully from "+old_name+ " to " +new_name+ "\n")
				self.edtoldname.setText(""),
				self.edtnewname.setText("")  
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The file does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

	def doubleclick(self):
		item = self.listWidget.currentItem()
		self.edtmovetofolder.setText(item.text())

	#Hàm xử lý nút chuyển đến folder
	def movetofolder(self):
		name_folder_move = self.edtmovetofolder.toPlainText()
		if name_folder_move == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Warning!!!")
			msg.setInformativeText("Please Enter Name Folder!!")
			msg.setWindowTitle("Warning")
			msg.exec_()
		else:
			try:
				ftp_client.cwd(name_folder_move)
				for i in range(self.listWidget.count()):
					itemremove = self.listWidget.item(0)
					self.listWidget.takeItem(self.listWidget.row(itemremove))
				dem = 0
				for name in ftp_client.nlst():
					self.listWidget.insertItem(dem, name)
				self.areadisplay.insertPlainText("Successfully moved to the directory. The current directory: "+ftp_client.pwd()+"\n")
				self.edtmovetofolder.setText("")
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Critical)
				msg.setText("Error!!!")
				msg.setInformativeText("Oppp! Something was wrong! The folder does not exist!")
				msg.setWindowTitle("Error")
				msg.exec_()

		
	#Hàm xử lý nút trở về 1 folder trước    
	def returnfolder(self):
		try:
			ftp_client.cwd("..")
			for i in range(self.listWidget.count()):
					itemremove = self.listWidget.item(0)
					self.listWidget.takeItem(self.listWidget.row(itemremove))
			dem = 0
			for name in ftp_client.nlst():
				self.listWidget.insertItem(dem, name)
			self.areadisplay.insertPlainText("Successfully moved to the directory. The current directory: "+ftp_client.pwd()+"\n")
		except:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("Oppp! Something was wrong!Being in the original folder")
			msg.setWindowTitle("Error")
			msg.exec_()

	#Hàm xử lý nút upload file
	#Điều kiện file upload lên từ client phải ở cùng hoặc sâu hơn vị trí đặt file chạy ftp-client (file code .python) hoặc phải trỏ được đường dẫn chính xác đến vị trí file.
	#Muốn upload đến thư mục nào đó thì thực hiện kết nối đến thư mục đó trên server.
	def uploadfile(self):
		link_file_upload = self.edtup_downfile.toPlainText()
		if link_file_upload == "": 
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Error!!!")
			msg.setInformativeText("Please insert name file need to upload!")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			leng = len(link_file_upload)
			chuoi = link_file_upload.split("/")
			for tu in chuoi:
				name_file_upload = tu
			file_upload = open(link_file_upload,"rb") 
			ftp_client.storbinary("{CMD} {FileName}".
				format(CMD="STOR",FileName=name_file_upload),
				file_upload)
			print(file_upload.read()) 
			print(name_file_upload)
			file_upload.close()
			self.edtup_downfile.setText("")
			for i in range(self.listWidget.count()):
					itemremove = self.listWidget.item(0)
					self.listWidget.takeItem(self.listWidget.row(itemremove))
			dem = 0
			for name in ftp_client.nlst():
				self.listWidget.insertItem(dem, name)
			self.areadisplay.insertPlainText("Uploaded Successfully file: "+name_file_upload+"\n")

	def clickeditem(self):
		item = self.listWidget.currentItem()
		self.edtnamefiledownload.setText(item.text())
	#Hàm xử lý nút downloadfile
	#Muốn download file nào, thực hiện trỏ thư mục server chứa file đó
	#Kết nối vào FTP server folder chứa thư mục và thực hiện download
	def downloadfile(self):
		name_file_download = self.edtnamefiledownload.toPlainText()
		if name_file_download == "":
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Warning)
			msg.setText("Error!!!")
			msg.setInformativeText("Please insert name file need to download!")
			msg.setWindowTitle("Error")
			msg.exec_()
		else:
			try:
				file_path = name_file_download
				file_name = name_file_download
				file_stream = open(file_path,"wb")      
				ftp_client.retrbinary('RETR {}'.format(file_name),
							file_stream.write, 1024)
				file_stream.close() 
				self.areadisplay.insertPlainText("Download Successfully file: "+name_file_download+"\n") 
			except:
				msg = QtWidgets.QMessageBox()
				msg.setIcon(QtWidgets.QMessageBox.Warning)
				msg.setText("Error!!!")
				msg.setInformativeText("Please insert name file need to download!")
				msg.setWindowTitle("Error")
				msg.exec_()

	def defquit(self):
		try:
			ftp_client.quit()
			self.areadisplay.insertPlainText("Closed connection. See you again!!\n") 
		except:
			msg = QtWidgets.QMessageBox()
			msg.setIcon(QtWidgets.QMessageBox.Critical)
			msg.setText("Error!!!")
			msg.setInformativeText("No connection!!!")
			msg.setWindowTitle("Error")
			msg.exec_()
#Main           

if __name__ == "__main__":
	ftp_client = FTP()
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	MainWindow1 = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.Connect()
	MainWindow.show()
	sys.exit(app.exec_()) 
